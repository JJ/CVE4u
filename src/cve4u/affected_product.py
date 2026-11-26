from typing import Self

from pydantic import BaseModel, ConfigDict, model_validator

from cve4u.software import Software
from cve4u.status import Status
from cve4u.version_range import VersionRange


class AffectedProduct(BaseModel):
    model_config = ConfigDict(frozen=True)

    software: Software
    versions: tuple[VersionRange, ...] = ()
    default_status: Status = Status.UNKNOWN

    @model_validator(mode="after")
    def check_versions_or_default_status(self) -> Self:
        if not self.versions and "default_status" not in self.model_fields_set:
            raise ValueError("an affected product needs versions or a default status")
        return self
