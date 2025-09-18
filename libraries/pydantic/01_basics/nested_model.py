from typing import List, Optional
from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name : str
    address : Address


address = Address(
    street="123 Main St",
    city="Dhaka",
    zip_code="12345"
)

user = User(
    id=1,
    name="Tahjib",
    address=address
)

print(user)


user_data = {
    "id": 2,
    "name": "New User",
    "address": {
        "street": "456 Elm St",
        "city": "Chittagong",
        "zip_code": "67890"
    }
}
new_user = User(**user_data)
print(new_user)