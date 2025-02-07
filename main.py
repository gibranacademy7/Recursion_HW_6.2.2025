# main.py
import sys
from Ex5_tree_builder import build_tree

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <directory_path>")
        sys.exit(1)

    root_path = sys.argv[1]  # Get path from command-line arguments
    root = build_tree(root_path)

    if root:
        root.draw()
    else:
        print("Invalid path!")
