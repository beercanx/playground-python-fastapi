# Playground Python FastAPI
Playground project for Python and FastAPI  

[![python](https://github.com/beercanx/playground-python-fastapi/actions/workflows/python.yml/badge.svg)](https://github.com/beercanx/playground-python-fastapi/actions/workflows/python.yml) 
[![CodeQL](https://github.com/beercanx/playground-python-fastapi/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/beercanx/playground-python-fastapi/actions/workflows/github-code-scanning/codeql) 
[![Dependabot Updates](https://github.com/beercanx/playground-python-fastapi/actions/workflows/dependabot/dependabot-updates/badge.svg)](https://github.com/beercanx/playground-python-fastapi/actions/workflows/dependabot/dependabot-updates)

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

## Reading materials
List of most of the content/blogs/projects that inspired/influenced this setup
* https://github.com/stejackson94/DogAsAService
* https://docs.astral.sh/uv/guides/integration/fastapi
* https://docs.astral.sh/uv/guides/integration/github
* https://docs.astral.sh/uv/guides/integration/dependency-bots/#dependabot
* https://azzamjiul.medium.com/introduction-to-integration-testing-in-fastapi-773fe8567337
