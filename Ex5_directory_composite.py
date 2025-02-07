# directory_composite.py
from component import Component

class DirectoryComposite(Component):
    def __init__(self, name):
        super().__init__(name)
        self.children = []  # Contains files and subdirectories

    def add(self, component):
        self.children.append(component)

    def draw(self, indent=0):
        print(" " * indent + f"[{self.name}]")
        for child in self.children:
            child.draw(indent + 4)  # Increase indentation
