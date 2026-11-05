from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    vendor: str
    name: str
