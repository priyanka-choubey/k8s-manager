import yaml

def load_subprocesses():
    with open("utils/command.yaml", "r") as f:
        return yaml.safe_load(f)