# Quick Health Check - Automated IP Update System

This repository provides an automated system for updating SSH configurations across multiple remote hosts and pentesters' machines. The system is built with a Flask server that stores and serves the latest IP addresses for specific hosts (apex, cybercoders, and creativecc), and scripts (client.py and pentesters.py) that handle updating the relevant SSH configurations on the clients and testers' machines.

## Components

    Flask Server (server.py): Manages and serves updated IP addresses for the remote hosts.
    Client Script (client.py): Runs on each remote host (apex, cybercoders, creativecc) to send their updated IP addresses to the Flask server.
    Pentesters Script (pentesters.py): Runs on the pentesters' machines to pull the updated IP addresses from the Flask server and update their local SSH configuration.
    Cron Jobs: Automates the periodic execution of client.py and pentesters.py on remote hosts and testers' machines, respectively.
    Systemd Service: Automates the start of the Flask server (server.py) on boot and ensures it stays running.

## Installation Instructions

    ### Flask Server Setup

### Prerequisites

    Python 3.x installed
    Flask installed (pip install flask)
    Server with access to the network where remote hosts and pentesters' machines reside

#### Steps

    Clone the Repository:

git clone https://github.com/your-repo/quick_health_check.git cd quick_health_check

    Install Flask:

Install the required Python packages using pip:

pip install flask

    Set Up the systemd Service:

Create the systemd service file for the Flask app.

Edit or create a service file at /etc/systemd/system/healthcheck.service:

sudo nano /etc/systemd/system/healthcheck.service

Add the following content to the file:

[Unit] Description=IP Updater Flask Service After=network.target

[Service] User=your-username # Replace with your username WorkingDirectory=/path/to/your/flask/app # Replace with the path to your Flask app ExecStart=/usr/bin/python3 /path/to/your/flask/app/server.py # Replace with the full path to server.py Restart=always

[Install] WantedBy=multi-user.target

    Reload systemd:

After saving the file, reload systemd and start the service:

sudo systemctl daemon-reload sudo systemctl enable healthcheck sudo systemctl start healthcheck

    Check Service Status:

Verify that the Flask server is running:

sudo systemctl status healthcheck

Flask Server Configuration

The server.py script handles requests from remote hosts (client.py) and pentesters' machines (pentesters.py). It serves updated IPs for the specified hosts (apex, cybercoders, creativecc).

    API Endpoints:
        /config: Returns the current IPs in JSON format.
        /update_ip: Accepts POST requests to update the IP for a specified host.

    Remote Hosts (Clients) Setup

Each remote host (apex, cybercoders, creativecc) needs to run the client.py script to send its updated IP address to the Flask server.

Steps

    Clone the Repository:

On each remote host:

git clone https://github.com/your-repo/quick_health_check.git cd quick_health_check

    Set Up the Cron Job:

On each remote host, set up a cron job to periodically send the updated IP to the Flask server.

Open the crontab for editing:

crontab -e

Add the following line to run client.py every 30 minutes:

*/30 * * * * /usr/bin/python3 /path/to/client.py >> /path/to/client_log.txt 2>&1

Adjust the interval as needed.

    Pentesters Machines Setup

Pentesters will run the pentesters.py script on their local machines to periodically fetch the updated SSH config from the Flask server.

Steps

    Clone the Repository:

On each pentester's machine:

git clone https://github.com/your-repo/quick_health_check.git cd quick_health_check

    Set Up the Cron Job:

Open the crontab for editing:

crontab -e

Add the following line to run pentesters.py every 30 minutes:

*/30 * * * * /usr/bin/python3 /path/to/pentesters.py >> /path/to/pentesters_log.txt 2>&1

Adjust the interval as needed.

    Additional Notes

    Ensure that the paths to client.py and pentesters.py are correctly specified in the cron jobs.
    Logs can be reviewed in the specified log file paths (client_log.txt, pentesters_log.txt) for debugging or confirmation.
