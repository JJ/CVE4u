from pydantic import BaseModel, ConfigDict

from cve4u.product import Product
from cve4u.version import Version


class TargetKnowledge(BaseModel):
    model_config = ConfigDict(frozen=True)

    os: str | None = None
    product: Product | None = None
    version: Version | None = None
