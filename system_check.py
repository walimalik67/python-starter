import os
import pathlib
import sys

data = {
    "python_executable": sys.executable,
    "python_version": sys.version.split()[0],
    "cwd": os.getcwd(),
    "in_venv": (hasattr(sys, "real_prefix") or sys.prefix != getattr(sys, "base_prefix", sys.prefix)),
}

print("Interpreter:", data["python_executable"])
print("Python:", data["python_version"])
print("CWD:", data["cwd"])
print("In venv:", data["in_venv"])

# write a file locally
pathlib.Path("output.txt").write_text("Hello from python-starter!\\n", encoding="utf-8")
print("Wrote output.txt")
