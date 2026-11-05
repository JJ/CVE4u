from pydantic import BaseModel, ConfigDict, Field, model_validator


class Version(BaseModel):
    model_config = ConfigDict(frozen=True)

    text: str = Field(compare=False)
    numbers: tuple[int, ...] = Field(init=False)

    @model_validator(mode="after")
    def validate_version(self):
        pieces = self.text.split(".")
        if not all(piece.isdecimal() for piece in pieces):
            raise ValueError(f"Version must only contain numbers and dots: {self.text}")

        numbers = [int(piece) for piece in pieces]
        while len(numbers) > 1 and numbers[-1] == 0:
            numbers.pop()

        object.__setattr__(self, "numbers", tuple(numbers))
