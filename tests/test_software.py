import pytest

from cve4u.software import Software


@pytest.fixture
def software() -> Software:
    return Software(
        vendor="TOTOLINK",
        product="A720R",
        aliases=("a720r_firmware",),
    )


@pytest.mark.parametrize(
    "name",
    [
        "A720R",
        "TOTOLINK A720R",
        "a720r_firmware",
        "A720R_FIRMWARE",
        "  totolink   a720r  ",
        "TOTOLINK a720r_firmware",
    ],
)
def test_matches_product_names(software: Software, name: str) -> None:
    assert software.matches_name(name)


@pytest.mark.parametrize(
    "name", ["A720", "A720R2", "Other A720R", "TOTOLINK", "", "  "]
)
def test_rejects_unrelated_names(software: Software, name: str) -> None:
    assert not software.matches_name(name)


def test_software_without_aliases() -> None:
    software = Software(vendor="TOTOLINK", product="A720R")

    assert software.aliases == ()
    assert software.matches_name("A720R")
    assert software.matches_name("TOTOLINK A720R")
    assert not software.matches_name("a720r_firmware")


def test_matches_multiple_aliases() -> None:
    software = Software(
        vendor="Example",
        product="Router",
        aliases=("router_firmware", "router_os"),
    )

    assert software.matches_name("router_firmware")
    assert software.matches_name("router_os")


def test_ignores_blank_aliases() -> None:
    software = Software(vendor="TOTOLINK", product="A720R", aliases=("", " "))

    assert not software.matches_name("TOTOLINK")