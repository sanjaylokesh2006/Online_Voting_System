# main.py


from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from crud import create_voting_option, read_voting_option, read_all_voting_options, update_voting_option, delete_voting_option
from schemas import VotingOptionCreate, VotingOptionUpdate

app = FastAPI()

@app.post("/voting-options/", response_model=VotingOptionCreate)
def create_voting_option_endpoint(voting_option: VotingOptionCreate, db: Session = Depends(get_db)):
    return create_voting_option(db=db, voting_option=voting_option)

@app.get("/voting-options/{voting_option_id}", response_model=VotingOptionCreate)
def read_voting_option_endpoint(voting_option_id: int, db: Session = Depends(get_db)):
    voting_option = read_voting_option(db=db, voting_option_id=voting_option_id)
    if voting_option is None:
        raise HTTPException(status_code=404, detail="Voting option not found")
    return voting_option

@app.get("/voting-options/", response_model=list[VotingOptionCreate])
def read_all_voting_options_endpoint(db: Session = Depends(get_db)):
    return read_all_voting_options(db=db)

@app.put("/voting-options/{voting_option_id}", response_model=VotingOptionUpdate)
def update_voting_option_endpoint(voting_option_id: int, voting_option: VotingOptionUpdate, db: Session = Depends(get_db)):
    updated_voting_option = update_voting_option(db=db, voting_option_id=voting_option_id, voting_option=voting_option)
    if updated_voting_option is None:
        raise HTTPException(status_code=404, detail="Voting option not found")
    return updated_voting_option

@app.delete("/voting-options/{voting_option_id}", response_model=bool)
def delete_voting_option_endpoint(voting_option_id: int, db: Session = Depends(get_db)):
    deleted = delete_voting_option(db=db, voting_option_id=voting_option_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Voting option not found")
    return deleted


# database.py


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/dbname"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# models.py


from sqlalchemy import Column, Integer, String
from database import Base

class VotingOption(Base):
    __tablename__ = "voting_options"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)


# schemas.py


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


# crud.py


from sqlalchemy.orm import Session
from models import VotingOption
from schemas import VotingOptionCreate, VotingOptionUpdate

def create_voting_option(db: Session, voting_option: VotingOptionCreate):
    db_voting_option = VotingOption(name=voting_option.name, description=voting_option.description)
    db.add(db_voting_option)
    db.commit()
    db.refresh(db_voting_option)
    return db_voting_option

def read_voting_option(db: Session, voting_option_id: int):
    return db.query(VotingOption).filter(VotingOption.id == voting_option_id).first()

def read_all_voting_options(db: Session):
    return db.query(VotingOption).all()

def update_voting_option(db: Session, voting_option_id: int, voting_option: VotingOptionUpdate):
    db_voting_option = db.query(VotingOption).filter(VotingOption.id == voting_option_id).first()
    if db_voting_option:
        db_voting_option.name = voting_option.name
        db_voting_option.description = voting_option.description
        db.commit()
        db.refresh(db_voting_option)
    return db_voting_option

def delete_voting_option(db: Session, voting_option_id: int):
    db_voting_option = db.query(VotingOption).filter(VotingOption.id == voting_option_id).first()
    if db_voting_option:
        db.delete(db_voting_option)
        db.commit()
        return True
    return False


# routes.py


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from crud import create_voting_option, read_voting_option, read_all_voting_options, update_voting_option, delete_voting_option
from schemas import VotingOptionCreate, VotingOptionUpdate

router = APIRouter()

@router.post("/voting-options/", response_model=VotingOptionCreate)
def create_voting_option_endpoint(voting_option: VotingOptionCreate, db: Session = Depends(get_db)):
    return create_voting_option(db=db, voting_option=voting_option)

@router.get("/voting-options/{voting_option_id}", response_model=VotingOptionCreate)
def read_voting_option_endpoint(voting_option_id: int, db: Session = Depends(get_db)):
    voting_option = read_voting_option(db=db, voting_option_id=voting_option_id)
    if voting_option is None:
        raise HTTPException(status_code=404, detail="Voting option not found")
    return voting_option

@router.get("/voting-options/", response_model=list[VotingOptionCreate])
def read_all_voting_options_endpoint(db: Session = Depends(get_db)):
    return read_all_voting_options(db=db)

@router.put("/voting-options/{voting_option_id}", response_model=VotingOptionUpdate)
def update_voting_option_endpoint(voting_option_id: int, voting_option: VotingOptionUpdate, db: Session = Depends(get_db)):
    updated_voting_option = update_voting_option(db=db, voting_option_id=voting_option_id, voting_option=voting_option)
    if updated_voting_option is None:
        raise HTTPException(status_code=404, detail="Voting option not found")
    return updated_voting_option

@router.delete("/voting-options/{voting_option_id}", response_model=bool)
def delete_voting_option_endpoint(voting_option_id: int, db: Session = Depends(get_db)):
    deleted = delete_voting_option(db=db, voting_option_id=voting_option_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Voting option not found")
    return deleted


# requirements.txt


fastapi[all]
sqlalchemy
psycopg2-binary
pydantic
uvicorn