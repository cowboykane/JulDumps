logs = [
    "INFO Login",
    "ERROR Database timeout",
    "INFO Logout",
    "WARNING High CPU",
    "ERROR Permission denied",
    "INFO Backup Complete"
]

log_list = {}

#  parsing

for log in logs:
    line = log.split(" ")
    parts = log
    
    server = parts[0]
    
    log_list[server] = log_list.get(server, 0) + 1
    
