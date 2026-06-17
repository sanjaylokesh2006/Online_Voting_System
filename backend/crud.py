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

def get_voting_option(db: Session, voting_option_id: int):
    return db.query(VotingOption).filter(VotingOption.id == voting_option_id).first()