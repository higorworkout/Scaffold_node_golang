from forge.domain.architecture import Architecture

DEFAULT_PROJECT_CONFIG = {
    "name": "my-project",
    "architecture": Architecture.CLEAN,
    "language": "Node.js",
    "docker": True,
    "iac": "None",
    "ci": "None",
    "create_repo": False,
    "repo_provider": None,
    "repo_name": None,
    "visibility": None,
    "license": "MIT",
    "readme": True,
}