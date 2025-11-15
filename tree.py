import os


def print_tree(start_path, indent=""):
    items = sorted(os.listdir(start_path))
    for index, item in enumerate(items):
        path = os.path.join(start_path, item)
        connector = "└── " if index == len(items) - 1 else "├── "
        print(indent + connector + item)

        if os.path.isdir(path):
            extension = "    " if index == len(items) - 1 else "│   "
            print_tree(path, indent + extension)


if __name__ == "__main__":
    root = "."  # change to project path or keep as "." for current directory
    print(os.path.abspath(root))
    print_tree(root)
