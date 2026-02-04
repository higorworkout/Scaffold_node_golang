# application/use_cases/create_project/project_creator.py
from abc import ABC, abstractmethod
from forge.domain.project import Project
from forge.application.commands.create_project_command import CreateProjectCommand

class ProjectCreator(ABC):

    @abstractmethod
    def create(self, project: Project, command: CreateProjectCommand) -> None:
        pass
    
    