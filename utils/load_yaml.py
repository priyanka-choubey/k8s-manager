import yaml
# import os

def load_subprocesses():
    # script_dir = os.path.dirname(__file__)
    # rel_path = "command.yaml"
    # abs_file_path = os.path.join(script_dir, rel_path)
    with open("utils/command.yaml", "r") as f:
        return yaml.safe_load(f)