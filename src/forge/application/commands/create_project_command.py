from dataclasses import dataclass
from typing import Optional
from forge.domain.architecture import Architecture
from forge.src.forge.domain.system_architecture import SystemType


@dataclass(frozen=True)
class CreateProjectCommand:
    name: str
    architecture: Architecture
    system_type: SystemType
    language: str
    docker: bool
    iac: str
    ci: str
    create_repo: bool
    repo_provider: Optional[str]
    repo_name: Optional[str]
    visibility: Optional[str]
    readme: bool