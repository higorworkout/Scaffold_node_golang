from enum import Enum

class Architecture(Enum):
    PROFESSIONAL = "professional"
    CLEAN = "clean"
    HEXAGONAL = "hexagonal"
    
    @classmethod
    def choices(cls):
        return [
            ("Professional (DDD + Clean + Hexagonal) ⭐ Recommended", cls.PROFESSIONAL),
            ("Clean Architecture", cls.CLEAN),
            ("Hexagonal Architecture", cls.HEXAGONAL),
        ]
        
    
    @classmethod
    def from_value(cls, value: str) -> "Architecture":
        try:
            return cls(value)
        except ValueError:
            raise ValueError(f"Invalid architecture: {value}")