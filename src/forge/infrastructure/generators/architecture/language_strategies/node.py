

class NodeApiGenerator(BaseArchitectureGenerator):

    def generate(self, path: Path):
        self.copy_template(
            template_path="templates/backend//clean",
            target_path=path
        )