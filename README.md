# FastAPI Exercise 1: BMI Calculator API

This exercise helps students build a small FastAPI app that calculates BMI from a JSON request body.

It pairs naturally with the Streamlit BMI calculator exercise:

- Streamlit version: user enters values in a web UI
- FastAPI version: client sends values to an HTTP API

## Learning Goals

- Create a FastAPI app
- Define Pydantic request and response models
- Use field validation with `Field`
- Create `GET` and `POST` routes
- Return JSON responses
- Test an API using Swagger docs or `curl`

## Files

- `exercise.md`: student-facing exercise instructions
- `main_starter.py`: TODO starter code for students
- `main_solution.py`: complete reference solution
- `teaching_notes.md`: instructor flow and common errors
- `requirements.txt`: runtime dependency list

## Setup

Create and activate a virtual environment before installing dependencies.

### macOS or Linux

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run The Starter

```bash
uvicorn main_starter:app --reload
```

## Run The Solution

```bash
uvicorn main_solution:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

## Expected BMI Categories

| BMI Range | Category |
| --- | --- |
| `< 18.5` | Underweight |
| `18.5 - 24.9` | Normal weight |
| `25.0 - 29.9` | Overweight |
| `>= 30.0` | Obese |
