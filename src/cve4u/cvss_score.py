from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class CvssScore(BaseModel):
    model_config = ConfigDict(frozen=True)

    version: Literal["2.0", "3.0", "3.1", "4.0"]
    score: float = Field(ge=0, le=10)
    vector: str
    severity: Literal["NONE", "LOW", "MEDIUM", "HIGH", "CRITICAL"] | None = None
