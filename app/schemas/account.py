from pydantic import BaseModel

from app.common.choices import Position, Tier
from .student import Student


class AccountBase(BaseModel):
    id: str
    nickname: str
    profile_image: str
    level: int
    league_points: int
    wins: int
    losses: int


class AccountCreate(BaseModel):
    nickname: str
    position: Position


class AccountData(AccountBase):
    tier_class: Tier | None
    division: int | None
    league_points: int | None


class Account(AccountBase):
    position: Position
    tier: str
    win_rate: int
    key: int
    owner: Student
