from forge.src.forge.application.ports.project_generator import ProjectGenerator
from forge.src.forge.domain.project import Project
from forge.src.forge.infrastructure.generators.base_generator import BaseGenerator


class GoProjectGenerator(BaseGenerator, ProjectGenerator):
    
    def generate(self, project: Project):
        root = self.base_path / project.name
        
        self.create_dir(root / "src")
        self.create_dir(root / "tests")
        
        self.write_file
        
        self.write_file(
            root / "package.json",
            f"""{{
            "name": "{project.name}",
            "version": "1.0.0",
            "main": "src/index.js"
            }}""")