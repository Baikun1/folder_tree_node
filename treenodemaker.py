import os
import json

def build_tree(path, ignore_dirs=None, ignore_files=None):
    if ignore_dirs is None:
        ignore_dirs = ['migrations', '.git', '__pycache__', 'node_modules', 'staticfiles', 'test_statics', 'media', 'frontend', 'dist', 'dev-dist', '.DS_Store', '.idea', '.vscode', 'logs', 'env', 'main.pdf']
    if ignore_files is None:
        ignore_files = ['.gitignore']

    name = os.path.basename(path) or path
    node = {"name": name}

    if os.path.isdir(path):
        children = []
        for item in sorted(os.listdir(path)):
            item_path = os.path.join(path, item)
            item_name = os.path.basename(item_path)
            if os.path.isdir(item_path):
                if item_name not in ignore_dirs:
                    children.append(build_tree(item_path, ignore_dirs, ignore_files))
            else:
                if item_name not in ignore_files:
                    children.append(build_tree(item_path, ignore_dirs, ignore_files))
        if children:
            node["children"] = children
    return node

def save_tree_to_json(root_path, output_file="tree2.json", ignore_dirs=None, ignore_files=None):
    tree = build_tree(root_path, ignore_dirs, ignore_files)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(tree, f, indent=4)
    print(f"Tree saved to {output_file}")

# Example usage:
# Save tree of current directory with default ignores
save_tree_to_json(".", "tree3.json")
