from pydantic import BaseModel, ConfigDict, Field

from cve4u.affected_product import AffectedProduct
from cve4u.cvss_score import CvssScore


class CVE(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: str = Field(pattern=r"^CVE-[0-9]{4}-[0-9]{4,19}$")
    title: str | None = None
    description: str
    affected: tuple[AffectedProduct, ...]
    cvss_scores: tuple[CvssScore, ...] = ()
