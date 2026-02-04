from forge.infrastructure.generators.node_project_generator import NodeProjectGenerator
from forge.infrastructure.generators.go_generator import GoProjectGenerator


def get_generator(language: str):
    if language == "Node.js":
        return NodeProjectGenerator()

    if language == "Go":
        return GoProjectGenerator()

    raise ValueError(f"Unsupported language: {language}")
