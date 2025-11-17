# Quick Start Guide - Zaban Python Package

This guide will help you get started with the Zaban Python client package.

## 📦 Package Overview

The **Zaban Python client** is a production-ready PyPI package that provides an OpenAI-style interface to the Zaban API for Indian language services:

- ✅ **Translation** (22 Indian languages via IndicTrans2)
- ✅ **Text-to-Speech (TTS)**
- ✅ **Speech-to-Text (STT)**
- ✅ **Transliteration**
- ✅ **Sync & Async support**
- ✅ **Type hints with Pydantic**
- ✅ **Comprehensive error handling**

## 🚀 Installation (For Users)

Once published to PyPI, users can install with:

```bash
pip install zaban
```

## 🛠️ Development Setup

### 1. Navigate to Package Directory

```bash
cd C:\Users\JSPNLP\Desktop\zaban\zaban-python
```

### 2. Install in Development Mode

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Install in editable mode
pip install -e .

# Or with dev dependencies
pip install -e .[dev]
```

### 3. Test the Package

```python
# test_local.py
from zaban import Zaban

# Initialize (requires running Zaban backend)
client = Zaban(
    api_key="sk-your-api-key",
    base_url="http://localhost:8000/api/v1"
)

# Test translation
result = client.translation.create(
    text="Hello, world!",
    source_lang="eng_Latn",
    target_lang="hin_Deva"
)
print(result.translated_text)
```

## 📝 Basic Usage Examples

### Example 1: Simple Translation

```python
from zaban import Zaban

client = Zaban(api_key="sk-your-api-key")

# English to Hindi
result = client.translation.create(
    text="Hello, how are you?",
    source_lang="eng_Latn",
    target_lang="hin_Deva"
)
print(result.translated_text)  # Output: आप कैसे हैं?
```

### Example 2: Auto-Detection

```python
# Let the API detect source language
result = client.translation.create(
    text="Good morning",
    target_lang="tam_Taml",
    auto_detect=True
)
print(f"Detected: {result.source_lang}")
print(f"Translation: {result.translated_text}")
```

### Example 3: Async Batch Translation

```python
import asyncio
from zaban import AsyncZaban

async def batch_translate():
    async with AsyncZaban(api_key="sk-your-api-key") as client:
        texts = ["Hello", "Goodbye", "Thank you"]
        
        tasks = [
            client.translation.create(text=t, target_lang="hin_Deva", auto_detect=True)
            for t in texts
        ]
        
        results = await asyncio.gather(*tasks)
        
        for text, result in zip(texts, results):
            print(f"{text} -> {result.translated_text}")

asyncio.run(batch_translate())
```

### Example 4: Text-to-Speech

```python
# Generate speech
audio = client.audio.speech.create(
    text="नमस्ते दुनिया",
    lang="hi",
    speaker="female"
)

# Save to file
audio.save("output.wav")
```

### Example 5: Transliteration

```python
result = client.transliteration.create(
    text="namaste",
    source_script="latn",
    target_script="deva",
    lang="hi"
)
print(result.top)  # Output: नमस्ते
```

## 🧪 Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=zaban

# Run specific test file
pytest tests/test_client.py

# Run with verbose output
pytest -v
```

## 🏗️ Building the Package

### 1. Install Build Tools

```bash
pip install build twine
```

### 2. Build Distribution

```bash
# Clean previous builds
rm -rf dist/ build/ *.egg-info

# Build package
python -m build
```

This creates:
- `dist/zaban-0.1.0.tar.gz` (source)
- `dist/zaban-0.1.0-py3-none-any.whl` (wheel)

### 3. Check Package

```bash
twine check dist/*
```

## 📤 Publishing to PyPI

### Test on TestPyPI First

```bash
# Upload to TestPyPI
twine upload --repository testpypi dist/*

# Test installation
pip install --index-url https://test.pypi.org/simple/ zaban
```

### Publish to PyPI

```bash
# Upload to real PyPI (requires API token)
twine upload dist/*
```

See [PUBLISHING.md](PUBLISHING.md) for detailed publishing instructions.

## 🔑 API Key Setup

### For Development (Localhost)

