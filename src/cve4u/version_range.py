from dataclasses import dataclass

from cve4u.version import Version


@dataclass(frozen=True)
class VersionRange:
    start: Version | None = None
    end: Version | None = None
    start_included: bool = True
    end_included: bool = False

    def __post_init__(self) -> None:
        if self.start is None and self.end is None:
            raise ValueError("A version range needs a start, an end or both")
        if self.start is not None and self.end is not None and self.start > self.end:
            raise ValueError("The start of a version range must be before its end")
