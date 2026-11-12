from pydantic import BaseModel, ConfigDict, Field


class CveId(BaseModel):
    model_config = ConfigDict(frozen=True)

    value: str = Field(pattern=r"^CVE-[0-9]{4}-[0-9]{4,19}$")
