from pathlib import Path
from forge.application.ports.system_architecture_generator import SystemArchitectureGenerator
from forge.infrastructure.system_architectures.base_system_generator import BaseSystemGenerator


class MicroservicesGenerator(BaseSystemGenerator, SystemArchitectureGenerator):
    def generate(self, root: Path) -> None:
        services = ["auth", "users", "billing"]

        for service in services:
            self.create_dir(root / "services" / service / "src")
            self.create_dir(root / "services" / service / "tests")

        # gateway opcional
        self.create_dir(root / "gateway")

        # docker-compose base
        self.write_file(
            root / "docker-compose.yml",
            """
            version: '3.9'
            services:
            auth:
                build: ./services/auth
            users:
                build: ./services/users
            billing:
                build: ./services/billing
            """.strip(),
        )