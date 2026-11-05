from dataclasses import dataclass

from cve4u.version import Version


@dataclass(frozen=True)
class VersionRange:
    start: Version | None = None
    end: Version | None = None
    start_included: bool = True
    end_included: bool = False

