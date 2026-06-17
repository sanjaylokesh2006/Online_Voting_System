from pydantic import BaseModel

class VotingOptionBase(BaseModel):
    name: str
    description: str | None = None

class VotingOptionCreate(VotingOptionBase):
    pass

class VotingOptionUpdate(VotingOptionBase):
    pass

class VotingOptionRead(VotingOptionBase):
    id: int

    class Config:
        orm_mode = True