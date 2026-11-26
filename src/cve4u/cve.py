from pydantic import BaseModel, ConfigDict, Field

from cve4u.software import Software


class CVE(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: str = Field(pattern=r"^CVE-[0-9]{4}-[0-9]{4,19}$")
    title: str | None = None
    description: str
    affected: tuple[Software, ...]
