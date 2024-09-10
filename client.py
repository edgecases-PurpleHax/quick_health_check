import requests
import netifaces as ni

SERVER_URL = "http://155.138.223.225:5000/update_ip"
CLIENT_NAME = "apex"  # Change this to the appropriate client name

def get_tun0_ip():
    """
    Fetch the IP address of the tun0 interface.
    
    Returns:
        str: The IP address of the tun0 interface.
    """
    ni.ifaddresses('tun0')
    ip = ni.ifaddresses('tun0')[ni.AF_INET][0]['addr']
    return ip

def send_ip_to_server(ip):
    """
    Send the client's IP and identifier to the server.
    
    Args:
        ip (str): The client's tun0 IP address.
    
    Returns:
        None
    """
    data = {'host': CLIENT_NAME, 'ip': ip}
    response = requests.post(SERVER_URL, json=data)
    if response.status_code == 200:
        print(f"IP {ip} for {CLIENT_NAME} sent successfully.")
    else:
        print(f"Failed to send IP for {CLIENT_NAME}. Status code: {response.status_code}")

if __name__ == "__main__":
    tun0_ip = get_tun0_ip()
    send_ip_to_server(tun0_ip)

