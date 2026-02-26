# forge/infrastructure/architectures/base_architecture_generator.py
from pathlib import Path


class BaseArchitectureGenerator:
    def create_dir(self, path: Path):
        path.mkdir(parents=True, exist_ok=True)

    def write_file(self, path: Path, content: str):
        path.write_text(content, encoding="utf-8")