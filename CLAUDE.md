# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`gi` is a command-line tool that generates `.gitignore` files by fetching templates from the [Toptal gitignore API](https://www.toptal.com/developers/gitignore/api/).

## Development Setup

```bash
# 建立並啟動虛擬環境
python3.13 -m venv venv
source venv/bin/activate

# 安裝依賴
pip install requests pyinstaller
```

## Running the Tool

```bash
# Directly with Python
python gi.py python,macos

# Using the compiled binary
./dist/gi/gi python,macos
```

## Building the Binary

```bash
pyinstaller gi.spec
```

Output binary: `dist/gi/gi` (macOS arm64, ~1.4MB)

## Architecture

Single-file application (`gi.py`):
1. Reads comma-separated keywords from `sys.argv[1]`
2. Fetches `https://www.toptal.com/developers/gitignore/api/{keywords}`
3. Writes the response to `.gitignore` in the current directory

Runtime dependency: `requests` only. `gi.spec` configures PyInstaller with `COLLECT` mode (folder output, not single-file).
