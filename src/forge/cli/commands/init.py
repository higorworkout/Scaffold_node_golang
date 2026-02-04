# forge/cli/run.py
import argparse
from forge.cli.flows.create_project_flow import collect_project_answers
from forge.cli.presenters.summary_presenter import ProjectSummaryPresenter
from forge.application.mappers.project_mapper import answers_to_command
from forge.src.forge.application.use_cases.create_project.create_project_use_case import CreateProjectUseCase
from forge.src.forge.cli.config.load_config import load_project_config


def run():
    parser = argparse.ArgumentParser(
        description=
        "Script de bootstrap completo pra projetos de com arquitetura limpa e hexagonal"
    )
    parser.add_argument("--yes", action="store_true", help="Use default configuration")
    parser.add_argument("--config", type=str, help="Path to config YAML file")

    args = parser.parse_args()

    print("🔥 Welcome to Forge\n")

    if args.config:
        config = load_project_config(args.config)
        answers = collect_project_answers(interactive=False, preset=config)

    elif args.yes:
        answers = collect_project_answers(interactive=False)

    else:
        answers = collect_project_answers(interactive=True)

    ProjectSummaryPresenter.show(answers)

    command = answers_to_command(answers)
    CreateProjectUseCase().execute(command)