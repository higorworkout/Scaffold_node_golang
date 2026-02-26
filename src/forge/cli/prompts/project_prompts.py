from forge.domain.architecture import Architecture
from forge.src.forge.domain.system_architecture import SystemType
import questionary


def ask_project_name():
    return questionary.text(
        "Project name:",
        validate=lambda x: len(x) > 0
    ).ask()
    
def ask_system_type() -> str:
    return questionary.select(
        "🏗️ What type of system do you want to build?",
        choices=SystemType.choices()
    ).ask()
    
def ask_architecture():
    return questionary.select(
        "Choose architecture:",
        choices=[
            questionary.Choice(title, value)
            for title, value in Architecture.choices()
        ]
    ).ask()
    
def ask_language():
    return questionary.select(
        "Choose language:",
        choices=[
            "Go",
            "Node.js",
            "Nest.js"
        ]
    ).ask()


def ask_docker():
    return questionary.confirm(
        "Enable Docker support?",
        default=True
    ).ask()
    
def ask_iac():
    return questionary.select(
        "Infrastructure as Code:",
        choices=[
            "None",
            "Terraform",
            "AWS CDK",
        ]
    ).ask()
    
def ask_ci():
    return questionary.select(
        "CI/CD:",
        choices=[
            "None",
            "GitHub Actions",
            "GitLab CI",
        ]
    ).ask()
    
# ─────────────────────────────────────────────
# Git / Repositório remoto
# ─────────────────────────────────────────────

def ask_create_remote_repo():
    return questionary.confirm(
        "Create remote repository?",
        default=True
    ).ask()
    
def ask_git_provider():
    return questionary.select(
        "Repository provider:",
        choices=[
            "GitHub",
            "GitLab",
        ]
    ).ask()


def ask_repository_name(default_name: str):
    return questionary.text(
        "Repository name:",
        default=default_name,
        validate=lambda x: len(x.strip()) > 0
    ).ask()


def ask_repository_visibility():
    return questionary.select(
        "Repository visibility:",
        choices=[
            "Private ⭐",
            "Public",
        ]
    ).ask()


def ask_generate_readme():
    return questionary.confirm(
        "Generate README?",
        default=True
    ).ask()