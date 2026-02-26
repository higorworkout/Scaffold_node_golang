from typing import Protocol

from scaffold.forge.build.lib.forge.domain.project import Project


class ArchitectureCreator(Protocol):
    def create(self, path: str, project: Project) -> None:
        ...
