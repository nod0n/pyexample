# PyExample - Example Data Science Project with Python (no tools like uv/poetry/conda)

Minimal example Python project demonstrating a sane structure (`src/` layout), loose dependency pinning in `pyproject.toml`, and reproducible installs via a separate `requirements.txt` — without mandating a specific tool like Poetry or uv. This is a starting point, using uv/poetry/*conda is recommended for more advanced use cases.

## Project Layout

```
pyexample/
├── .gitignore                      # Git ignore file (excludes .venv/, __pycache__/, *.pyc, .egg-info/, etc.)
├── .venv/                          # Virtual environment (ignored)
├── pyproject.toml
├── requirements.txt                # Frozen snapshot (reproducible installs)
├── README.md
├── LICENSE
├── references.bib
├── data/                           # Data assets
├── src/
│   ├── pyexample/                  # Main Python package
│   │   ├── __init__.py
│   │   ├── __pycache__/            # Python bytecode cache (ignored)
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__/        # (ignored)
│   │   │   └── baseline.py
│   │   └── utils/
│   │       ├── __init__.py
│   │       ├── __pycache__/        # (ignored)
│   │       └── data.py
│   ├── pyexample.egg-info/         # Build metadata from pip install -e . (ignored)
│   ├── externalcode1/              # Vendored external code (importable package)
│   └── externalcode2/              # Vendored external code (importable package)
├── scripts/
│   └── best_model_inference.py     # Runnable script (not importable as a package)
├── tests/
│   ├── __init__.py
│   ├── test_baseline.py            # Smoke tests for models
│   └── test_data.py                # Smoke tests for utils
└── notebooks/
	├── eda.qmd                     # Quarto notebook (source)
	├── eda.html                    # Rendered HTML
	├── eda.pdf                     # Rendered PDF
	└── eda.ipynb                   # Jupyter notebook (optional)
```

Note: Only code under `src/` is importable as packages/modules. Scripts and notebooks are not importable. Items marked "(ignored)" are generated during development and excluded via `.gitignore`.

Note: Committing `*.qmd` files is preferred over `*.ipynb` for easier diffs and reviews, but feel free to use Jupyter if desired and ignore that quarto exists. See Notebooks section below for details.

## Development Setup (Editable)

If you want to contribute or run scripts/notebooks:

```bash
python -m venv .venv
source .venv/bin/activate           # macOS/Linux
pip install --upgrade pip
pip install -r requirements.txt     # install exact dependencies
pip install -e .                    # install package editable
```

### Depenceny changes

Add dependencys to `pyproject.toml` with loose ranges, e.g.:

```toml
dependencies = [
    "pandas>=2.0",
]
```

From your current environment snapshot:

```bash
pip install -e .
pip freeze > requirements.txt
```

Others can then install exact versions via:

```bash
pip install -r requirements.txt
```

## Why Loose Pins in `pyproject.toml`?

- Avoid blocking users who already depend on newer compatible versions.
- Let dependency resolvers choose best matching versions in broader environments.
- Separate portability (specification) from reproducibility (freeze file).

Typical pattern inside `pyproject.toml`:

```toml
[project]
requires-python = ">=3.12"
dependencies = [
	"pandas>=2.0",
	"jupyter>=1.0",
	"pytest>=9.0",  # included here for simplicity; no separate dev extras
]
```

## Vendored Code (external folders in `src/`)

If you need to copy code from another repository and modify it, add it under `src/` as its own package/folder. Example:

```
src/
	pyexample/
		...
	external_libname/
		__init__.py
		module.py
```

Import it explicitly where needed, e.g. `from external_libname import module`. Do always import modules not specific classes/functions to avoid name collisions.

## Running Scripts

After activating the virtual environment and installing editable:

```bash
python scripts/best_model_inference.py
```

## Notebooks

Notebook-like Quarto files (`*.qmd`) files live under `notebooks/`. After activating the virtual environment and installing editable, render to HTML/PDF:

```bash
quarto render notebooks/eda.qmd
```

Benefits of `.qmd`: lighter diffs, easier reviews compared to raw `.ipynb`.

### Convert `*.qmd` to `*.ipynb` and Vice Versa

To convert between Quarto `.qmd` files and Jupyter `.ipynb` notebooks, you can use the following commands:

```bash
# Convert .qmd to .ipynb
quarto convert notebooks/eda.qmd
# Convert .ipynb to .qmd
quarto convert notebooks/eda.ipynb
```

## Testing

Run tests (if added) via:

```bash
pytest -q
```
