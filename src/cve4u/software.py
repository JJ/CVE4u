from pydantic import BaseModel, ConfigDict


class Software(BaseModel):
    model_config = ConfigDict(frozen=True)

    vendor: str
    product: str
    aliases: tuple[str, ...] = ()

    def matches_name(self, name: str) -> bool:
        query = " ".join(name.casefold().split())
        if not query:
            return False

        for candidate in (self.product, *self.aliases):
            normalized = " ".join(candidate.casefold().split())
            if not normalized:
                continue
            qualified = " ".join(f"{self.vendor} {candidate}".casefold().split())
            if query in (normalized, qualified):
                return True

        return False
