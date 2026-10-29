from dataclasses import dataclass, field


@dataclass(frozen=True, order=True)
class Version:
    text: str = field(compare=False)
    numbers: tuple[int, ...] = field(init=False)

    def __post_init__(self) -> None:
        cleaned_pieces = []
        for piece in self.text.split("."):
            if piece == "*":
                cleaned_pieces.append("0")
            elif piece.isdecimal():
                cleaned_pieces.append(piece)
            else:
                digits = "".join(filter(str.isdigit, piece))
                if digits:
                    cleaned_pieces.append(digits)
                else:
                    break

        numbers = [int(piece) for piece in cleaned_pieces] if cleaned_pieces else [0]
        while len(numbers) > 1 and numbers[-1] == 0:
            numbers.pop()

        object.__setattr__(self, "numbers", tuple(numbers))
