# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`gi` is a command-line tool that generates `.gitignore` files by fetching templates from the [Toptal gitignore API](https://www.toptal.com/developers/gitignore/api/).

## Development Setup

```bash
# Activate virtual environment (Python 3.13)
source venv/bin/activate

# Install dependencies
pip install requests
```

## Running the Tool

```bash
# Directly with Python
python gi.py python,java

# Using the compiled binary
./dist/gi/gi python,java
```

The tool writes `.gitignore` to the current working directory.

## Building the Binary

```bash
# Activate venv first, then build with PyInstaller
source venv/bin/activate
pyinstaller gi.spec
```

Output binary: `dist/gi/gi` (macOS arm64, ~1.4MB)

## Architecture

Single-file application (`gi.py`):
1. Reads comma-separated keywords from `sys.argv[1]`
2. Fetches `https://www.toptal.com/developers/gitignore/api/{keywords}`
3. Writes the response to `.gitignore` in the current directory

Runtime dependency: `requests` only. `gi.spec` configures PyInstaller with `COLLECT` mode (folder output, not single-file).
