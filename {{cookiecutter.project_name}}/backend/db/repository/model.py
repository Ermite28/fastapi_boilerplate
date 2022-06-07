from sqlalchemy.orm import Session

from backend.db.models.model import Model
from backend.schemas.model import CreateModel

def create_new_model(model: CreateModel, db:Session):
    model_object = Model(**model.dict())
    db.add(model_object)
    db.commit()
    db.refresh(model_object)
    return model_object

def retreive_model(id:int, db:Session):
    return db.query(Model).filter(Model.id == id)