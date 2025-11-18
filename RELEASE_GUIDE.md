# Quick Release Guide

## 🚀 How to Publish a New Version (Automated)

### 1. Update Version
Edit `pyproject.toml`:
```toml
version = "0.1.3"  # Update this
```

### 2. Update Changelog
Add your changes to `CHANGELOG.md`

### 3. Commit & Push
```bash
git add .
git commit -m "Release v0.1.3"
git push origin main
```

### 4. Create GitHub Release
1. Go to: https://github.com/prajjwalkumarpanzade/zaban-client/releases/new
2. Click "Choose a tag" → type `v0.1.3` → "Create new tag"
3. Release title: `v0.1.3`
4. Add description (copy from CHANGELOG.md)
5. Click "**Publish release**"

### 5. ✅ Done!
GitHub Actions will automatically publish to PyPI in ~2 minutes.

---

## 📋 One-Time Setup (Do this first!)

### Add PyPI Token to GitHub:
1. Go to: https://github.com/prajjwalkumarpanzade/zaban-client/settings/secrets/actions
2. Click "New repository secret"
3. Name: `PYPI_API_TOKEN`
4. Value: Your PyPI token (the one starting with `pypi-`)
5. Click "Add secret"

---

## 🔍 Monitoring

- Check workflow status: https://github.com/prajjwalkumarpanzade/zaban-client/actions
- View on PyPI: https://pypi.org/project/zaban/

---

## 🆘 Troubleshooting

**Error: "File already exists"**
→ You forgot to increment the version in `pyproject.toml`

**Error: "Invalid credentials"**
→ Check that `PYPI_API_TOKEN` secret is set correctly in GitHub

**Workflow doesn't trigger**
→ Make sure you clicked "Publish release" (not just "Save draft")

