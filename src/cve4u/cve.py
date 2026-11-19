from pydantic import BaseModel, ConfigDict

from cve4u.software import Software


class CVE(BaseModel):
    model_config = ConfigDict(frozen=True)

    title: str | None = None
    description: str
    affected: tuple[Software, ...]
