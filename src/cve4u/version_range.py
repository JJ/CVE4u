from pydantic import BaseModel, ConfigDict, model_validator

from cve4u.version import Version


class VersionRange(BaseModel):
    model_config = ConfigDict(frozen=True)

    start: Version | None = None
    end: Version | None = None
    start_included: bool = True
    end_included: bool = False

    @model_validator(mode="after")
    def validate_range_boundaries(self) -> "VersionRange":
        if self.start is None and self.end is None:
            raise ValueError("A version range needs a start, an end or both")

        if self.start is not None and self.end is not None:
            if self.start > self.end:
                raise ValueError("The start of a version range must be before its end")
            if self.start == self.end and not (self.start_included and self.end_included):
                raise ValueError("A version range must contain at least one version")

        return self
