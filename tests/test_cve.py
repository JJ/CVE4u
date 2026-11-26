import pytest

from cve4u.cve import CVE
from cve4u.software import Software


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("A720R", True),
        ("TOTOLINK A720R", True),
        ("a720r_firmware", True),
        ("A720R2", False),
    ],
)
def test_cve_matches_affected_product(name: str, expected: bool) -> None:
    cve = CVE(
        id="CVE-2026-82539",
        description="Example vulnerability in TOTOLINK A720R.",
        affected=(
            Software(vendor="Example", product="Other"),
            Software(
                vendor="TOTOLINK",
                product="A720R",
                aliases=("a720r_firmware",),
            ),
        ),
    )

    assert cve.matches_product(name) is expected


def test_cve_without_affected_products() -> None:
    cve = CVE(
        id="CVE-2026-82539",
        description="Example description.",
        affected=(),
    )

    assert not cve.matches_product("A720R")