# cntdrun

[![PyPI - Version](https://img.shields.io/pypi/v/cntdrun)](https://pypi.org/project/cntdrun/)
[![Python](https://img.shields.io/badge/python-3.9+-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](./LICENSE)

A countdown timer GUI that executes a shell command when time runs out. Built with PySide6.

![](https://img.shields.io/badge/GUI-PySide6-green)

## Features

- ⏱️ Configurable countdown timer with visual display
- 🖥️ Frameless, always-on-top floating window — drag to reposition
- ⌨️ Press `Enter` to close early
- 🎨 Customizable fonts, sizes, colors, and window geometry
- 🚀 Executes any shell command on completion

## Requirements

- **Python** ≥ 3.9
- Display server (X11 / Wayland / Windows GUI)

## Installation

### uv tool install (recommended)

```bash
uv tool install cntdrun
```

Installs `cntdrun` as a globally available CLI tool managed by uv.

### pip

```bash
pip install cntdrun
```

### From source

```bash
git clone https://github.com/gzj/cntdrun.git
cd cntdrun
uv sync
uv run cntdrun --version
```

## Usage

`cntdrun` can be invoked in several ways depending on how you installed it:

### After `uv tool install` (global)

```bash
cntdrun 3 "echo 'Time is up!'"
```

### During development (from source)

```bash
# Direct entry point
uv run cntdrun 3 "echo 'Time is up!'"

# As Python module
uv run python -m cntdrun 3 "echo 'Time is up!'"

# Show help / version
uv run cntdrun --help
uv run cntdrun --version
```

### After `pip install`

```bash
cntdrun 3 "echo 'Time is up!'"
```

| Argument | Description |
|----------|-------------|
| `count` | Countdown duration in seconds |
| `command` | Shell command to run after countdown |

### Options

| Option | Default | Description |
|--------|---------|-------------|
| `--command-label` | *(command text)* | Custom label above the countdown |
| `--window-width` | `250` | Window width in pixels |
| `--window-height` | `150` | Window height in pixels |
| `--window-x` | *(centered)* | X position on screen |
| `--window-y` | *(centered)* | Y position on screen |
| `--label-font` | `Arial` | Font for the countdown number |
| `--label-size` | `32` | Font size for the countdown number |
| `--button-text` | `close` | Text on the close button |
| `--button-font` | `Arial` | Font for the close button |
| `--button-size` | `10` | Font size for the close button |
| `--version` | | Show version and exit |

### Examples

```bash
# Simple 3-second countdown
cntdrun 3 "echo 'Time is up!'"

# Shutdown after 10 seconds
cntdrun 10 "shutdown /s /t 0"

# Custom appearance and position
cntdrun 5 "notify-send Done" \
    --label-font "Cascadia Code" \
    --label-size 48 \
    --button-text "Cancel" \
    --button-font "Segoe UI" \
    --button-size 12 \
    --window-x 100 \
    --window-y 200 \
    --window-width 300 \
    --window-height 180 \
    --command-label "Shutting down..."
```

## Development

```bash
git clone https://github.com/gzj/cntdrun.git
cd cntdrun
uv sync
uv run cntdrun --version
```

## License

MIT
