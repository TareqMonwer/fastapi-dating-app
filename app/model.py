from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Tareq Monwer",
                "email": "tareqmonwer@mail.com",
                "password": "mypassword"
            }
        }


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...) 
    password: str = Field(...) 
    
    class Config:
        schema_extra = { 
            "example": {
                "email": "tareqmonwer@mail.com",
                "password": "mypassword"  
            }
        }        


