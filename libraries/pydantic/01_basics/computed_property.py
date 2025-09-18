from pydantic import BaseModel, computed_field, Field

class Product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity
    


class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(
        ...,
        ge=1,
        description="Number of nights must be at least 1",
    )
    rate_per_night: float

    @computed_field
    @property
    def total_cost(self) -> float:
        return self.nights * self.rate_per_night
    

booking = Booking(
    user_id=1,
    room_id=101,
    nights=3,
    rate_per_night=150.0
)    
print(booking.total_cost)
print(booking.model_dump())