1. Start your Zaban backend:
   ```bash
   cd C:\Users\JSPNLP\Desktop\zaban\zaban\zaban_backend
   uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

2. Get a JWT token and create an API key (see backend README)

3. Use the API key:
   ```python
   client = Zaban(
       api_key="sk-your-api-key",
       base_url="http://localhost:8000/api/v1"
   )
   ```

### For Production

```python
# Set environment variable
export ZABAN_API_KEY="sk-your-api-key"

# Client auto-loads from environment
client = Zaban()
```

## 📁 Package Structure

```
zaban-python/
├── zaban/                      # Main package
│   ├── __init__.py            # Package exports
│   ├── client.py              # Zaban & AsyncZaban clients
│   ├── _client.py             # Base HTTP client
│   ├── _exceptions.py         # Error classes
│   ├── _utils.py              # Utilities
│   ├── version.py             # Version info
│   ├── types/                 # Type definitions
│   │   ├── __init__.py
│   │   ├── common.py
│   │   ├── translation.py
│   │   ├── tts.py
│   │   ├── stt.py
│   │   └── transliteration.py
│   └── resources/             # API resources
│       ├── __init__.py
│       ├── translation.py
│       ├── audio.py
│       └── transliteration.py
├── tests/                      # Test suite
│   ├── test_client.py
│   ├── test_translation.py
│   ├── test_types.py
│   ├── test_exceptions.py
│   └── test_utils.py
├── examples/                   # Example scripts
│   ├── basic_usage.py
│   ├── async_usage.py
│   └── batch_translation.py
├── .github/workflows/          # CI/CD
│   ├── test.yml
│   └── publish.yml
├── pyproject.toml             # Package configuration
├── README.md                  # Main documentation
├── LICENSE                    # MIT License
├── CHANGELOG.md              # Version history
├── PUBLISHING.md             # Publishing guide
└── CONTRIBUTING.md           # Contribution guide
```

## 🎯 Next Steps

### 1. Test Locally

```bash
cd C:\Users\JSPNLP\Desktop\zaban\zaban-python

# Install in dev mode
pip install -e .[dev]

# Run tests
pytest

# Try examples
python examples/basic_usage.py
```

### 2. Customize (Optional)

- Update package name in `pyproject.toml`
- Update author info
- Update GitHub URLs
- Customize README

### 3. Publish

Follow [PUBLISHING.md](PUBLISHING.md) for step-by-step publishing instructions.

## 🌟 Features Comparison with OpenAI Client

| Feature | OpenAI | Zaban |
|---------|--------|-------|
| **Style** | `client.chat.completions.create()` | `client.translation.create()` |
| **Sync/Async** | ✅ Both | ✅ Both |
| **Type Hints** | ✅ Yes | ✅ Yes |
| **Context Manager** | ✅ Yes | ✅ Yes |
| **Error Handling** | ✅ Comprehensive | ✅ Comprehensive |
| **Resources** | Chat, Completions, Embeddings | Translation, Audio, Transliteration |
| **Languages** | English-centric | 22 Indian languages |

## 📚 Additional Resources

- **Backend API**: `C:\Users\JSPNLP\Desktop\zaban\zaban\zaban_backend\`
- **API Reference**: Backend `API_QUICK_REFERENCE.md`
- **Examples**: `examples/` directory
- **Tests**: `tests/` directory

## 💡 Tips

1. **Development**: Use `pip install -e .` for live code changes
2. **Testing**: Run tests before publishing
3. **Version**: Increment version in `zaban/version.py` before each release
4. **Environment**: Use `.env` or environment variables for API keys
5. **Documentation**: Keep README and examples up to date

## 🐛 Troubleshooting

### Import Error

```python
# If you get "ModuleNotFoundError: No module named 'zaban'"
pip install -e .
```

### API Connection Error

```python
# Make sure backend is running
# Check base_url is correct
client = Zaban(
    api_key="sk-test",
    base_url="http://localhost:8000/api/v1"  # Verify this URL
)
```

### Type Errors

```bash
# Install type stubs if needed
pip install types-requests
```

## 📞 Support

- **Issues**: Open an issue on GitHub
- **Email**: support@zaban.ai
- **Documentation**: See README.md and other .md files

---

**Congratulations! 🎉** You now have a production-ready Python package for Zaban API!

