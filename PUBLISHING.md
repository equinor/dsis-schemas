# Publishing Guide for dsis-model-sdk

This guide explains how to publish new versions of the `dsis-model-sdk` package to PyPI.

## Prerequisites

### 1. PyPI Account Setup

1. Create an account on [PyPI](https://pypi.org/account/register/)
2. Enable Two-Factor Authentication (2FA) for security
3. Create an API token at https://pypi.org/manage/account/token/

### 2. GitHub Repository Setup

#### Configure PyPI Trusted Publishing

1. Go to your PyPI account settings: https://pypi.org/manage/account/publishing/
2. Add a new pending publisher with these details:
   - **PyPI Project Name**: `dsis-model-sdk`
   - **Owner**: `equinor`
   - **Repository name**: `dsis-schemas`
   - **Workflow name**: `publish-to-pypi.yml`
   - **Environment name**: `release`

#### Configure GitHub Environment

1. Go to your GitHub repository settings
2. Navigate to **Environments** → **New environment**
3. Create an environment named `release`
4. (Optional) Add protection rules:
   - Required reviewers
   - Wait timer
   - Deployment branches (only tags matching `v*`)

## Publishing Process

### Step 1: Update Version Number

Edit `pyproject.toml` and update the version number:

```toml
[project]
name = "dsis-model-sdk"
version = "1.0.1"  # Update this
```

Follow [Semantic Versioning](https://semver.org/):
- **MAJOR** version (1.x.x): Incompatible API changes
- **MINOR** version (x.1.x): New functionality, backwards compatible
- **PATCH** version (x.x.1): Bug fixes, backwards compatible

### Step 2: Update Changelog

Update `README.md` or create a `CHANGELOG.md` with release notes:

```markdown
## [1.0.1] - 2025-10-13

### Added
- New feature X
- Support for Y

### Fixed
- Bug fix Z

### Changed
- Updated dependency versions
```

### Step 3: Commit Changes

```bash
git add pyproject.toml README.md
git commit -m "chore: bump version to 1.0.1"
git push origin main
```

### Step 4: Create and Push Git Tag

```bash
# Create an annotated tag
git tag -a v1.0.1 -m "Release version 1.0.1"

# Push the tag to GitHub
git push origin v1.0.1
```

### Step 5: Monitor the Release

1. Go to **Actions** tab in your GitHub repository
2. Watch the "Publish to PyPI" workflow run
3. Verify the build completes successfully
4. Check that the package appears on PyPI: https://pypi.org/project/dsis-model-sdk/

## Testing Before Release

### Local Build Test

Test the build locally before creating a tag:

```bash
# Install build tools
pip install build twine

# Build the package
python -m build

# Check the built package
twine check dist/*

# Test installation locally
pip install dist/dsis_model_sdk-1.0.1-py3-none-any.whl

# Test imports
python -c "import dsis_model_sdk; print('Success!')"
```

### Test on TestPyPI (Optional)

You can test publishing to TestPyPI first:

1. Create an account on [TestPyPI](https://test.pypi.org/)
2. Create an API token
3. Publish manually:

```bash
# Build the package
python -m build

# Upload to TestPyPI
twine upload --repository testpypi dist/*

# Test installation from TestPyPI
pip install --index-url https://test.pypi.org/simple/ dsis-model-sdk
```

## Automated Workflows

### Test Build Workflow

Runs on every push to `main` and on pull requests:
- Builds the package
- Validates with `twine check`
- Tests installation
- Verifies imports work correctly

### Publish to PyPI Workflow

Runs only when a tag matching `v*` is pushed:
- Builds the package
- Publishes to PyPI using trusted publishing
- No API tokens needed (uses OIDC)

## Troubleshooting

### Build Fails

**Issue**: Package build fails with missing files

**Solution**: Check `MANIFEST.in` and ensure all necessary files are included

### Import Errors After Installation

**Issue**: `ModuleNotFoundError` when importing the package

**Solution**: Verify `pyproject.toml` has correct package configuration:
```toml
[tool.setuptools.packages.find]
include = ["dsis_model_sdk*"]
```

### PyPI Upload Fails

**Issue**: Authentication error or permission denied

**Solution**: 
1. Verify trusted publishing is configured correctly on PyPI
2. Check GitHub environment name matches (`release`)
3. Ensure workflow file name matches (`publish-to-pypi.yml`)

### Version Already Exists

**Issue**: PyPI rejects upload because version already exists

**Solution**: 
- PyPI does not allow re-uploading the same version
- Increment the version number in `pyproject.toml`
- Create a new tag with the new version

## Package Information

- **Package Name**: `dsis-model-sdk`
- **PyPI URL**: https://pypi.org/project/dsis-model-sdk/
- **Repository**: https://github.com/equinor/dsis-schemas
- **Documentation**: https://github.com/equinor/dsis-schemas/blob/main/README.md

## Installation for Users

Once published, users can install the package with:

```bash
pip install dsis-model-sdk
```

Or with specific version:

```bash
pip install dsis-model-sdk==1.0.1
```

## Support

For issues or questions:
- Open an issue: https://github.com/equinor/dsis-schemas/issues
- Contact: dsis@equinor.com

