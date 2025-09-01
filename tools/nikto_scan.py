import subprocess

def run_nikto_scan(target: str):
    try:
        result = subprocess.run(
            ["nikto", "-h", target],
            capture_output=True, text=True, check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error running Nikto: {e.stderr}"
