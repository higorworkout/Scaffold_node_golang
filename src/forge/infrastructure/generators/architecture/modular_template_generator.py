from pathlib import Path
from forge.application.ports.architecture_generator import ArchitectureGenerator
from forge.src.forge.infrastructure.architecture.base_architecture_generator import BaseArchitectureGenerator


class HexagonalArchitectureGenerator(BaseArchitectureGenerator, ArchitectureGenerator):
    def generate(self, src_path: Path) -> None:
        # Core (regra de negócio)
        self.create_dir(src_path / "core" / "domain")
        self.create_dir(src_path / "core" / "application" / "ports")

        # Adapters (entrada e saída)
        self.create_dir(src_path / "adapters" / "inbound")
        self.create_dir(src_path / "adapters" / "outbound")

        # Infrastructure (frameworks, configs, etc.)
        self.create_dir(src_path / "infrastructure")

        # Arquivos README explicativos
        self.write_file(
            src_path / "core" / "domain" / "README.md",
            "# Domain\n\nPure business rules and entities live here.",
        )

        self.write_file(
            src_path / "core" / "application" / "README.md",
            "# Application\n\nUse cases and orchestration logic.",
        )

        self.write_file(
            src_path / "core" / "application" / "ports" / "README.md",
            "# Ports\n\nInterfaces for inbound and outbound communication.",
        )

        self.write_file(
            src_path / "adapters" / "inbound" / "README.md",
            "# Inbound Adapters\n\nHTTP controllers, CLI, events, etc.",
        )

        self.write_file(
            src_path / "adapters" / "outbound" / "README.md",
            "# Outbound Adapters\n\nDatabase, queues, external APIs, etc.",
        )

        self.write_file(
            src_path / "infrastructure" / "README.md",
            "# Infrastructure\n\nFrameworks, configs, and technical details.",
        )