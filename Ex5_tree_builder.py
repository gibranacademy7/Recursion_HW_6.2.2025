# tree_builder.py
import os
from Ex5_file_leaf import FileLeaf
from Ex5_directory_composite import DirectoryComposite

def build_tree(path):
    if os.path.isfile(path):  # If it's a file, return a Leaf
        return FileLeaf(os.path.basename(path), os.path.getsize(path))

    elif os.path.isdir(path):  # If it's a directory, return a Composite
        directory = DirectoryComposite(os.path.basename(path))
        for item in os.listdir(path):  # Iterate over items in directory
            item_path = os.path.join(path, item)
            directory.add(build_tree(item_path))  # Recursive call
        return directory

    return None  # If path is invalid
