from dataclasses import dataclass

from cve4u.product import Product


@dataclass(frozen=True,slots=True,kw_only=True)
class TargetKnowledge:
    os: str | None = None
    product: Product | None = None
    version: str | None = None
