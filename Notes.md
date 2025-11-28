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

# SYS - System Information Tool

## What is SYS?
- **Built-in Python module** - access system-level information
- **Python's "system toolkit"** - runtime, paths, environment details
- **No installation needed** - comes with Python

## What It Provides
- 🖥️ **System info**: Platform, version, paths
- 🐍 **Python runtime**: Interpreter details, memory
- 📋 **Command-line arguments**: Access script arguments
- 📂 **Paths**: Module search paths, executable location
- 🌐 **Environment**: Standard I/O, exit codes

## sys.argv - Command Line Arguments

**What is it?**
- **List of command-line arguments** passed to your script
- `sys.argv[0]` = script name
- `sys.argv[1:]` = actual arguments

**Example:**
```python
# script.py
import sys

print(f"Script name: {sys.argv[0]}")
print(f"Arguments: {sys.argv[1:]}")
```

```bash
# Running: python script.py hello world 123
# Output:
# Script name: script.py
# Arguments: ['hello', 'world', '123']
```

**Common Use Cases:**
```python
import sys

# Get filename from command line
filename = sys.argv[1]

# Check argument count
if len(sys.argv) < 2:
    print("Usage: python script.py <filename>")
    sys.exit(1)

# Parse multiple arguments
name = sys.argv[1]
age = int(sys.argv[2])
```

## Common sys Functions

```python
import sys

# Exit program
sys.exit(0)  # Success
sys.exit(1)  # Error

# Python version
sys.version      # '3.12.0 ...'
sys.version_info # (3, 12, 0, ...)

# Platform info
sys.platform  # 'win32', 'linux', 'darwin'

# Module paths
sys.path  # List of directories Python searches

# Standard streams
sys.stdin   # Input
sys.stdout  # Output
sys.stderr  # Errors
```

## sys vs os Module

| sys | os |
|-----|-----|
| Python runtime info | Operating system operations |
| Command-line args | File/directory operations |
| Exit program | Environment variables |
| Python paths | Process management |
| stdin/stdout/stderr | Path manipulation |

# --verbose

**--verbose** = “give me more details while running”

When you run a command with --verbose, the program prints extra information about what it’s doing, step by step, instead of just showing success/failure.