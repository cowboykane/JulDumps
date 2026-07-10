import shutil, os
from pathlib import Path

# System Inventory Generator:

servers = [
    {"hostname": "web01", "ip": "10.0.0.5", "os": "Ubuntu"},
    {"hostname": "db01", "ip": "10.0.0.10", "os": "Rocky Linux"},
    {"hostname": "proxy01", "ip": "10.0.0.20", "os": "Debian"}
]

print("===== SERVER INVENTORY =====")

for server in servers:
    hostname = server["hostname"]
    ip = server["ip"]
    os_type = server["os"]
    
    print(f"Hostname: {hostname}")
    print(f"IP: {ip}")
    print(f"OS: {os_type}")
    print() 

print(f"Total Servers: {len(servers)}")
