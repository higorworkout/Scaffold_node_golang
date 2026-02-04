from dataclasses import dataclass
from typing import Optional
from forge.domain.architecture import Architecture


@dataclass(frozen=True)
class CreateProjectCommand:
    name: str
    architecture: Architecture
    language: str
    docker: bool
    iac: str
    ci: str
    create_repo: bool
    repo_provider: Optional[str]
    repo_name: Optional[str]
    visibility: Optional[str]
    readme: bool