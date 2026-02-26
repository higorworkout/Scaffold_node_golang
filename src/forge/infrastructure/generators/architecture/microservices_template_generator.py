from pathlib import Path
from forge.application.ports.architecture_generator import ArchitectureGenerator
from forge.src.forge.infrastructure.architecture.base_architecture_generator import BaseArchitectureGenerator


class ProfessionalArchitectureGenerator(BaseArchitectureGenerator, ArchitectureGenerator):
    def generate(self, src_path: Path) -> None:
        # Domain (DDD-ready)
        self.create_dir(src_path / "domain")

        # Application + Ports (Clean + Hexagonal)
        self.create_dir(src_path / "application" / "ports")

        # Hexagonal adapters
        self.create_dir(src_path / "adapters" / "inbound")
        self.create_dir(src_path / "adapters" / "outbound")

        # Infrastructure (frameworks, configs, etc.)
        self.create_dir(src_path / "infrastructure")

        # Shared kernel (DDD)
        self.create_dir(src_path / "shared")

        # READMEs explicativos
        self.write_file(
            src_path / "domain" / "README.md",
            "# Domain\n\nBusiness entities and rules (DDD-ready).",
        )

        self.write_file(
            src_path / "application" / "README.md",
            "# Application\n\nUse cases and orchestration logic.",
        )

        self.write_file(
            src_path / "application" / "ports" / "README.md",
            "# Ports\n\nInbound and outbound contracts (Hexagonal Architecture).",
        )

        self.write_file(
            src_path / "adapters" / "inbound" / "README.md",
            "# Inbound Adapters\n\nHTTP, CLI, events, and other entry points.",
        )

        self.write_file(
            src_path / "adapters" / "outbound" / "README.md",
            "# Outbound Adapters\n\nDatabase, queues, and external services.",
        )

        self.write_file(
            src_path / "infrastructure" / "README.md",
            "# Infrastructure\n\nFrameworks, drivers, and technical details.",
        )

        self.write_file(
            src_path / "shared" / "README.md",
            "# Shared Kernel\n\nCommon code shared across domains (DDD).",
        )