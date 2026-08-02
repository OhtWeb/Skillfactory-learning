def log_filter(logs, log_level):
    for line in logs.strip().split('\n'):
        if log_level in line:
            yield line
logs = """\
2023-08-15 14:15:24 INFO Starting the system.
2023-08-15 14:15:26 WARN System load is above 80%.
2023-08-15 14:15:27 ERROR Failed to connect to database.
2023-08-15 14:15:28 INFO Connection retry in 5 seconds.
"""
for log in log_filter(logs, 'INFO'):
    print(log)