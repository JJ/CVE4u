from dataclasses import dataclass


@dataclass(frozen=True,slots=True,kw_only=True)
class TargetKnowledge:
    os: str | None=None
    product: Product | None = None
    version: str | None = None
