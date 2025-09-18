from pydantic import BaseModel, Feild_validator, model_validator

class Person(BaseModel):
    first_name: str
    last_name: str
## multiple field validator
    @Feild_validator('first_name', 'last_name')
    def name_must_be_capitalized(cls,value):
        if not value.istitle():
            raise ValueError('Name must be capitalized')
        return value
    


class User(BaseModel):
    email : str

    @Feild_validator('email')
    def email_must_contain_at_symbol(cls,value):
        if '@' not in value:
            raise ValueError('Invalid email address')
        return value
    


class Product(BaseModel):
    price : str ## $4.44

    @Feild_validator('price',mode='before')
    def parse_price(cls, v):
        if isinstance(v, str):
            return float(v.replace('$',''))
        return v
    

class DateRange(BaseModel):
    start_date: str  ## YYYY-MM-DD
    end_date: str    ## YYYY-MM-DD

    @model_validator(mode='after')
    def check_date_order(cls, values):
        if values.start_date > values.end_date:
            raise ValueError('start_date must be before end_date')
        return values