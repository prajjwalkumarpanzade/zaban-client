# Contributing to Zaban Python Client

Thank you for your interest in contributing to the Zaban Python client! This document provides guidelines and instructions for contributing.

## Getting Started

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/zaban-python.git
cd zaban-python
```

### 2. Set Up Development Environment

```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install package in editable mode with dev dependencies
pip install -e .[dev]
```

### 3. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

## Development Workflow

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=zaban --cov-report=html

# Run specific test file
pytest tests/test_client.py

# Run specific test
pytest tests/test_client.py::test_client_initialization
```

### Type Checking

```bash
# Run type checker
mypy zaban
```

### Linting

```bash
# Check code style
ruff check zaban

# Auto-fix issues
ruff check --fix zaban
```

### Formatting

```bash
# Format code with black
black zaban tests examples
```

## Code Guidelines

### Style

- Follow [PEP 8](https://peps.python.org/pep-0008/)
- Use type hints for all functions
- Maximum line length: 100 characters
- Use descriptive variable names

### Documentation

- Add docstrings to all public functions and classes
- Use Google-style docstrings
- Include examples in docstrings when appropriate

Example:

```python
def translate(
    self,
    text: str,
    *,
    to: str,
    from_: Optional[str] = None,
) -> TranslationResponse:
    """Translate text from one language to another.
    
    Args:
        text: Text to translate
        to: Target language code (e.g., 'hin_Deva')
        from_: Source language code (optional)
        
    Returns:
        TranslationResponse with translated text
        
    Raises:
        ValidationError: If language codes are invalid
        
    Example:
        ```python
        result = client.translation.translate(
            "Hello",
            to="hin_Deva",
            from_="eng_Latn"
        )
        print(result.translated_text)
        ```
    """
```

### Testing

- Write tests for all new features
- Maintain or improve code coverage
- Use meaningful test names
- Mock external API calls

Example:

```python
def test_translation_with_auto_detect():
    """Test translation with automatic language detection."""
    client = Zaban(api_key="sk-test-key")
    
    with patch.object(client._client, "request") as mock_request:
        mock_request.return_value = {
            "translated_text": "नमस्ते",
            "source_lang": "eng_Latn",
            "target_lang": "hin_Deva",
            "model": "test",
            "auto_detected": True,
        }
        
        result = client.translation.create(
            text="Hello",
            target_lang="hin_Deva",
            auto_detect=True
        )
        
        assert result.auto_detected is True
```

## Commit Guidelines

### Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
type(scope): subject

body (optional)

footer (optional)
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `test`: Test additions or changes
- `refactor`: Code refactoring
- `style`: Code style changes (formatting)
- `chore`: Build process or auxiliary tool changes

Examples:

```bash
feat(translation): add batch translation support

fix(client): handle connection timeout errors

docs(readme): update installation instructions

test(translation): add tests for auto-detection
```

## Pull Request Process

### 1. Ensure Quality

Before submitting a PR:

- [ ] All tests pass
- [ ] Type checks pass
- [ ] Linter passes
- [ ] Code is formatted
- [ ] Documentation is updated
- [ ] CHANGELOG.md is updated (if applicable)

### 2. Create Pull Request

1. Push your branch to GitHub
2. Go to the repository and click "New Pull Request"
3. Fill in the PR template:
   - Description of changes
   - Related issues
   - Testing done
   - Screenshots (if applicable)

### 3. Code Review

- Address reviewer comments
- Keep the PR focused on a single concern
- Keep commits clean and organized

### 4. Merge

Once approved, your PR will be merged by a maintainer.

## Adding New Features

### 1. Discuss First

For major features, open an issue first to discuss:

- Use case
- Proposed API
- Implementation approach

### 2. Implementation Checklist

- [ ] Implement feature
- [ ] Add type hints
- [ ] Write docstrings
- [ ] Add tests
- [ ] Update documentation
- [ ] Add example usage
- [ ] Update CHANGELOG.md

### 3. Example Structure

```
zaban-python/
├── zaban/
│   ├── resources/
│   │   └── new_resource.py      # New resource implementation
│   └── types/
│       └── new_types.py          # Type definitions
├── tests/
│   └── test_new_resource.py      # Tests
├── examples/
│   └── new_feature_example.py    # Usage example
└── CHANGELOG.md                   # Update with changes
```

## Reporting Bugs

### Before Reporting

1. Check existing issues
2. Verify it's not a configuration issue
3. Try to reproduce with minimal example

### Bug Report Template

```markdown
**Describe the bug**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Initialize client with '...'
2. Call method '....'
3. See error

**Expected behavior**
What you expected to happen.

**Code example**
```python
from zaban import Zaban
# Minimal code to reproduce
```

**Environment**
- OS: [e.g., Ubuntu 22.04]
- Python version: [e.g., 3.11]
- Package version: [e.g., 0.1.0]

**Additional context**
Any other context about the problem.
```

## Questions?

- Open an issue with the "question" label
- Email: support@zaban.ai

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

