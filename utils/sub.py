import subprocess

def run_subprocess(sub, *args, print_status=False):
    try:
        result = subprocess.run(sub.get("command").format(*args), shell=True, check=True)
        if print_status:
            print("✅ "+ sub.get("success"))
        return result
    except subprocess.CalledProcessError:
        if print_status:
            print("❌ "+ sub.get("failure"))
        return subprocess.CalledProcessError