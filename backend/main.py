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