from dataclasses import dataclass


@dataclass(eq=False)
class CVE:
    _id: str
    _descriptions: str
    _title: str | None = None
