from forge.domain.architecture import Architecture
from forge.application.ports.architecture_generator import ArchitectureGenerator

from forge.src.forge.infrastructure.architecture.clean_architecture_generator import (
    CleanArchitectureGenerator,
)
from forge.src.forge.infrastructure.architecture.hexagonal_generator import HexagonalArchitectureGenerator
from forge.src.forge.infrastructure.architecture.professional_architecture_generator import (
    ProfessionalArchitectureGenerator,
)


# Registry de geradores por arquitetura
_GENERATORS: dict[Architecture, type[ArchitectureGenerator]] = {
    Architecture.CLEAN: CleanArchitectureGenerator,
    Architecture.HEXAGONAL: HexagonalArchitectureGenerator,
    Architecture.PROFESSIONAL: ProfessionalArchitectureGenerator,
}


def get_architecture_generator(architecture: Architecture) -> ArchitectureGenerator:
    """
    Factory responsável por retornar o gerador de arquitetura correto.
    """

    try:
        generator_class = _GENERATORS[architecture]
        return generator_class()
    except KeyError as exc:
        raise ValueError(f"Unsupported architecture: {architecture}") from exc