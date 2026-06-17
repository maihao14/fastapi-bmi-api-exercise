# Exercise 2: BMI Calculator API

## Objective

Create a BMI (Body Mass Index) calculator API using FastAPI.

Your API should accept height and weight as JSON, calculate BMI, and return the BMI value with a health category message.

This exercise is similar to the Streamlit BMI calculator, but instead of building a web UI, you will build an HTTP API.

## Requirements

1. Create a FastAPI app with the title `BMI Calculator API`
2. Create a request model named `BMIRequest` with:
   - `height_cm`: height in centimeters
   - `weight_kg`: weight in kilograms
3. Add validation:
   - `height_cm` should be between `50` and `250`
   - `weight_kg` should be between `10` and `300`
4. Create a response model named `BMIResponse` with:
   - `bmi`
   - `category`
   - `message`
5. Add a `GET /` route that returns a welcome message
6. Add a `GET /health` route that returns:

```json
{"status": "ok"}
```

7. Add a `POST /bmi` route that:
   - Accepts a JSON request body
   - Converts height from centimeters to meters
   - Calculates BMI with this formula:

```python
bmi = weight_kg / (height_m ** 2)
```

8. Return BMI rounded to 2 decimal places
9. Return a category based on the BMI range:

| BMI Range | Category |
| --- | --- |
| Less than 18.5 | Underweight |
| 18.5 to 24.9 | Normal weight |
| 25.0 to 29.9 | Overweight |
| 30.0 or higher | Obese |

## Starter Code

Open `main_starter.py` and complete all TODO sections.

Run the starter app:

```bash
uvicorn main_starter:app --reload
```

Run the solution app:

```bash
uvicorn main_solution:app --reload
```

Then open the interactive docs:

```text
http://127.0.0.1:8000/docs
```

## Example Request

Send this JSON body to `POST /bmi`:

```json
{
  "height_cm": 170,
  "weight_kg": 70
}
```

Expected response:

```json
{
  "bmi": 24.22,
  "category": "Normal weight",
  "message": "Your BMI is within the normal range. Keep maintaining balanced eating and regular activity."
}
```

## cURL Example

```bash
curl -X POST "http://127.0.0.1:8000/bmi" \
  -H "Content-Type: application/json" \
  -d '{"height_cm": 170, "weight_kg": 70}'
```

## Bonus Challenges

- Add imperial unit support with inches and pounds
- Add a `unit_system` field with values `metric` or `imperial`
- Return the original input values in the response
- Add a `GET /bmi/example` route that returns a sample request body
- Write a few tests using FastAPI's `TestClient`
