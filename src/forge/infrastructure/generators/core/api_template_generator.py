from forge.src.forge.infrastructure.generators.core.api_template_config import ApiTemplateConfig
from forge.src.forge.infrastructure.generators.node.express.express_generator import NodeExpressGenerator


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

    _orm_registry = {
        "node": {
            "prisma": PrismaGenerator,
            "typeorm": TypeOrmGenerator,
        }
    }

    def __init__(self, config: ApiTemplateConfig):
        self.config = config

    def generate(self, path: Path):
        language_registry = self._registry.get(self.config.language)

        if not language_registry:
            raise ValueError("Unsupported language")

        framework_class = language_registry.get(self.config.framework)

        if not framework_class:
            raise ValueError("Unsupported framework")

        orm_generator = None

        if self.config.orm:
            orm_class = self._orm_registry[self.config.language].get(self.config.orm)
            orm_generator = orm_class()

        generator = framework_class(orm_generator=orm_generator)
        generator.generate(path)