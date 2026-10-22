from dataclasses import dataclass

from cve4u.version import Version


@dataclass(frozen=True)
class VersionRange:
    """Versions affected by a CVE, such as >= 2.4.0 and < 2.4.50.
    A start or an end set to None means there is no limit on that side.
    """

    start: Version | None = None
    end: Version | None = None
    start_included: bool = True  # True means >=, False means >
    end_included: bool = False  # True means <=, False means <

    def __post_init__(self) -> None:
        if self.start is None and self.end is None:
            raise ValueError("A version range needs a start, an end or both")
        if self.start is not None and self.end is not None:
            if self.start > self.end:
                raise ValueError("The start of a version range must be before its end")

    def contains(self, version: Version) -> bool:
        """Tell whether the version is inside the range."""
        if self.start is not None:
            if self.start_included and version < self.start:
                return False
            if not self.start_included and version <= self.start:
                return False

        if self.end is not None:
            if self.end_included and version > self.end:
                return False
            if not self.end_included and version >= self.end:
                return False

        return True
