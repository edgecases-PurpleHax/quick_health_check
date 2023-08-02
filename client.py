import requests
import subprocess
status = subprocess.call(['systemctl', 'is-active', '--quiet', 'ssh'])
if (status == 0):
    active = "active"
else:
    active = "inactive"

r = requests.get(url=f"http://192.168.0.132:9000/health_check?active={active}")
print(r.content)
