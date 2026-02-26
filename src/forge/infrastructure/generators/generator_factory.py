from forge.src.forge.infrastructure.generators.project.node_project_generator import NodeProjectGenerator
from forge.src.forge.infrastructure.generators.project.go_generator import GoProjectGenerator
from forge.src.forge.infrastructure.generators.project.nest_Project_Generator import NestProjectGenerator


GENERATORS = {
    "Node.js": NodeProjectGenerator,
    "Go": GoProjectGenerator,
    "NestJS": NestProjectGenerator,
}

def get_generator(language: str):
    try:
        return GENERATORS[language]()
    except KeyError:
        raise ValueError(f"Unsupported language: {language}")
