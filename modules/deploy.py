from utils.sub import run_subprocess
from utils.load_yaml import load_subprocesses

def deploy_manifest(config, name):
    sub = load_subprocesses().get("deploy")

    run_subprocess(sub, name, config)





    


