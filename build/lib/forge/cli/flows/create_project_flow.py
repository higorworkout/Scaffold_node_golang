# cli/flows/create_project_flow.py
from forge.cli.prompts.project_prompts import *
from dataclasses import dataclass

@dataclass
class ProjectAnswers:
    name: str
    architecture: str
    language: str
    docker: bool
    iac: str
    ci: str
    create_repo: bool
    repo_provider: str | None
    repo_name: str | None
    visibility: str | None
    readme: bool

def collect_project_answers() -> ProjectAnswers:
    name = ask_project_name()
    architecture = ask_architecture()
    language = ask_language()
    docker = ask_docker()
    iac = ask_iac()
    ci = ask_ci()

    create_repo = ask_create_remote_repo()

    repo_provider = None
    repo_name = None
    visibility = None

    if create_repo:
        repo_provider = ask_git_provider()
        repo_name = ask_repository_name(name)
        visibility = ask_repository_visibility()
    readme = ask_generate_readme()

    return ProjectAnswers(
        name=name,
        architecture=architecture,
        language=language,
        docker=docker,
        iac=iac,
        ci=ci,
        create_repo=create_repo,
        repo_provider=repo_provider,
        repo_name=repo_name,
        visibility=visibility,
        readme=readme
    )