from pydantic import BaseModel, ConfigDict

from cve4u.version import Version


class VersionRange(BaseModel):
    model_config = ConfigDict(frozen=True)

    start: Version | None = None
    end: Version | None = None
    start_included: bool = True
    end_included: bool = False
