from dataclasses import dataclass
from forge.domain.architecture import Architecture


@dataclass
class Project:
    name: str
    architecture: Architecture
    language: str

    def supports_docker(self) -> bool:
        return self.language in ("Go", "Node.js", "Nest.js")