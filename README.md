## CodeShade

**CodeShade** is a Python tool to obfuscate your scripts for security and privacy. It can transform Python code into **Base64** or **emoji-based representations** and obfuscate Bash scripts using `bash-obfuscate`.

## Features

- Obfuscate **Python scripts** to Base64 variables.

- Obfuscate **Python scripts** to emoji sequences.

- Obfuscate **Bash scripts** using bash-obfuscate.

- Interactive menu for easy use in the terminal.

- Command-line support for automated workflows.

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/s-r-e-e-r-a-j/CodeShade.git
```
2. **Navigate to the CodeShade directory:**
```bash
cd CodeShade
```
3. **Make sure `Node.js` and `npm` are installed for Bash obfuscation:**
```bash
npm install -g bash-obfuscate
```

## Usage
**Interactive Mode**

Run CodeShade interactively:
```bash
python -m codeshade --interactive
```

You can choose options like:
```bash
1) Python → base64

2) Python → emoji

3) Bash obfuscate

0) Exit
```

When the tool asks for `src:` and `dst:`

- `src:` = type the path to the original file you want to obfuscate (for example `hello.py` or `script.sh`).

- `dst:` = type the path where the obfuscated file should be saved (for example `hello_b64.py` or `out.sh`).
