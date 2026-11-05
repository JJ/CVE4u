from dataclasses import dataclass, field


@dataclass(frozen=True, order=True)
class Version:
    major: int
    minor: int
    patch: int
