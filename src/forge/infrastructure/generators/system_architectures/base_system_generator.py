from pathlib import Path


class BaseSystemGenerator:
    def create_dir(self, path: Path):
        path.mkdir(parents=True, exist_ok=True)

    def write_file(self, path: Path, content: str):
        path.write_text(content, encoding="utf-8")