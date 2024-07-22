from pydantic import BaseModel


class LoginUserDto(BaseModel):
    email: str
    password: str
