# Ex.5:

# We need to implement a recursive function that builds a file-system tree using the Composite Design Pattern. In this pattern:
#
# Each directory (folder) will be a Composite, meaning it can contain files and other subdirectories.
# Each file will be a Leaf, storing its name and size.
# Each component (both directories and files) will have a draw() function that prints their names with indentation.
# Steps to Implement:
# Use Python's os or pathlib module to traverse a given directory recursively.
# Create a base class (Component) with a draw() method.
# Create a FileLeaf class (representing a file), which will store:
# The file name
# The file size
# Create a DirectoryComposite class (representing a directory), which will:
# Store the directory name
# Contain a list of child components (files or directories)
# Implement a recursive function to construct the tree from a given file path.
# Use draw() to print the hierarchical structure.


# Class Diagram (UML):

# file_system_tree/
# │── main.py
# │── tree_builder.py
# │── component.py
# │── file_leaf.py
# │── directory_composite.py


# To split this code into separate files while maintaining clean architecture and organization, we can divide it into three modules:
#
# component.py – Defines the Component base class.
# file_leaf.py – Defines the FileLeaf (representing files).
# directory_composite.py – Defines the DirectoryComposite (representing directories).
# tree_builder.py – Contains the recursive function to build the tree.
# main.py – The entry point to run the program.