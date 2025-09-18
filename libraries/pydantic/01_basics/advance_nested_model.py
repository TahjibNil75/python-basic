from typing import List, Optional, Union
from pydantic import BaseModel, Field





class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class Company(BaseModel):
    name: str
    address: Optional[Address] = None

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
    company: Optional[Company] = None



