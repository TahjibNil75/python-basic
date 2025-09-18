from pydantic import BaseModel, Feild_validator, model_validator

class User(BaseModel):
    id:int
    username: str

    @Feild_validator('username')
    def username_length(cls, value):
        if len(value) < 4:
            raise ValueError('Username must be at least 4 characters long')
        return value
    


class SignUpData(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def password_validation(cls, values):
        if values.password != values.confirm_password:
            raise ValueError('Password and Confirm Password do not match')
        return values