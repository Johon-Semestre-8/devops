import os
import platform

def ping(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    response = os.system(f"ping {param} 1 {host}")
    return response == 0

if __name__ == "__main__":
    host = input("Enter host to ping: ")
    if ping(host):
        print(f"{host} is reachable.")
    else:
        print(f"{host} is not reachable.")