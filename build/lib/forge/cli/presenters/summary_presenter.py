# cli/presenters/summary_presenter.py
from forge.cli.flows.create_project_flow import ProjectAnswers


class ProjectSummaryPresenter:

    @staticmethod
    def show(answers: ProjectAnswers) -> None:
        print("\n✅ Configuration summary:\n")

        # ─────────────────────────────────────────────
        # Core
        # ─────────────────────────────────────────────
        print("📦 Project")
        print(f"  Name: {answers.name}")
        print(f"  Architecture: {answers.architecture}")
        print(f"  Language: {answers.language}")

        # ─────────────────────────────────────────────
        # Tooling
        # ─────────────────────────────────────────────
        print("\n🛠 Tooling")
        print(f"  Docker: {'Yes' if answers.docker else 'No'}")
        print(f"  Infrastructure as Code: {answers.iac}")
        print(f"  CI/CD: {answers.ci}")

        # ─────────────────────────────────────────────
        # Repository
        # ─────────────────────────────────────────────
        print("\n🔗 Repository")

        if answers.create_repo:
            print("  Remote repository: Enabled")
            print(f"    Provider: {answers.repo_provider}")
            print(f"    Name: {answers.repo_name}")
            print(f"    Visibility: {answers.visibility}")
        else:
            print("  Remote repository: Disabled")

        # ─────────────────────────────────────────────
        # Extras
        # ─────────────────────────────────────────────
        print("\n📄 Extras")
        print(f"  README: {'Yes' if answers.readme else 'No'}")

        print("\n─────────────────────────────────────────────")