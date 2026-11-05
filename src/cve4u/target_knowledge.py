from pydantic import BaseModel, ConfigDict

from cve4u.product import Product


model_config = ConfigDict(frozen=True)
class TargetKnowledge(BaseModel):
    os: str | None = None
    product: Product | None = None
    version: str | None = None
