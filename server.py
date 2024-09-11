"""
Flask application to manage and serve updated IP addresses for specified hosts.
The application provides endpoints to retrieve current IP addresses and update
the IP addresses for the specified hosts ('apex', 'cybercoders', 'creativecc').

API Endpoints:
- /config (GET): Returns the current IPs for all hosts in JSON format.
- /update_ip (POST): Updates the IP address for a specified host.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Store the IPs for the hosts that the clients will update
client_ips = {
    "apex": "172.27.246.137",
    "cybercoders": "172.27.246.135",
    "creativecc": "172.27.246.142"
}

@app.route("/config", methods=["GET"])
def get_config():
    """
    Get the current IPs for all specified hosts.

    This endpoint returns the current IP addresses for the 'apex',
    'cybercoders', and 'creativecc' hosts in JSON format.

    Returns:
        Response: JSON object containing hostnames and their corresponding IPs.
    """
    return jsonify(client_ips)

@app.route("/update_ip", methods=["POST"])
def update_ip():
    """
    Update the IP address for a specified host.

    This endpoint accepts a JSON object with the 'host' and 'ip' keys
    to update the corresponding host's IP address in the system.

    Example JSON input:
    {
        "host": "apex",
        "ip": "172.27.247.54"
    }

    Returns:
        Response: Success or error message based on the input.
    """
    data = request.get_json()
    host = data.get('host')
    new_ip = data.get('ip')
    
    if host in client_ips and new_ip:
        client_ips[host] = new_ip
        return jsonify({"status": "success", "message": f"Updated {host} IP to {new_ip}"}), 200
    else:
        return jsonify({"status": "error", "message": "Invalid host or IP"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

