from pydantic import BaseModel, Field, model_validator, EmailStr

from typing_extensions import Self

#Схема пользователя
class UserSchema(BaseModel):
    username: str = Field(min_length=3,
                          max_length=16)
    email: EmailStr = Field(min_length=3,
                       max_length=256)
    password: str = Field(min_length=3,
                         max_length=16)
    password_confirm: str = Field(exclude=True)

    @model_validator(mode='after')
    def check_password(self) -> Self:
        if self.password != self.password_confirm:
            raise ValueError("Passwords do not match")
        return self

#Схема аутентификация пользователя
class AuthenticationSchema(UserSchema):
    username: str = Field(min_length=3,
                          max_length=16)
    password: str = Field(min_length=3,
                          max_length=16)