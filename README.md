# Learning‑Artifacts Repository

A collection of **learning notes, code examples, and explainer notebooks** covering several topics:

- **Python** – design patterns, data models, programming techniques.
- **Computer Vision Toolbox** – image processing, CNN examples.
- **Data‑Analysis Toolbox** – Jupyter notebooks for data exploration.
- **Machine‑Learning Toolbox** – MLOps, Airflow, TensorFlow/Keras demos.
- **Misc** – assorted experiments.

## Quick Start with `uv`
```bash
# Install the core environment (only ipykernel)
uv sync

# Install extra dependencies for a specific toolbox, e.g.:
uv sync --extra python           # Python learning extras (currently empty)
uv sync --extra ml_toolbox       # Generic ML utilities
uv sync --extra ml_toolbox_airflow
uv sync --extra ml_toolbox_tensorflow
uv sync --extra cv_toolbox
uv sync --extra da_toolbox
```

Launch notebooks (any folder) with:
```bash
uv run jupyter lab
```

## Navigation
- [Python folder](python/)
- [Computer Vision toolbox](cv_toolbox/)
- [Data‑Analysis toolbox](da_toolbox/)
- [Machine‑Learning toolbox](ml_toolbox/)
- [Miscellaneous](misc/)