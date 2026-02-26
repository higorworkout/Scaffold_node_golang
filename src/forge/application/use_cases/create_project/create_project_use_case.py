from forge.application.commands.create_project_command import CreateProjectCommand
from forge.domain.project import Project


class CreateProjectUseCase:
    def __init__(
        self,
        docker_generator,
        system_creators: dict,
        iac_generators: dict,
        repo_creator,
    ):
        self.system_creators = system_creators
        self.docker_generator = docker_generator
        self.iac_generators = iac_generators
        self.repo_creator = repo_creator

    def execute(self, command: CreateProjectCommand) -> None:
        project = Project(
            name=command.name,
            architecture=command.architecture,
            system_type=command.system_type,
            language=command.language,
        )

        # --- Features opcionais ---

        self._handle_docker(command, project)
        self._handle_iac(command, project)
        self._handle_repository(command, project)

    # -----------------------------
    # Handlers privados
    # -----------------------------

    def _handle_docker(self, command, project):
        if command.docker and project.supports_docker():
            self.docker_generator.generate(project)

    def _handle_iac(self, command, project):
        if not command.iac:
            return

        generator = self.iac_generators.get(command.iac)

        if generator:
            generator.generate(project)

    def _handle_repository(self, command, project):
        if command.create_repo:
            self.repo_creator.create(project, provider=command.repo_provider)
