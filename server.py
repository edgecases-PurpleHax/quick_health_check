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
    Return the current IPs for the specified hosts in JSON format.
    
    Returns:
        Response: JSON object containing hostnames and their IPs.
    """
    return jsonify(client_ips)

@app.route("/update_ip", methods=["POST"])
def update_ip():
    """
    Update the IP address for a specified host.
    
    Expected Input:
        JSON object with keys 'host' and 'ip' to update the relevant host's IP.
        
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

