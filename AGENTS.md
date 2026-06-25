# AI Coding Agent Instructions

## Repository overview
This is a small Python learning and experimentation workspace. It contains:
- `app.py` and `MyFile.py` as simple Python scripts
- `test_primes.py` for a prime-number test or script example
- Jupyter notebooks: `JFile.ipynb`, `ListExample.ipynb`, `Dictionaries.ipynb`
- `.venv/` virtual environment for Python 3.13.9

## What to know before editing
- Use the workspace Python interpreter at `d:\GenAI\.venv\Scripts\python.exe`.
- The default terminal environment is PowerShell with `.venv` auto-activation.
- Formatting is expected to follow Black conventions.
- Pylint is enabled in the workspace and should be respected when updating Python files.

## Common tasks
- Run Python scripts directly:
  - `python MyFile.py`
  - `python app.py`
- Open notebooks with:
  - `jupyter notebook JFile.ipynb`
- Run tests if needed with `pytest test_primes.py`.

## Conventions and constraints
- This workspace does not currently include a `requirements.txt` or `pyproject.toml` file.
- Do not assume external dependencies beyond the standard library unless the user adds them.
- Keep edits small and educational; prefer clear, idiomatic Python for learning examples.

## Notes for AI agents
- The repository is primarily a learning sandbox, not a production app.
- Prioritize readability and straightforward logic over complex optimizations.
- Avoid introducing non-standard editor configuration changes unless explicitly requested.
- Use the existing `README.md` for setup and environment assumptions.
