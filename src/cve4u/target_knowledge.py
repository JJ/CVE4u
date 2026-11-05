from dataclasses import dataclass

from cve4u.product import Product
from cve4u.version import Version


@dataclass(frozen=True,slots=True,kw_only=True)
class TargetKnowledge:
    os: str | None = None
    product: Product | None = None
    version: Version | None = None
