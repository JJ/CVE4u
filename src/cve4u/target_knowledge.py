from pydantic import BaseModel, ConfigDict

from cve4u.software import Software
from cve4u.version import Version


class TargetKnowledge(BaseModel):
    model_config = ConfigDict(frozen=True)

    os: str | None = None
    software: Software | None = None
    version: Version | None = None
