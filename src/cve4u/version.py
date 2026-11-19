from pydantic import BaseModel, ConfigDict


class Version(BaseModel):
    model_config = ConfigDict(frozen=True)

    text: str
