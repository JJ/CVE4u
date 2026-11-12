from functools import total_ordering

from pydantic import BaseModel, ConfigDict, computed_field


@total_ordering
class Version(BaseModel):
    model_config = ConfigDict(frozen=True)

    text: str

    @computed_field
    @property
    def numbers(self) -> tuple[int, ...]:
        return tuple(int(p) for p in self.text.split(".") if p.isdigit())

    def __lt__(self, other: "Version") -> bool:
        if not isinstance(other, Version):
            return NotImplemented
        return self.numbers < other.numbers
