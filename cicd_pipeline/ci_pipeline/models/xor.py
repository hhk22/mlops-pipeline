from pydantic import BaseModel


class XORInput(BaseModel):
    x1: float
    x2: float