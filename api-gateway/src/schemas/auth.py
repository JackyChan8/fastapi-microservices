from pydantic import BaseModel, Field, field_validator, EmailStr


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str = Field(
        min_length=8,
        max_length=100,
        title='Password',
        description='Password User'
    )
    password_confirm: str

    @field_validator('password_confirm')
    def passwords_match(cls, v, values, **kwargs):
        if 'password' in values.data and v != values.data.get('password'):
            raise ValueError('passwords do not match')
        return v


class UserLogin(UserBase):
    password: str = Field(
        min_length=8,
        max_length=100,
        title='Password',
        description='Password User'
    )
