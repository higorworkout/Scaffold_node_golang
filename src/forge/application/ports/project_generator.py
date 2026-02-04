from abc import ABC, abstractmethod
from forge.domain.project import Project


class ProjectGenerator(ABC):

    @abstractmethod
    def generate(self, project: Project) -> None:
        pass
