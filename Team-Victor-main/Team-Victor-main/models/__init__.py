from pydantic import BaseModel

class Restaurants(BaseModel):
    name: str
    cluster: int