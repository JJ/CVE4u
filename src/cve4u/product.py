from pydantic import BaseModel, ConfigDict


model_config = ConfigDict(frozen=True)
class Product(BaseModel):
    vendor: str
    name: str
