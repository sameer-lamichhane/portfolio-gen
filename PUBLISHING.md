# Publishing PortfolioGen to PyPI

## Prerequisites

1. **PyPI Account**: Create accounts on both:
   - [PyPI](https://pypi.org/account/register/) (production)
   - [TestPyPI](https://test.pypi.org/account/register/) (testing)

2. **API Tokens**: Generate API tokens for secure uploading:
   - Go to PyPI Account Settings → API tokens
   - Create a token for "Entire account" or specific project
   - Save the token securely

## Quick Publishing (Automated)

Run the publishing script:
```bash
python publish.py
```

This will:
- Clean previous builds
- Install dependencies
- Build the package
- Check the package
- Optionally upload to PyPI

## Manual Publishing Steps

### 1. Install Build Tools
```bash
pip install build twine
```

### 2. Clean Previous Builds
```bash
# Windows
rmdir /s /q build dist *.egg-info

# Linux/Mac
rm -rf build dist *.egg-info
```

### 3. Build the Package
```bash
python -m build
```

This creates:
- `dist/portfoliogen-1.0.0.tar.gz` (source distribution)
- `dist/portfoliogen-1.0.0-py3-none-any.whl` (wheel)

### 4. Check the Package
```bash
python -m twine check dist/*
```

### 5. Test Upload (Optional)
Upload to TestPyPI first to test:
```bash
python -m twine upload --repository testpypi dist/*
```

Test installation:
```bash
pip install --index-url https://test.pypi.org/simple/ portfoliogen
```

### 6. Upload to PyPI
```bash
python -m twine upload dist/*
```

You'll be prompted for:
- Username: `__token__`
- Password: Your API token (starts with `pypi-`)

## After Publishing

### Verify Installation
```bash
pip install portfoliogen
portfoliogen --version
portfoliogen MyTestPortfolio
```

### Update Package
For future updates:
1. Update version in `setup.py` and `pyproject.toml`
2. Update `CHANGELOG.md`
3. Rebuild and republish

## Troubleshooting

### Common Issues

1. **Package name already exists**
   - Choose a unique name
   - Check availability on PyPI first

2. **Authentication failed**
   - Verify API token is correct
   - Use `__token__` as username

3. **File already exists**
   - You can't overwrite existing versions
   - Increment version number

4. **Missing files in package**
   - Check `MANIFEST.in`
   - Verify `package_data` in setup.py

### Useful Commands

```bash
# Check what files will be included
python setup.py check
python setup.py sdist --dry-run

# Test local installation
pip install -e .

# Uninstall for testing
pip uninstall portfoliogen
```

## Security Notes

- Never commit API tokens to git
- Use environment variables for tokens
- Consider using GitHub Actions for automated publishing

## Resources

- [PyPI Publishing Guide](https://packaging.python.org/tutorials/packaging-projects/)
- [Twine Documentation](https://twine.readthedocs.io/)
- [Python Packaging Guide](https://packaging.python.org/)