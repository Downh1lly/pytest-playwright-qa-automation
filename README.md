# pytest-restful-booker

Pytest project for testing the Restful Booker API and booking form UI.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install
```

## Run tests

```powershell
pytest
pytest -m api
pytest -m ui
```

The API client is in `api/`, and browser page objects are in `pages/`.
