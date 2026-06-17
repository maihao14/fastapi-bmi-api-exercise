from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(title="BMI Calculator API")


# TODO 1: Create a request model named BMIRequest.
# It should include:
# - height_cm: float, minimum 50, maximum 250
# - weight_kg: float, minimum 10, maximum 300
class BMIRequest(BaseModel):
    pass


# TODO 2: Create a response model named BMIResponse.
# It should include:
# - bmi: float
# - category: str
# - message: str
class BMIResponse(BaseModel):
    pass


def calculate_bmi(height_cm: float, weight_kg: float) -> float:
    # TODO 3: Convert height from centimeters to meters.
    height_m = None

    # TODO 4: Calculate BMI using weight_kg / (height_m ** 2).
    bmi = None

    return bmi


def get_bmi_category(bmi: float) -> tuple[str, str]:
    # TODO 5: Return category and message based on BMI.
    # Less than 18.5: Underweight
    # 18.5 to 24.9: Normal weight
    # 25.0 to 29.9: Overweight
    # 30.0 or higher: Obese
    pass


@app.get("/")
def read_root() -> dict[str, str]:
    # TODO 6: Return a welcome message.
    return {}


@app.get("/health")
def health_check() -> dict[str, str]:
    # TODO 7: Return {"status": "ok"}.
    return {}


@app.post("/bmi", response_model=BMIResponse)
def calculate_bmi_endpoint(request: BMIRequest) -> BMIResponse:
    # TODO 8: Calculate BMI using request.height_cm and request.weight_kg.
    bmi = None

    # TODO 9: Get category and message.
    category = None
    message = None

    # TODO 10: Return BMIResponse with BMI rounded to 2 decimal places.
    pass
