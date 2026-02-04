from pathlib import Path
from forge.domain.project import Project

class BaseGenerator:
    
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)

    def create_dir(self, path: Path):
        path.mkdir(parents=True, exist_ok=True)
        
    def write_file(self, path: Path, content: str):
        path.write_text(content, encoding="utf-8") 