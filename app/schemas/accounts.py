from datetime import datetime
from typing import Optional

from pydantic import UUID4, BaseModel, EmailStr, validator, Field


class TokenBase(BaseModel):
    """ Return response data """
    token: UUID4 = Field(..., alias="access_token")
    expires: datetime
    token_type: Optional[str] = "bearer"

    class Config:
        allow_population_by_field_name = True

    @validator("token")
    def hexlify_token(cls, value):
        """ Convert UUID to pure hex string """
        return value.hex


class AccountBase(BaseModel):
    """ Return response data """
    id: int
    brief: str
    name: str
    fund_id: int
    dateStart: datetime
    dateEnd: datetime
    user_id: int


class AccountCreate(BaseModel):
    """ Validate request data """
    brief: str
    name: str
    fund_id: int
    user_id: int


class Account(AccountBase):
    """ Return detailed response data with token """
    token: TokenBase = {}
