from fastapi import FastAPI, HTTPException, Depends

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel


from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Integration with sql")

#### Database setup
engine = create_engine("sqlite:///test.db", connect_args={"check_same_thread": False})
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

get_db()


## Database Model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    role = Column(String(50), nullable=False)

Base.metadata.create_all(bind=engine)


## Pydantic Models
class UserCreate(BaseModel):
    name: str
    email: str
    role: str

class UserResponse(BaseModel):
    id:int
    name: str
    email: str
    role: str

    class Config:
        from_attributes = True





@app.get("/")
def root():
    return {"message":"Basics of fast APi"}



@app.get("/user/{user_id}", response_model=UserResponse)
def get_user(user_id:int, db:Session=Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.post("/user/", response_model=UserResponse)
def create_user(user: UserCreate, db:Session=Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    
    ## Create User
    new_user = User(name=user.name, email=user.email, role=user.role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

## Update User
@app.put("/user/{user_id}", response_model=UserResponse)
def update_user(user_id:int, updated_user:UserCreate, db:Session= Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.name = updated_user.name
    user.email = updated_user.email
    user.role = updated_user.role

    db.commit()
    db.refresh(user)
    return user


## Delete User
@app.delete("/user/{user_id}")
def delete_user(user_id:int, db:Session=Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"detail": "User deleted successfully"}    

# ## Get All Users
# @app.get("/users/", response_model=List[UserResponse])
# def get_users(skip:int=0, limit:int=10, db:Session=Depends(get_db)):
#     users = db.query(User).offset(skip).limit(limit).all()
#     return users


## Get All Users
@app.get("/users/", response_model=List[UserResponse])
def get_users(db:Session=Depends(get_db)):
    users = db.query(User).all()
    return users