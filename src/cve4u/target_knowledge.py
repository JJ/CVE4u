from dataclasses import dataclass


@dataclass(frozen=True,slots=True,kw_only=True)
class TargetKnowledge:
    os: str | None=None
    os_version: str | None=None
    product: str | None=None
    version: str | None=None
    vendor: str | None=None
    architecture: str | None=None
