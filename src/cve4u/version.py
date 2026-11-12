from functools import total_ordering

from pydantic import BaseModel, ConfigDict


@total_ordering
class Version(BaseModel):
    model_config = ConfigDict(frozen=True)

    text: str
