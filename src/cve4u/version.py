from dataclasses import dataclass, field


@dataclass(frozen=True, order=True)
class Version:
    text: str = field(compare=False)
    numbers: tuple[int, ...] = field(init=False)
