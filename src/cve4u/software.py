from pydantic import BaseModel, ConfigDict


class Software(BaseModel):
    model_config = ConfigDict(frozen=True)

    vendor: str
    product: str
    platforms: tuple[str, ...] = ()
