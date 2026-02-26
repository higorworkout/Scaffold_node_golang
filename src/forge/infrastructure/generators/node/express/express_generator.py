from pathlib import Path


class NodeExpressGenerator:

    def __init__(self, orm_generator=None):
        self.orm_generator = orm_generator

    def generate(self, path: Path):
        self._generate_base_structure(path)

        if self.orm_generator:
            self.orm_generator.generate(path)