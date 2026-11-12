from pydantic import BaseModel, ConfigDict

from cve4u.product import Product


class TargetKnowledge(BaseModel):
    model_config = ConfigDict(frozen=True)

    os: str | None = None
    product: Product | None = None
    version: str | None = None
