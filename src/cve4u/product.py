from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    vendor: str
    name: str

    def __post_init__(self) -> None:
        vendor = self.vendor.strip().lower()
        name = self.name.strip().lower()
        if not vendor or not name:
            raise ValueError("Product vendor and name cannot be empty")
        object.__setattr__(self, "vendor", vendor)
        object.__setattr__(self, "name", name)
