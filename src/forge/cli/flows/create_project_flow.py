# cli/flows/create_project_flow.py
from forge.cli.prompts.project_prompts import *
from dataclasses import dataclass

from forge.cli.defauts.project_defaults import DEFAULT_PROJECT_CONFIG

@dataclass
class ProjectAnswers:
    name: str
    system_type: str
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

def collect_project_answers(
        interactive: bool = True,
        preset: dict | None = None,
    ) -> ProjectAnswers:
    
    if not interactive:
        data = preset or DEFAULT_PROJECT_CONFIG
        return ProjectAnswers(**data)
    
    name = ask_project_name()
    system_type=ask_system_type(),
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
        system_type=system_type,
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