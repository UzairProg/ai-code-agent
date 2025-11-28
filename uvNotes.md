# UV - Python Package Manager

## What is UV?
- **Fast Python package installer & resolver** - written in Rust
- **Drop-in replacement** for pip, pip-tools, pipx, poetry, pyenv
- **10-100x faster** than traditional Python tools

## Key Features
- ⚡ **Speed**: Rust-based, parallel downloads, cached dependencies
- 🔧 **All-in-one**: Package management + virtual environments + project management
- 🐍 **Python version management**: Install & switch Python versions
- 📦 **Lock files**: Deterministic builds with `uv.lock`
- 🔒 **Security**: Built-in vulnerability scanning

## Common Commands
```bash
# Install packages
uv add requests pandas

# Create virtual environment
uv venv

# Run scripts
uv run main.py

# Install Python version
uv python install 3.12

# Sync dependencies
uv sync
```

## UV vs Node.js Ecosystem

| Feature | UV (Python) | Node.js |
|---------|-------------|---------|
| **Package Manager** | uv | npm/yarn/pnpm |
| **Lock File** | uv.lock | package-lock.json |
| **Scripts** | uv run | npm run |
| **Environment** | uv venv | node_modules |
| **Version Manager** | uv python install | nvm |
| **Speed** | 10-100x faster | Standard |
| **Language** | Rust | JavaScript |

## Why UV > Traditional Python Tools?
- **pip**: No dependency resolution, slow
- **poetry**: Slow resolver, complex
- **conda**: Heavy, slow environment creation
- **UV**: Fast, simple, comprehensive

## Project Structure
```
my-project/
├── pyproject.toml    # Project config (like package.json)
├── uv.lock          # Lock file (like package-lock.json)
└── .python-version  # Python version (like .nvmrc)
```