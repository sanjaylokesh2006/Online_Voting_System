from sqlalchemy import Column, Integer, String
from database import Base

class VotingOption(Base):
    __tablename__ = "voting_options"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)