from pydantic import BaseModel, Field
from typing import Optional


class Employee(BaseModel):
    id: int = Field(..., gt=0)
    name: str = Field(..., min_length=3, max_length=30)
    department: str = Field(..., min_length=3, max_length=30)
    age: Optional[int] = Field(None, gt=18, lt=70) # it can accept 35 or "35", to make it strictly accept only 35, StrictInt can be used.


# ... -> ellipsis -> we give when we tell the parameter is required
# gt -> greater than
# lt -> lower than
# min_length, max_length -> char length
# default=None or directly None, when we want to give a default value (eg, in age)
# this is power of pydantic, it can validate all these things
# this is all implementation of validation