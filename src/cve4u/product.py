from pydantic import BaseModel, ConfigDict


class Product(BaseModel):
    model_config = ConfigDict(frozen=True)

    vendor: str
    name: str
