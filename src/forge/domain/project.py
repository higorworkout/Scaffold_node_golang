from dataclasses import dataclass
from forge.domain.architecture import Architecture
from forge.domain.system_type import SystemType


@dataclass
class Project:
    name: str
    architecture: Architecture
    system_type = SystemType
    language: str

    def supports_docker(self) -> bool:
        return self.language in ("Go", "Node.js", "Nest.js")