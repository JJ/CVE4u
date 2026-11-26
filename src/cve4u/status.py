from enum import StrEnum


class Status(StrEnum):
    AFFECTED = "affected"
    UNAFFECTED = "unaffected"
    UNKNOWN = "unknown"
