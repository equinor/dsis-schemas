#!/usr/bin/env python3
"""Extract structured metadata from the OpenWorks Common Model Teiid DDL.

Captures what the JSON schemas don't carry: primary/unique/foreign keys,
column options (creatable/updatable, units, media, complex-type structure),
entity options, native source tables and per-column source expressions,
INSTEAD OF triggers (insert/update/delete support), virtual functions and procedures.

Usage:
    python scripts/extract_ddl_metadata.py [ddl_path] [output_json_path]

A Markdown rendering is written next to the JSON output (same name, .md).
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DDL = ROOT / "OpenWorksCommonModel_10_7.ddl"
DEFAULT_OUT = ROOT / "common-model-ddl-metadata.json"

MODEL_PREFIX = "OpenWorksCommonModel:"
STMT_RE = re.compile(
    r"^[ \t]*CREATE\s+(VIEW|TRIGGER|VIRTUAL\s+FUNCTION|VIRTUAL\s+PROCEDURE)\b",
    re.IGNORECASE | re.MULTILINE,
)
NATIVE_TABLE_RE = re.compile(r"\bopenworks_sm\.(\w+)", re.IGNORECASE)
WRITE_RE = re.compile(
    r"\b(INSERT\s+INTO|UPDATE|DELETE\s+FROM)\s+openworks_sm\.(\w+)", re.IGNORECASE
)


def strip_comments(text):
    out, i, n = [], 0, len(text)
    while i < n:
        c = text[i]
        if c in ("'", '"'):
            j = i + 1
            while j < n:
                if text[j] == c:
                    if j + 1 < n and text[j + 1] == c:
                        j += 2
                        continue
                    break
                j += 1
            out.append(text[i : j + 1])
            i = j + 1
        elif text.startswith("/*", i):
            end = text.find("*/", i + 2)
            i = n if end < 0 else end + 2
            out.append(" ")
        elif text.startswith("--", i):
            end = text.find("\n", i)
            i = n if end < 0 else end
        else:
            out.append(c)
            i += 1
    return "".join(out)


def scan(text, start=0):
    """Yield (index, char, depth) for characters outside string literals."""
    depth, i, n = 0, start, len(text)
    while i < n:
        c = text[i]
        if c in ("'", '"'):
            j = i + 1
            while j < n:
                if text[j] == c:
                    if j + 1 < n and text[j + 1] == c:
                        j += 2
                        continue
                    break
                j += 1
            i = j + 1
            continue
        if c == "(":
            depth += 1
        elif c == ")":
            depth -= 1
        yield i, c, depth
        i += 1


def matching_paren(text, open_idx):
    for i, c, depth in scan(text, open_idx):
        if c == ")" and depth == 0:
            return i
    raise ValueError(f"Unbalanced parenthesis at {open_idx}")


def split_top(text, sep=","):
    parts, last = [], 0
    for i, c, depth in scan(text):
        if c == sep and depth == 0:
            parts.append(text[last:i])
            last = i + 1
    parts.append(text[last:])
    return [p.strip() for p in parts if p.strip()]


def find_top_keyword(text, keyword, start=0):
    pat = re.compile(rf"\b{keyword}\b", re.IGNORECASE)
    for i, _c, depth in scan(text, start):
        if depth == 0 and pat.match(text, i) and (i == 0 or not (text[i - 1].isalnum() or text[i - 1] == "_")):
            return i
    return -1


def parse_value(raw):
    raw = raw.strip()
    if len(raw) >= 2 and raw[0] == raw[-1] == "'":
        val = raw[1:-1].replace("''", "'")
        low = val.lower()
        if low in ("true", "false"):
            return low == "true"
        if val[:1] in "[{":
            try:
                return json.loads(val)
            except json.JSONDecodeError:
                return val
        return val
    low = raw.lower()
    if low in ("true", "false"):
        return low == "true"
    try:
        return int(raw)
    except ValueError:
        try:
            return float(raw)
        except ValueError:
            return raw


def parse_options(body):
    opts = {}
    for item in split_top(body):
        m = re.match(r'("(?:[^"]|"")*"|[\w.:]+)\s+(.*)$', item, re.DOTALL)
        if not m:
            continue
        key = m.group(1).strip('"')
        opts[key] = parse_value(m.group(2))
    return opts


def extract_options_clause(text):
    """Return (options_dict, text_without_options) for a trailing OPTIONS(...) clause."""
    m = re.search(r"\bOPTIONS\s*\(", text, re.IGNORECASE)
    if not m:
        return {}, text
    close = matching_paren(text, m.end() - 1)
    return parse_options(text[m.end() : close]), text[: m.start()] + text[close + 1 :]


def column_options(opts):
    """Strip the 'OpenWorksCommonModel:<Entity>.<column>.' prefix from option keys."""
    result = {}
    for key, val in opts.items():
        if key.startswith(MODEL_PREFIX):
            key = key.rsplit(".", 1)[-1]
        result[key] = val
    return result


def parse_type(tokens_text):
    m = re.match(r"(\w+)\s*(?:\(\s*([^)]*)\))?", tokens_text)
    sql_type = m.group(1).upper()
    col = {"type": sql_type}
    if m.group(2):
        args = [a.strip() for a in m.group(2).split(",")]
        if sql_type in ("DECIMAL", "NUMERIC") or len(args) > 1:
            col["precision"] = int(args[0])
            if len(args) > 1:
                col["scale"] = int(args[1])
        else:
            col["length"] = int(args[0])
    return col, tokens_text[m.end() :]


def parse_column(item):
    m = re.match(r'("[^"]+"|\w+)\s+', item)
    name = m.group(1).strip('"')
    rest = item[m.end() :]
    opts, rest = extract_options_clause(rest)
    col, rest = parse_type(rest.strip())
    col["name"] = name
    col["nullable"] = not re.search(r"\bNOT\s+NULL\b", rest, re.IGNORECASE)
    if re.search(r"\bAUTO_INCREMENT\b", rest, re.IGNORECASE):
        col["auto_increment"] = True
    d = re.search(r"\bDEFAULT\s+('(?:[^']|'')*'|[\w.\-]+)", rest, re.IGNORECASE)
    if d:
        col["default"] = parse_value(d.group(1))
    if opts:
        col["options"] = column_options(opts)
    return col


def parse_cols_list(text):
    return [c.strip().strip('"') for c in text.split(",")]


def parse_constraint(item):
    m = re.match(r"CONSTRAINT\s+(\w+)\s+(.*)$", item, re.IGNORECASE | re.DOTALL)
    name, rest = m.group(1), m.group(2)
    pk = re.match(r"PRIMARY\s+KEY\s*\(([^)]*)\)", rest, re.IGNORECASE)
    if pk:
        return "primary_key", {"name": name, "columns": parse_cols_list(pk.group(1))}
    uk = re.match(r"UNIQUE\s*\(([^)]*)\)", rest, re.IGNORECASE)
    if uk:
        return "unique", {"name": name, "columns": parse_cols_list(uk.group(1))}
    fk = re.match(
        r"FOREIGN\s+KEY\s*\(([^)]*)\)\s*REFERENCES\s+(\w+)\s*(?:\(([^)]*)\))?",
        rest,
        re.IGNORECASE,
    )
    if fk:
        return "foreign_key", {
            "name": name,
            "columns": parse_cols_list(fk.group(1)),
            "references_entity": fk.group(2),
            "references_columns": parse_cols_list(fk.group(3)) if fk.group(3) else [],
        }
    return "other", {"name": name, "definition": " ".join(rest.split())}


def native_tables(text):
    seen = {}
    for t in NATIVE_TABLE_RE.findall(text):
        seen.setdefault(t.lower(), t)
    return sorted(seen.values(), key=str.lower)


def select_list(query):
    """Return the top-level select expressions of the first SELECT in the query."""
    m = re.search(r"\bSELECT\b", query, re.IGNORECASE)
    if not m:
        return []
    start = m.end()
    d = re.match(r"\s*DISTINCT\b", query[start:], re.IGNORECASE)
    if d:
        start += d.end()
    end = find_top_keyword(query, "FROM", start)
    return split_top(query[start : end if end >= 0 else len(query)])


def strip_alias(expr):
    expr = " ".join(expr.split())
    m = re.match(r"(.*?)\s+AS\s+(\"[^\"]+\"|\w+)$", expr, re.IGNORECASE | re.DOTALL)
    return m.group(1) if m else expr


def parse_view(stmt):
    m = re.match(r"\s*CREATE\s+VIEW\s+(\w+)\s*\(", stmt, re.IGNORECASE)
    name = m.group(1)
    open_idx = m.end() - 1
    close = matching_paren(stmt, open_idx)
    body = stmt[open_idx + 1 : close]
    tail = stmt[close + 1 :]

    as_idx = find_top_keyword(tail, "AS")
    head, query = (tail[:as_idx], tail[as_idx + 2 :]) if as_idx >= 0 else (tail, "")
    view_opts, _ = extract_options_clause(head)
    query = query.strip().rstrip(";").strip()

    entity = {
        "name": name,
        "updatable": view_opts.pop("UPDATABLE", None),
        "implemented": view_opts.pop(f"{name}.IMPLEMENTED", None),
        "options": view_opts,
        "columns": [],
        "primary_key": None,
        "unique_constraints": [],
        "foreign_keys": [],
        "other_constraints": [],
        "native_source_tables": native_tables(query),
        "triggers": {},
    }
    if not entity["options"]:
        del entity["options"]

    for item in split_top(body):
        if re.match(r"CONSTRAINT\b", item, re.IGNORECASE):
            kind, data = parse_constraint(item)
            if kind == "primary_key":
                entity["primary_key"] = data
            elif kind == "unique":
                entity["unique_constraints"].append(data)
            elif kind == "foreign_key":
                entity["foreign_keys"].append(data)
            else:
                entity["other_constraints"].append(data)
        else:
            entity["columns"].append(parse_column(item))

    # Teiid maps view columns to the select list positionally.
    exprs = select_list(query)
    if len(exprs) == len(entity["columns"]):
        for col, expr in zip(entity["columns"], exprs):
            col["source_expression"] = strip_alias(expr)
    elif exprs:
        entity["source_mapping_warning"] = (
            f"select list has {len(exprs)} items but view declares {len(entity['columns'])} columns"
        )
    if not entity["other_constraints"]:
        del entity["other_constraints"]
    return entity


def parse_trigger(stmt):
    m = re.match(
        r"\s*CREATE\s+TRIGGER\s+ON\s+(\w+)\s+INSTEAD\s+OF\s+(INSERT|UPDATE|DELETE)\b",
        stmt,
        re.IGNORECASE,
    )
    if not m:
        return None
    writes = {}
    for op, table in WRITE_RE.findall(stmt):
        op = op.split()[0].upper()
        writes.setdefault(op, {}).setdefault(table.lower(), table)
    errors = sorted(set(re.findall(r"ERROR\s+'((?:[^']|'')*)'", stmt, re.IGNORECASE)))
    trig = {
        "entity": m.group(1),
        "event": m.group(2).upper(),
        "native_writes": {op: sorted(t.values(), key=str.lower) for op, t in writes.items()},
        "native_objects_referenced": native_tables(stmt),
    }
    if errors:
        trig["error_messages"] = errors
    return trig


def parse_params(text):
    params = []
    for p in split_top(text):
        parts = p.split()
        if len(parts) >= 2:
            params.append({"name": parts[0], "type": " ".join(parts[1:])})
    return params


def parse_routine(stmt, kind):
    m = re.match(rf"\s*CREATE\s+VIRTUAL\s+{kind}\s+(\w+)\s*\(", stmt, re.IGNORECASE)
    name = m.group(1)
    close = matching_paren(stmt, m.end() - 1)
    routine = {"name": name, "parameters": parse_params(stmt[m.end() : close])}
    rest = stmt[close + 1 :]
    r = re.match(r"\s*RETURNS\s*", rest, re.IGNORECASE)
    if r:
        rest = rest[r.end() :]
        if rest.startswith("("):
            rclose = matching_paren(rest, 0)
            routine["returns"] = parse_params(rest[1:rclose])
            rest = rest[rclose + 1 :]
        else:
            t = re.match(r"(\w+)", rest)
            routine["returns"] = t.group(1).upper()
            rest = rest[t.end() :]
    as_idx = find_top_keyword(rest, "AS")
    head = rest[:as_idx] if as_idx >= 0 else rest
    opts, _ = extract_options_clause(head)
    if opts:
        routine["options"] = opts
    if as_idx >= 0:
        routine["native_objects_referenced"] = native_tables(rest[as_idx:])
    return routine


def extract(ddl_text):
    text = strip_comments(ddl_text)
    starts = [m.start() for m in STMT_RE.finditer(text)] + [len(text)]
    entities, functions, procedures, triggers = {}, [], [], []

    for a, b in zip(starts, starts[1:]):
        stmt = text[a:b]
        kind = STMT_RE.match(text, a).group(1).upper().split()[-1]
        if kind == "VIEW":
            e = parse_view(stmt)
            entities[e["name"]] = e
        elif kind == "TRIGGER":
            t = parse_trigger(stmt)
            if t:
                triggers.append(t)
        elif kind == "FUNCTION":
            functions.append(parse_routine(stmt, "FUNCTION"))
        elif kind == "PROCEDURE":
            procedures.append(parse_routine(stmt, "PROCEDURE"))

    by_lower = {k.lower(): k for k in entities}
    for t in triggers:
        key = by_lower.get(t.pop("entity").lower())
        if key:
            entities[key]["triggers"][t.pop("event")] = t

    relationships = [
        {
            "from_entity": e["name"],
            "from_columns": fk["columns"],
            "to_entity": by_lower.get(fk["references_entity"].lower(), fk["references_entity"]),
            "to_columns": fk["references_columns"],
            "constraint": fk["name"],
        }
        for e in entities.values()
        for fk in e["foreign_keys"]
    ]
    for e in entities.values():
        e["supported_operations"] = ["SELECT"] + [op for op in ("INSERT", "UPDATE", "DELETE") if op in e["triggers"]]
        e["referenced_by"] = sorted(
            {r["from_entity"] for r in relationships if r["to_entity"] == e["name"]}
        )

    return {
        "source": "OpenWorksCommonModel DDL",
        "summary": {
            "entities": len(entities),
            "foreign_keys": len(relationships),
            "triggers": len(triggers),
            "functions": len(functions),
            "procedures": len(procedures),
        },
        "entities": dict(sorted(entities.items(), key=lambda kv: kv[0].lower())),
        "relationships": relationships,
        "functions": functions,
        "procedures": procedures,
    }


def md_cell(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def md_anchor(name):
    return name.lower()


def md_type(col):
    t = col["type"]
    if "length" in col:
        return f"{t}({col['length']})"
    if "precision" in col:
        return f"{t}({col['precision']}{', ' + str(col['scale']) if 'scale' in col else ''})"
    return t


def md_column_notes(col, fk_cols, pk_cols):
    opts = col.get("options", {})
    notes = []
    if col["name"] in pk_cols:
        notes.append("PK")
    if col["name"] in fk_cols:
        notes.append(f"FK → [{fk_cols[col['name']]}](#{md_anchor(fk_cols[col['name']])})")
    if col.get("auto_increment"):
        notes.append("auto")
    if "default" in col:
        notes.append(f"default `{col['default']}`")
    if opts.get("isCreatable") is False or opts.get("isUpdatable") is False:
        notes.append("read-only")
    if opts.get("isImplemented") is False:
        notes.append("not implemented")
    if "unitField" in opts:
        notes.append(f"unit in `{opts['unitField']}`")
    if "unitType" in opts:
        notes.append(f"unit type `{opts['unitType']}`")
    if "unitTypeAttribute" in opts:
        notes.append(f"unit type from `{opts['unitTypeAttribute']}`")
    if opts.get("isSpatial"):
        notes.append("spatial")
    if opts.get("isMedia"):
        ctype = opts.get("mediaContentType")
        notes.append(f"media `{ctype}`" if ctype else "media")
    if "elementType" in opts:
        notes.append(f"element `{opts['elementType']}`")
    if "elementStruct" in opts:
        struct = opts["elementStruct"]
        if isinstance(struct, list):
            fields = ", ".join(f"{f.get('name')}:{f.get('type')}" for f in struct if isinstance(f, dict))
            notes.append(f"struct `{{{fields}}}`")
    return "; ".join(notes)


def to_markdown(result):
    s = result["summary"]
    lines = [
        "# OpenWorks Common Model – DDL Metadata",
        "",
        "Generated by `scripts/extract_ddl_metadata.py`. Do not edit by hand.",
        "",
        f"- Entities: {s['entities']}",
        f"- Foreign keys: {s['foreign_keys']}",
        f"- Triggers: {s['triggers']}",
        f"- Functions: {s['functions']}",
        f"- Procedures: {s['procedures']}",
        "",
        "## Entity Index",
        "",
        "| Entity | Operations | Primary Key | Columns | Native Source Tables |",
        "|---|---|---|---|---|",
    ]
    for e in result["entities"].values():
        pk = ", ".join(e["primary_key"]["columns"]) if e["primary_key"] else "–"
        ops = ", ".join(op for op in e["supported_operations"])
        lines.append(
            f"| [{e['name']}](#{md_anchor(e['name'])}) | {ops} | {md_cell(pk)} | {len(e['columns'])} | "
            f"{md_cell(', '.join(e['native_source_tables']))} |"
        )

    lines += ["", "## Entities", ""]
    for e in result["entities"].values():
        pk_cols = set(e["primary_key"]["columns"]) if e["primary_key"] else set()
        fk_cols = {c: fk["references_entity"] for fk in e["foreign_keys"] for c in fk["columns"]}
        lines += [f"### {e['name']}", ""]
        lines.append(f"- Updatable: `{e['updatable']}` · Implemented: `{e['implemented']}`")
        lines.append(f"- Operations: {', '.join(e['supported_operations'])}")
        if e["native_source_tables"]:
            lines.append(f"- Native source tables: {', '.join(f'`{t}`' for t in e['native_source_tables'])}")
        if e["unique_constraints"]:
            uks = "; ".join(f"`{u['name']}` ({', '.join(u['columns'])})" for u in e["unique_constraints"])
            lines.append(f"- Unique: {uks}")
        if e["referenced_by"]:
            refs = ", ".join(f"[{r}](#{md_anchor(r)})" for r in e["referenced_by"])
            lines.append(f"- Referenced by: {refs}")
        if e.get("source_mapping_warning"):
            lines.append(f"- Note: {e['source_mapping_warning']}")
        lines += ["", "| Column | Type | Null | Notes | Source |", "|---|---|---|---|---|"]
        for c in e["columns"]:
            src = c.get("source_expression", "")
            lines.append(
                f"| `{c['name']}` | {md_type(c)} | {'Y' if c['nullable'] else 'N'} | "
                f"{md_cell(md_column_notes(c, fk_cols, pk_cols))} | {('`' + md_cell(src) + '`') if src else ''} |"
            )
        if e["triggers"]:
            lines += ["", "| Trigger | Writes |", "|---|---|"]
            for event, t in e["triggers"].items():
                writes = "; ".join(f"{op} {', '.join(tbls)}" for op, tbls in t["native_writes"].items())
                lines.append(f"| {event} | {md_cell(writes) or '–'} |")
        lines.append("")

    lines += ["## Functions", "", "| Name | Parameters | Returns | Implementation |", "|---|---|---|---|"]
    for f in result["functions"]:
        params = ", ".join(f"{p['name']} {p['type']}" for p in f["parameters"])
        opts = f.get("options", {})
        impl = f"{opts.get('JAVA_CLASS', '')}.{opts.get('JAVA_METHOD', '')}".strip(".")
        lines.append(f"| `{f['name']}` | {md_cell(params)} | {f.get('returns', '')} | `{impl}` |")

    lines += ["", "## Procedures", "", "| Name | Parameters | Returns | Native Objects |", "|---|---|---|---|"]
    for p in result["procedures"]:
        params = ", ".join(f"{x['name']} {x['type']}" for x in p["parameters"])
        ret = p.get("returns", "")
        if isinstance(ret, list):
            ret = ", ".join(f"{x['name']} {x['type']}" for x in ret)
        native = ", ".join(p.get("native_objects_referenced", []))
        lines.append(f"| `{p['name']}` | {md_cell(params)} | {md_cell(ret)} | {md_cell(native)} |")
    return "\n".join(lines) + "\n"


def main():
    ddl = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_DDL
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_OUT
    result = extract(ddl.read_text(encoding="utf-8", errors="replace"))
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    md_out = out.with_suffix(".md")
    md_out.write_text(to_markdown(result), encoding="utf-8")
    print(f"Wrote {out} and {md_out}: {result['summary']}")
    warnings = [e["name"] for e in result["entities"].values() if "source_mapping_warning" in e]
    if warnings:
        print(f"Column source mapping skipped for {len(warnings)} entities: {', '.join(warnings)}")


if __name__ == "__main__":
    main()
