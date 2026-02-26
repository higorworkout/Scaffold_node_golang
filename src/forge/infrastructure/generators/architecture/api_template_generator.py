# forge/infrastructure/architectures/clean_architecture_generator.py
from pathlib import Path
from forge.application.ports.architecture_generator import ArchitectureGenerator
from forge.src.forge.infrastructure.generators.architecture.base_architecture_generator import BaseArchitectureGenerator

class ApiTemplateGenerator:

    _registry = {
        "node": {
            "express": NodeExpressGenerator,
            "fastify": NodeFastifyGenerator,
            "nestjs": NodeNestGenerator,
        },
        "golang": {
            "gin": GolangGinGenerator,
        }
    }

    def __init__(self, config: ApiTemplateConfig):
        self.config = config

    def generate(self, path: Path):
        language_registry = self._registry.get(self.config.language)

        if not language_registry:
            raise ValueError(f"Unsupported language: {self.config.language}")

        generator_class = language_registry.get(self.config.framework)

        if not generator_class:
            raise ValueError(
                f"Unsupported framework '{self.config.framework}' "
                f"for language '{self.config.language}'"
            )

        generator = generator_class()
        generator.generate(path)