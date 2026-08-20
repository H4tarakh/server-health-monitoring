import psutil
import socket

hostname = socket.gethostname()

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage("/").percent

print("=" * 40)
print(f"Server: {hostname}")
print(f"CPU: {cpu}%")
print(f"Memory: {memory}%")
print(f"Disk: {disk}%")
print("=" * 40)

if cpu > 80:
    print("WARNING: High CPU usage")

if memory > 80:
    print("WARNING: High memory usage")

if disk > 80:
    print("WARNING: High disk usage")
