from typing import Optional

from pydantic import BaseModel, Field
import re

class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=2,
        max_length=50,
        description="The full name of the employee",
        example="John Doe"
    )
    department: Optional[str] = "General"
    salary: float = Field(
        ...,
        ge=5000,
        le=200000,
        description="The annual salary of the employee in BDT",
    )


class Price(BaseModel):
    ammount: float
    discount: float = Field(
        ...,
        ge=0,
        le=100,
        description="Discount percentage",
    )

