# GitHub Actions Workflows

This repository includes automated workflows for testing, building, and publishing the portfoliogen package.

## 🔄 Available Workflows

### 1. **Test Package** (`test.yml`)
- **Triggers**: Push to main/develop, Pull requests
- **Purpose**: Test package on multiple OS and Python versions
- **Matrix**: Ubuntu/Windows/macOS × Python 3.7-3.12
- **Tests**: CLI functionality, portfolio generation, Python API

### 2. **Publish to PyPI** (`publish.yml`)
- **Triggers**: 
  - Release published (automatic)
  - Manual dispatch (with Test PyPI option)
- **Purpose**: Build and publish package to PyPI/Test PyPI
- **Requirements**: API tokens in repository secrets

### 3. **Create Release** (`release.yml`)
- **Triggers**: Git tags starting with 'v' (e.g., v1.0.1)
- **Purpose**: Create GitHub releases with built packages
- **Automatic**: Creates release notes and uploads assets

## 🔧 Setup Instructions

### 1. Repository Secrets
Add these secrets in GitHub repository settings:

```
PYPI_API_TOKEN          # Your PyPI API token
TEST_PYPI_API_TOKEN     # Your Test PyPI API token (optional)
```

### 2. API Token Setup
1. Go to [PyPI Account Settings](https://pypi.org/manage/account/)
2. Create API token for "Entire account" or specific project
3. Copy token (starts with `pypi-`)
4. Add to GitHub repository secrets

### 3. Test PyPI (Optional)
1. Create account on [Test PyPI](https://test.pypi.org/)
2. Generate API token
3. Add `TEST_PYPI_API_TOKEN` secret

## 🚀 Usage

### Automatic Publishing
1. **Create a tag**: `git tag v1.0.1 && git push origin v1.0.1`
2. **Release workflow** creates GitHub release
3. **Publish workflow** automatically publishes to PyPI

### Manual Publishing
1. Go to Actions → "Publish to PyPI"
2. Click "Run workflow"
3. Choose Test PyPI or PyPI
4. Click "Run workflow"

### Testing
- **Automatic**: Runs on every push/PR
- **Manual**: Go to Actions → "Test Package" → "Run workflow"

## 📋 Workflow Details

### Test Matrix
```yaml
os: [ubuntu-latest, windows-latest, macos-latest]
python-version: ['3.7', '3.8', '3.9', '3.10', '3.11', '3.12']
```

### Build Artifacts
- Source distribution (`.tar.gz`)
- Wheel distribution (`.whl`)
- Uploaded to GitHub Actions artifacts
- Attached to GitHub releases

### Security
- Uses GitHub's built-in `GITHUB_TOKEN`
- API tokens stored as encrypted secrets
- No sensitive data in workflow files

## 🔍 Monitoring

### Check Workflow Status
- Go to repository → Actions tab
- View workflow runs and logs
- Download build artifacts

### Troubleshooting
- Check workflow logs for errors
- Verify API tokens are correct
- Ensure package builds locally first

## 📝 Version Management

### Semantic Versioning
Use semantic versioning for tags:
- `v1.0.0` - Major release
- `v1.0.1` - Patch release  
- `v1.1.0` - Minor release

### Update Version
1. Update version in `setup.py` and `pyproject.toml`
2. Commit changes
3. Create and push tag: `git tag v1.0.1 && git push origin v1.0.1`
4. Workflows automatically trigger

## 🎯 Best Practices

1. **Test locally** before pushing
2. **Use Test PyPI** for testing releases
3. **Create meaningful** commit messages
4. **Update documentation** with new features
5. **Follow semantic versioning**

## 📚 Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [PyPI Publishing Guide](https://packaging.python.org/tutorials/packaging-projects/)
- [Semantic Versioning](https://semver.org/)