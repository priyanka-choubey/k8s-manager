import subprocess
from utils.load_yaml import load_subprocesses 

subprocesses = load_subprocesses()

def connect_to_cluster(config):
    run_subprocess(subprocesses.get("update_kubeconfig"), config)

    run_subprocess(subprocesses.get("check_cluster_connection"), print_status=True)
    
    try:
        run_subprocess(subprocesses.get("check_helm"))
    except subprocess.CalledProcessError:
        run_subprocess(subprocesses.get("install_helm"), print_status=True)     
        return 

    try:
        run_subprocess(subprocesses.get("check_keda"))
    except subprocess.CalledProcessError:
        run_subprocess(subprocesses.get("install_keda"), print_status=True)
        return

def run_subprocess(sub, *args, print_status=False):
    try:
        result = subprocess.run(sub.get("command").format(args), shell=True, check=True)
        if print_status:
            print("✅ "+ sub.get("success"))
        return result
    except subprocess.CalledProcessError:
        if print_status:
            print("❌ "+ sub.get("failure"))
        return subprocess.CalledProcessError