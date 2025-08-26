import sys, requests
print("Interpreter:", sys.executable)
r = requests.get("https://httpbin.org/get", timeout=5)
print("HTTP status:", r.status_code)
print("All good ✅")
