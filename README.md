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

- If you choose **Python → Base64**, after entering `src:` and `dst:`, the tool will also ask for `var (payload):`.
This is the variable name that will store the Base64-encoded data in the obfuscated Python script.
You can press Enter to use the default name `payload`.

- If you choose `Bash obfuscate`, after entering `src:` and `dst:` the tool will ask `auto install? (y/N):`. If you type `y` the tool will try to install `bash-obfuscate` using `npm` (this may require Node.js/npm). press **Enter** or type `n` to skip automatic installation.

## Command-Line Mode

- **Obfuscate Python to Base64:**
```bash
python -m codeshade py-base64 src.py dst.py --var payload
```

- **Obfuscate Python to Emoji:**
```bash
python -m codeshade py-emoji src.py dst.py
```
- **Obfuscate Bash script:**

```bash
python -m codeshade bash-obf script.sh output.sh --auto-install
```
