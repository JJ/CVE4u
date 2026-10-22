from dataclasses import dataclass, field


@dataclass(frozen=True, order=True)
class Version:
    """
    Software version such as 2.4.50, compared number by number.
    We can compare versions with <, <=, >, >=, == and !=.
    """

    text: str = field(compare=False)
    numbers: tuple[int, ...] = field(init=False)

    def __post_init__(self) -> None:
        numbers = []
        for piece in self.text.split("."):
            numbers.append(int(piece))

        object.__setattr__(self, "numbers", tuple(numbers))
