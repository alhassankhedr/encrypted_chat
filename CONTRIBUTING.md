# Contributing to OpenWebUI + Lorica.ai Integration

Thank you for your interest in contributing to this project! This document provides guidelines for contributing to the OpenWebUI + Lorica.ai integration.

## 🚀 Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally
3. Create a new branch for your feature or bugfix
4. Make your changes
5. Test your changes thoroughly
6. Submit a pull request

## 📋 Development Setup

1. **Prerequisites**
   - Python 3.12+
   - Git

2. **Setup Development Environment**
   ```bash
   git clone https://github.com/yourusername/openwebui-lorica.git
   cd openwebui-lorica
   python3.12 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Test Your Changes**
   - Ensure the pipe works correctly with OpenWebUI
   - Test both streaming and non-streaming responses
   - Verify error handling works properly

## 🔧 Code Guidelines

### Python Code Style
- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Add docstrings for all functions and classes
- Keep functions focused and single-purpose

### Security Considerations
- Never log sensitive data (API keys, user prompts, etc.)
- Ensure all error messages are safe and don't leak information
- Follow the principle of least privilege

### Documentation
- Update README.md if you add new features
- Add comments for complex logic
- Keep the security documentation accurate

## 🐛 Reporting Issues

When reporting issues, please include:

1. **Environment Information**
   - Python version
   - Operating system
   - OpenWebUI version
   - Lorica SDK version

2. **Steps to Reproduce**
   - Clear, numbered steps
   - Expected vs actual behavior

3. **Error Messages**
   - Full error traceback (if applicable)
   - Any relevant log messages

4. **Additional Context**
   - Screenshots (if helpful)
   - Configuration details (without sensitive data)

## 🔀 Pull Request Process

1. **Before Submitting**
   - Ensure your code follows the style guidelines
   - Test your changes thoroughly
   - Update documentation if needed

2. **Pull Request Description**
   - Clear title describing the change
   - Detailed description of what was changed and why
   - Reference any related issues

3. **Review Process**
   - All PRs require review before merging
   - Address feedback promptly
   - Keep PRs focused and reasonably sized

## 🏷️ Commit Messages

Use clear, descriptive commit messages:

```
feat: add support for custom headers
fix: resolve streaming response handling
docs: update installation instructions
refactor: improve error handling
```

## 📝 License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

## 🤝 Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow
- Follow the golden rule

## 🆘 Getting Help

- Check existing issues and discussions
- Ask questions in GitHub Discussions
- Review the documentation
- Contact maintainers if needed

Thank you for contributing! 🎉

