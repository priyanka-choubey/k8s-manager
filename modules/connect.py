from utils.sub import run_subprocess
from utils.load_yaml import load_subprocesses 

subprocesses = load_subprocesses().get("connect")

def connect_to_cluster(config):
    run_subprocess(subprocesses.get("update_kubeconfig"), config)

    run_subprocess(subprocesses.get("check_cluster_connection"), print_status=True)
    
    try:
        run_subprocess(subprocesses.get("check_helm"))
    except:
        run_subprocess(subprocesses.get("install_helm"), print_status=True)     
        return 

    try:
        run_subprocess(subprocesses.get("check_keda"))
    except:
        run_subprocess(subprocesses.get("install_keda"), print_status=True)
        return
