from enum import Enum


class SystemType(Enum):
    MONOLITH = "monolith"
    MODULAR_MONOLITH = "modular_monolith"
    MICROSERVICES = "microservices"

    @classmethod
    def choices(cls):
        return [
            ("Monolithic Application", cls.MONOLITH.value),
            ("Modular Monolith ⭐ Recommended", cls.MODULAR_MONOLITH.value),
            ("Microservices", cls.MICROSERVICES.value),
        ]

    @classmethod
    def from_value(cls, value: str) -> "SystemType":
        try:
            return cls(value)
        except ValueError:
            raise ValueError(f"Invalid system type: {value}")