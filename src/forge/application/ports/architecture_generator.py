from abc import ABC, abstractmethod
from pathlib import Path


class ArchitectureGenerator(ABC):
    @abstractmethod
    def generate(self, src_path: Path) -> None:
        """Generate folders/files inside src according to architecture."""
        pass