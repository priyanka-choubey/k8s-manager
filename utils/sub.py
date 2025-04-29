import subprocess

def run_subprocess(sub, *args, print_status=False):
    try:
        result = subprocess.run(sub.get("command").format(*args), capture_output=True, text=True, shell=True, check=True)
        if print_status:
            print("✅ "+ sub.get("success"))
        return result
    except subprocess.CalledProcessError as e:
        if print_status:
            print("❌ "+ sub.get("failure"))
        return e