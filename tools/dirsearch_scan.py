import subprocess

def run_dirsearch_scan(target: str):
    try:
        result = subprocess.run(
            ["dirsearch", "-u", target, "-e", "php,html,js"],
            capture_output=True, text=True, check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error running Dirsearch: {e.stderr}"
