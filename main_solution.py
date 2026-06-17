from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(
    title="BMI Calculator API",
    description="A beginner-friendly FastAPI app that calculates BMI from height and weight.",
    version="1.0.0",
)


class BMIRequest(BaseModel):
    height_cm: float = Field(
        ...,
        ge=50,
        le=250,
        description="Height in centimeters.",
        examples=[170],
    )
    weight_kg: float = Field(
        ...,
        ge=10,
        le=300,
        description="Weight in kilograms.",
        examples=[70],
    )


class BMIResponse(BaseModel):
    bmi: float
    category: Literal["Underweight", "Normal weight", "Overweight", "Obese"]
    message: str


def calculate_bmi(height_cm: float, weight_kg: float) -> float:
    height_m = height_cm / 100
    return weight_kg / (height_m**2)


def get_bmi_category(bmi: float) -> tuple[str, str]:
    if bmi < 18.5:
        return (
            "Underweight",
            "Your BMI is below the normal range. Consider discussing nutrition goals with a healthcare professional.",
        )
    if bmi < 25:
        return (
            "Normal weight",
            "Your BMI is within the normal range. Keep maintaining balanced eating and regular activity.",
        )
    if bmi < 30:
        return (
            "Overweight",
            "Your BMI is above the normal range. Small changes in diet and activity can help improve long-term health.",
        )
    return (
        "Obese",
        "Your BMI is in the obese range. Consider consulting a healthcare professional for personalized guidance.",
    )


@app.get("/")
def read_root() -> dict[str, str]:
    return {
        "message": "Welcome to the BMI Calculator API. Send height_cm and weight_kg to POST /bmi."
    }


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/bmi", response_model=BMIResponse)
def calculate_bmi_endpoint(request: BMIRequest) -> BMIResponse:
    bmi = calculate_bmi(request.height_cm, request.weight_kg)
    category, message = get_bmi_category(bmi)

    return BMIResponse(
        bmi=round(bmi, 2),
        category=category,
        message=message,
    )
