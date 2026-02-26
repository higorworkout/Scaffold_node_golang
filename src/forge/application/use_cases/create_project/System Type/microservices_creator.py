from scaffold.forge.build.lib.forge.domain.project import Project


class MicroservicesCreator:
    def __init__(self, architecture_creators: dict):
        self.architecture_creators = architecture_creators

    def create(self, project: Project) -> None:
        creator = self.architecture_creators.get(project.architecture)

        if not creator:
            raise ValueError("Unsupported architecture for microservices")

        creator.create(project)