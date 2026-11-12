from pydantic import BaseModel, ConfigDict

from cve4u.software import Software


class TargetKnowledge(BaseModel):
    model_config = ConfigDict(frozen=True)

    product: Software | None = None
    version: str | None = None
