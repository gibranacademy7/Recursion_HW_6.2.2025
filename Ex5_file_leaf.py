# file_leaf.py
from component import Component

class FileLeaf(Component):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size  # File size in bytes

    def draw(self, indent=0):
        print(" " * indent + f"- {self.name} ({self.size} bytes)")
