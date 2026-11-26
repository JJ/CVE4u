from pydantic import BaseModel, ConfigDict

from cve4u.software import Software
from cve4u.status import Status
from cve4u.version_range import VersionRange


class AffectedProduct(BaseModel):
    model_config = ConfigDict(frozen=True)

    software: Software
    versions: tuple[VersionRange, ...] = ()
    default_status: Status = Status.UNKNOWN
