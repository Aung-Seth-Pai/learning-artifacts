# Learning Artifacts

A collection of **learning notes, code examples, explainer notebooks, and mini-projects** that I maintain as active learning references. Each topic includes hands-on examples and documentation so the material is useful both for me and for anyone exploring these subjects.

## Repository Structure

| Folder | Description |
|--------|-------------|
| [**python/**](python/) | Design patterns (Decorator, Factory Method, Observer, Strategy), Python data model, and idioms & techniques. |
| [**de_toolbox/**](de_toolbox/) | Data engineering — [dbt experiments](de_toolbox/dbt_experiments/) (NYC Yellow Taxi mini-project), Airflow DAGs and fundamentals. |
| [**ml_toolbox/**](ml_toolbox/) | Machine learning — TensorFlow basics, math foundations for ML. |
| [**cv_toolbox/**](cv_toolbox/) | Computer vision — CNN/Keras models, VGG16, image processing. |
| [**da_toolbox/**](da_toolbox/) | Data analysis — exploratory notebooks (energy consumption, social media trends). |
| [**infra/**](infra/) | Infrastructure — NGINX primer with Docker Compose, reverse proxy, and SSL. |
| [**misc/**](misc/) | Miscellaneous — TFRecord experiments, chatbot prototype, prompt engineering with LangChain. |

## Quick Start with `uv`

This repo uses a single [uv](https://docs.astral.sh/uv/) environment at the root. Core dependency (`ipykernel`) is installed globally; each toolbox has its own optional dependency group to avoid collisions.

```bash
# Install the core environment (ipykernel only)
uv sync

# Install extra dependencies for a specific toolbox
uv sync --extra python                    # Python learning
uv sync --extra de_toolbox                # Data engineering (general)
uv sync --extra de_toolbox_dbt_experiments  # dbt + DuckDB
uv sync --extra ml_toolbox                # ML utilities
uv sync --extra ml_toolbox_tensorflow     # TensorFlow / Keras
uv sync --extra cv_toolbox                # Computer vision
uv sync --extra da_toolbox                # Data analysis
```

Launch notebooks from any folder:
```bash
uv run jupyter lab
```