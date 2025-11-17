# Publishing Guide for Zaban Python Package

This guide explains how to build and publish the Zaban Python client to PyPI.

## Prerequisites

1. **Python 3.8+** installed
2. **PyPI account** (create at https://pypi.org/account/register/)
3. **TestPyPI account** for testing (create at https://test.pypi.org/account/register/)
4. **API tokens** from PyPI and TestPyPI

## Setup

### 1. Install Build Tools

```bash
pip install build twine
```

### 2. Create PyPI API Tokens

1. Go to https://pypi.org/manage/account/token/
2. Create a new API token with scope for your project
3. Save the token securely (starts with `pypi-`)

For TestPyPI:
1. Go to https://test.pypi.org/manage/account/token/
2. Create a token
3. Save it securely

### 3. Configure Credentials (Optional)

Create `~/.pypirc`:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-YOUR_TOKEN_HERE

[testpypi]
username = __token__
password = pypi-YOUR_TEST_TOKEN_HERE
repository = https://test.pypi.org/legacy/
```

## Building the Package

### 1. Update Version

Update version in `zaban/version.py`:

```python
__version__ = "0.1.1"  # Increment version
```

### 2. Update CHANGELOG

Add entry to `CHANGELOG.md`:

```markdown
## [0.1.1] - 2025-11-18

### Added
- New feature description

### Fixed
- Bug fix description
```

### 3. Build the Package

```bash
# Clean previous builds
rm -rf dist/ build/ *.egg-info

# Build source distribution and wheel
python -m build
```

This creates:
- `dist/zaban-0.1.0.tar.gz` (source distribution)
- `dist/zaban-0.1.0-py3-none-any.whl` (wheel)

### 4. Check the Package

```bash
# Check package for errors
twine check dist/*
```

## Publishing

### Test on TestPyPI First

Always test on TestPyPI before publishing to real PyPI:

```bash
# Upload to TestPyPI
twine upload --repository testpypi dist/*

# Install from TestPyPI to verify
pip install --index-url https://test.pypi.org/simple/ zaban
```

Test the installed package:

```python
from zaban import Zaban
client = Zaban(api_key="sk-test")
print(client)
```

### Publish to PyPI

Once verified on TestPyPI:

```bash
# Upload to real PyPI
twine upload dist/*
```

Enter your PyPI credentials (or use token from ~/.pypirc).

### Verify Publication

```bash
# Install from PyPI
pip install zaban

# Test
python -c "from zaban import Zaban; print(Zaban.__doc__)"
```

## GitHub Actions (Automated)

The repository includes GitHub Actions workflows for automated publishing.

### Setup Secrets

In your GitHub repository settings, add secrets:

1. Go to Settings → Secrets and variables → Actions
2. Add secrets:
   - `PYPI_TOKEN`: Your PyPI API token
   - `TEST_PYPI_TOKEN`: Your TestPyPI API token

### Publish via GitHub Release

1. Create a new tag:
   ```bash
   git tag v0.1.0
   git push origin v0.1.0
   ```

2. Create a GitHub Release:
   - Go to GitHub → Releases → Create a new release
   - Choose the tag
   - Add release notes
   - Publish release

3. GitHub Actions will automatically build and publish to PyPI

### Manual Workflow Dispatch

You can also trigger publishing manually:

1. Go to Actions → Publish to PyPI
2. Click "Run workflow"
3. Choose to publish to TestPyPI or PyPI

## Version Management

Follow [Semantic Versioning](https://semver.org/):

- **MAJOR** version (1.0.0): Breaking changes
- **MINOR** version (0.1.0): New features, backward compatible
- **PATCH** version (0.0.1): Bug fixes, backward compatible

Examples:
- `0.1.0` → `0.1.1`: Bug fix
- `0.1.0` → `0.2.0`: New feature
- `0.1.0` → `1.0.0`: Breaking change or first stable release

## Checklist Before Publishing

- [ ] Version updated in `zaban/version.py`
- [ ] CHANGELOG.md updated
- [ ] All tests passing (`pytest`)
- [ ] Type checks passing (`mypy zaban`)
- [ ] Linter passing (`ruff check zaban`)
- [ ] README.md is up to date
- [ ] Package builds successfully (`python -m build`)
- [ ] Package passes checks (`twine check dist/*`)
- [ ] Tested on TestPyPI
- [ ] Git tag created
- [ ] GitHub release created

## Troubleshooting

### "File already exists" Error

If you get a file exists error on PyPI:

1. You cannot re-upload the same version
2. Increment the version number
3. Rebuild and upload again

### Import Errors After Install

Make sure `pyproject.toml` correctly lists all packages:

```toml
[tool.setuptools]
packages = ["zaban", "zaban.types", "zaban.resources"]
```

### Missing Dependencies

Ensure all dependencies are listed in `pyproject.toml`:

```toml
dependencies = [
    "httpx>=0.27.0",
    "pydantic>=2.0.0",
    "typing-extensions>=4.7.0",
]
```

## Resources

- [Python Packaging Guide](https://packaging.python.org/)
- [PyPI Help](https://pypi.org/help/)
- [Twine Documentation](https://twine.readthedocs.io/)
- [Semantic Versioning](https://semver.org/)

