import socket
import ipaddress
from datetime import datetime
import argparse
from scanner import discover_hosts


# Command-line arguments
parser = argparse.ArgumentParser(
    description="Simple TCP network scanner for local/lab networks."
)

parser.add_argument(
    "network",
    help="Target network, e.g. 192.168.1.0/24"
)

parser.add_argument(
    "ports",
    help="Comma-separated ports, e.g. 22,80,443"
)

args = parser.parse_args()


# Network validation
network_input = args.network

try:
    network = ipaddress.ip_network(network_input)
except ValueError:
    print("[!] Invalid network address.")
    exit()


# Host discovery
active_hosts = discover_hosts(network)

scan_time = datetime.now()


# Common services
services = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    443: "HTTPS",
    445: "SMB",
    3389: "RDP"
}


# Port input and validation
ports_input = args.ports

try:
    ports = list(
        set(
            int(port.strip())
            for port in ports_input.split(",")
        )
    )

    if any(port < 1 or port > 65535 for port in ports):
        raise ValueError

except ValueError:
    print("Invalid port number.")
    exit()


scan_results = []
host_results = {}


# Port scanning
for target in active_hosts:

    print()
    print(f"[*] Scanning ports on {target}...")

    open_ports = []

    for port in ports:

        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        sock.settimeout(0.5)

        result = sock.connect_ex(
            (str(target), port)
        )

        if result == 0:

            open_ports.append(port)

            print(
                f"  {port}/tcp OPEN "
                f"({services.get(port, 'Unknown')})"
            )

            scan_results.append(
                f"{target}:{port}/tcp OPEN "
                f"({services.get(port, 'Unknown')})"
            )

        sock.close()

    host_results[str(target)] = open_ports

    if not open_ports:
        print("  No open ports found.")


# Generate report
with open("scan_results.txt", "w") as file:

    file.write("========================================\n")
    file.write("Network Scan Report\n")
    file.write("========================================\n")

    file.write(f"Network: {network}\n")
    file.write(f"Scan Time: {scan_time}\n")
    file.write(f"Active Hosts: {len(active_hosts)}\n")
    file.write(f"Ports Requested: {len(ports)}\n")

    file.write("\n")

    file.write("Host Summary:\n")
    file.write("----------------------------------------\n")

    for host, open_ports in host_results.items():

        file.write(
            f"{host} - {len(open_ports)} open port(s)\n"
        )

    file.write("\n")

    file.write("Open Ports:\n")
    file.write("----------------------------------------\n")

    if scan_results:

        for result in scan_results:
            file.write(result + "\n")

    else:

        file.write("No open ports found.\n")