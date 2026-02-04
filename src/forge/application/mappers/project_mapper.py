from forge.cli.flows.create_project_flow import ProjectAnswers
from forge.application.commands.create_project_command import CreateProjectCommand
from forge.domain.architecture import Architecture


def answers_to_command(answers: ProjectAnswers) -> CreateProjectCommand:
    return CreateProjectCommand(
        name=answers.name,
        architecture=Architecture.from_value(answers.architecture),
        language=answers.language,
        docker=answers.docker,
        iac=answers.iac,
        ci=answers.ci,
        create_repo=answers.create_repo,
        repo_provider=answers.repo_provider,
        repo_name=answers.repo_name,
        visibility=answers.visibility,
        readme=answers.readme,
    )