# GenAI Project

A Python learning and experimentation workspace for algorithm problems, data structures, and computational practices.

## Project Structure

- `JFile.ipynb` - Jupyter notebook with Python learning examples
- `MyFile.py` - Main Python script
- `app.py` - Application entry point
- `.venv/` - Python virtual environment (3.13.9)

## Contents

### Jupyter Notebook (`JFile.ipynb`)
- Basic arithmetic and type operations
- Conditional statements and leap year checker
- Calculator program
- Loop operations (for, while, range)
- String iteration
- Prime number generator (1-100)
- Break and continue statements
- Sum of powers

## Setup

### Prerequisites
- Python 3.13.9+
- Virtual environment activated

### Installation

```bash
# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Install dependencies (if any)
pip install -r requirements.txt
```

### Running

#### Run Python files:
```powershell
python MyFile.py
# or directly
MyFile.py
```

#### Run Jupyter notebook:
```bash
jupyter notebook JFile.ipynb
```

## Quick Start

From the project terminal:

```powershell
# Activate venv (already configured as default)
# Run any Python file by name
MyFile.py

# Or with explicit Python call
python MyFile.py
```

## Configuration

- **Default Terminal Profile**: PowerShell with venv auto-activation
- **Python Interpreter**: `d:\GenAI\.venv\Scripts\python.exe`
- **Editor Settings**: Black formatter, Pylint linting enabled

## Notes

- 2 is a prime number (it's the only even prime)
- Prime numbers 1-100: 25 total
- The debug breakpoint example in the notebook shows how to use `breakpoint()` in loops

## Author

sampat.bansode

## License

MIT
