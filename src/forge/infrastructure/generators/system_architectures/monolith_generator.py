from pathlib import Path
from forge.application.ports.system_architecture_generator import SystemArchitectureGenerator
from forge.infrastructure.system_architectures.base_system_generator import BaseSystemGenerator


class MonolithGenerator(BaseSystemGenerator, SystemArchitectureGenerator):
    def generate(self, root: Path) -> None:
        self.create_dir(root / "src")
        self.create_dir(root / "tests")