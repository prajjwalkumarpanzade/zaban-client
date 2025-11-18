# GitHub Actions Setup Guide

This repository uses GitHub Actions to automate testing and publishing to PyPI.

## Workflows

### 1. Test Workflow (`test.yml`)
- **Triggers:** On push to `main` or on pull requests
- **Purpose:** Runs tests, linters, and type checking across Python 3.8-3.12
- **No setup required** - works automatically

### 2. Publish to PyPI Workflow (`publish-to-pypi.yml`)
- **Triggers:** When a new GitHub Release is published OR manually triggered
- **Purpose:** Automatically builds and publishes package to PyPI
- **Requires:** PyPI API token setup (see below)

## Setting Up PyPI Publishing

### Step 1: Add PyPI API Token to GitHub Secrets

1. Go to your GitHub repository
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Name: `PYPI_API_TOKEN`
5. Value: Your PyPI API token (starts with `pypi-`)
6. Click **Add secret**

### Step 2: Create a PyPI API Token

If you don't have a token yet:

1. Go to https://pypi.org/manage/account/token/
2. Click **Add API token**
3. Name it (e.g., "GitHub Actions - zaban")
4. Scope: Choose either:
   - **Entire account** (for first-time setup)
   - **Specific project: zaban** (more secure, after first publish)
5. Copy the token immediately (you won't see it again!)
6. Add it to GitHub Secrets (see Step 1)

## Publishing a New Version

### Automated Publishing (Recommended)

1. **Update version** in `pyproject.toml`:
   ```toml
   version = "0.1.2"  # Increment version
   ```

2. **Update** `CHANGELOG.md` with changes

3. **Commit and push**:
   ```bash
   git add .
   git commit -m "Release v0.1.2"
   git push origin main
   ```

4. **Create a GitHub Release**:
   - Go to your repo → **Releases** → **Create a new release**
   - Click **Choose a tag** → type `v0.1.2` → **Create new tag**
   - Release title: `v0.1.2` or `Release 0.1.2`
   - Add release notes (copy from CHANGELOG.md)
   - Click **Publish release**

5. **Done!** The workflow will automatically:
   - Build the package
   - Run checks
   - Publish to PyPI

### Manual Publishing (Alternative)

You can also trigger the workflow manually:

1. Go to **Actions** tab in your repo
2. Select **Publish to PyPI** workflow
3. Click **Run workflow**
4. Choose the branch
5. Click **Run workflow**

## Monitoring

- Check the **Actions** tab to see workflow runs
- If publishing fails, check the workflow logs for errors
- Most common issue: version already exists on PyPI (remember to increment version!)

## Version Numbering

Follow [Semantic Versioning](https://semver.org/):
- **Major** (1.0.0): Breaking changes
- **Minor** (0.1.0): New features, backwards compatible
- **Patch** (0.1.1): Bug fixes, backwards compatible

## Security Notes

- ⚠️ **Never commit** your PyPI token to git
- ✅ **Always use** GitHub Secrets for tokens
- 🔒 Consider using **project-scoped tokens** instead of account-wide tokens
- 🔄 **Rotate tokens** periodically for better security

