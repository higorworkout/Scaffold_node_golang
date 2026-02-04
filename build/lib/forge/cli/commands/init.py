# forge/cli/run.py

from forge.cli.flows.create_project_flow import collect_project_answers
from forge.cli.presenters.summary_presenter import ProjectSummaryPresenter
from forge.application.mappers.project_mapper import answers_to_command
from forge.application.use_cases.create_project_use_case import CreateProjectUseCase


def run():
    print("🔥 Welcome to Forge\n")

    # 1️⃣ Collect answers via CLI Flow
    answers = collect_project_answers()

    # 2️⃣ Present summary
    ProjectSummaryPresenter.show(answers)

    # 3️⃣ Map answers → Command
    command = answers_to_command(answers)

    # 4️⃣ Execute Use Case
    use_case = CreateProjectUseCase()
    use_case.execute(command)