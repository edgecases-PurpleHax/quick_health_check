import requests
import subprocess
ip = "change me to server ip"
status = subprocess.call(['systemctl', 'is-active', '--quiet', 'ssh'])
if (status == 0):
    active = "active"
else:
    active = "inactive"

r = requests.get(url=f"http://{ip}:9000/health_check?active={active}")
print(r.content)
