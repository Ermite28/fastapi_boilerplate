from datetime import date
from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class Model(BaseModel):
    id : int

class CreateModel(Model):
    pass

class ShowModel(Model):
    pass
