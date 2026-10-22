from dataclasses import dataclass, field


@dataclass(frozen=True, order=True)
class Version:
    text: str = field(compare=False)
    numbers: tuple[int, ...] = field(init=False)

    def __post_init__(self) -> None:
        pieces = self.text.split(".")
        if not all(piece.isdecimal() for piece in pieces):
            raise ValueError(f"Version must only contain numbers and dots: {self.text}")

        numbers = [int(piece) for piece in pieces]
        while len(numbers) > 1 and numbers[-1] == 0:
            numbers.pop()

        object.__setattr__(self, "numbers", tuple(numbers))
