# Playground Python FastAPI
Playground project for Python and FastAPI

## Getting Started

### Prerequisites
* uv 0.9+ (https://docs.astral.sh/uv/) An extremely fast Python package and project manager
* Python 3.14+ (optional, as uv will source this for you if it's not available)

### Development Commands

FastAPI server in dev mode (http://127.0.0.1:8000) with docs (http://127.0.0.1:8000/docs)
```bash
uv run fastapi dev
```

Running the pytest tests
```bash
uv run pytest tests -v
```
