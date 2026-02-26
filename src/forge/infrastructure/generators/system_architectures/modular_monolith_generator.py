from pathlib import Path
from forge.application.ports.system_architecture_generator import SystemArchitectureGenerator
from forge.infrastructure.system_architectures.base_system_generator import BaseSystemGenerator


class ModularMonolithGenerator(BaseSystemGenerator, SystemArchitectureGenerator):
    def generate(self, root: Path) -> None:
        modules = ["users", "auth", "billing"]

        for module in modules:
            self.create_dir(root / "src" / "modules" / module / "domain")
            self.create_dir(root / "src" / "modules" / module / "application")
            self.create_dir(root / "src" / "modules" / module / "infrastructure")
            self.create_dir(root / "src" / "modules" / module / "interfaces")
