# forge/application/ports/system_architecture_generator.py
from abc import ABC, abstractmethod
from pathlib import Path


class SystemArchitectureGenerator(ABC):
    @abstractmethod
    def generate(self, root: Path) -> None:
        """Generate project structure based on system architecture."""
        pass