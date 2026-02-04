from forge.application.commands.create_project_command import CreateProjectCommand
from forge.domain.project import Project


class CreateProjectUseCase:

    def execute(self, command: CreateProjectCommand) -> None:
        project = Project(
            name=command.name,
            architecture=command.architecture,
            language=command.language,
        )

        # Aqui depois entram os serviços reais
        if command.docker and project.supports_docker():
            print("🐳 Docker will be generated")

        if command.iac == "Terraform":
            print("🌍 Terraform structure will be generated")

        if command.iac == "AWS CDK":
            print("☁️ AWS CDK structure will be generated")

        if command.create_repo:
            print(f"🔗 Repository will be created on {command.repo_provider}")