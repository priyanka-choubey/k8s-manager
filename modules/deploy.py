from utils.sub import run_subprocess
from utils.load_yaml import load_subprocesses

def deploy_manifest(config, name, namespace):
    sub = load_subprocesses().get("deploy")

    run_subprocess(sub.get("deploy"), name, config, namespace)

    run_subprocess(sub.get("check_deployment"), name, namespace)






    


