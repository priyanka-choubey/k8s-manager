import yaml
import subprocess
from utils.sub import run_subprocess
from utils.load_yaml import load_subprocesses


def get_health(name, namespace):
    sub = load_subprocesses().get("health")

    deploy_result = run_subprocess(sub.get("deployment"), name, namespace)
    deploy = cli_output_to_yaml(deploy_result)
    if not deploy:
        return

    print("📦 Deployment Status:")
    replicas = deploy.get("status", {}).get("replicas", "N/A")
    print(f"   Replicas: {replicas}")

    print("\n📝 Deployment Conditions:")
    conditions = deploy.get("status", {}).get("conditions", [])
    if conditions:
        for condition in conditions:
            print(f"   - {condition.get('type')}: {condition.get('status')} ({condition.get('reason', 'N/A')})")
    else:
        print("   - No conditions reported.")

    print("\n🔍 Associated Pods:")
    selector = deploy.get("spec", {}).get("selector", {}).get("matchLabels", {})
    if not selector:
        print("   - No selector found for deployment.")
        return

    # Convert matchLabels dict to label selector string
    selector_str = ",".join([f"{k}={v}" for k, v in selector.items()])
    pods_result = run_subprocess(sub.get("pods"), selector_str, namespace)
    pods = cli_output_to_yaml(pods_result)
    if not pods or not pods.get("items"):
        print("   - No pods found for this deployment.")
        return

    for pod in pods.get("items", []):
        metadata = pod.get("metadata", {})
        status = pod.get("status", {})
        print(f"\n📦 Pod: {metadata.get('name')}")
        print(f"   - Phase: {status.get('phase')}")
        print(f"   - Host IP: {status.get('hostIP')}")
        print(f"   - Pod IP: {status.get('podIP')}")
        print(f"   - Start Time: {status.get('startTime')}")

        for container in status.get("containerStatuses", []):
            print(f"   - Container: {container.get('name')}")
            print(f"     > Ready: {container.get('ready')}")
            print(f"     > Restart Count: {container.get('restartCount')}")
            print(f"     > Image: {container.get('image')}")
        if not status.get("containerStatuses"):
            print("   - No container status available.")


def cli_output_to_yaml(result):
    # Check if result is a CalledProcessError (i.e., the command failed)
    if isinstance(result, subprocess.CalledProcessError):
        print(f"Error: Command failed with return code {result.returncode}")
        print(f"Stderr: {result.stderr}")
        return None

    # Ensure result.stdout exists and is a string
    output = getattr(result, "stdout", None)
    if not isinstance(output, str):
        print("Error: Invalid stdout; expected a string.")
        return None

    try:
        return yaml.safe_load(output)
    except yaml.YAMLError as e:
        print(f"YAML parsing error: {e}")
        return None