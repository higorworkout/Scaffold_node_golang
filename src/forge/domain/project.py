from dataclasses import dataclass
from forge.domain.architecture import Architecture
from forge.src.forge.domain.system_architecture import SystemType


@dataclass
class Project:
    name: str
    architecture: Architecture
    system_type = SystemType
    language: str

    def supports_docker(self) -> bool:
        return self.language in ("Go", "Node.js", "Nest.js")