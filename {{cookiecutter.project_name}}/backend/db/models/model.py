from sqlalchemy import Column, Integer

from backend.db.base_class import Base


class Model(Base):
    __tablename__ = "Model"

    id = Column(Integer, primary_key=True)