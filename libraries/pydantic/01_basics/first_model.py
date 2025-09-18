from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool 

# user_one_input_data = {'id':1, 'name':'John', 'is_active':"active"}
user_one_input_data = {'id':1, 'name':'John', 'is_active':True}
user = User(**user_one_input_data)
print(user)