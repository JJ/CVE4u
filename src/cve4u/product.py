from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    """Software product identified by vendor and name, as in CVE data."""

    vendor: str
    name: str

    def __post_init__(self) -> None:
        object.__setattr__(self, "vendor", self.vendor.strip().lower())
        object.__setattr__(self, "name", self.name.strip().lower())

