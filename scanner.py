import ipaddress
import subprocess
from concurrent.futures import ThreadPoolExecutor


def discover_hosts(network):
    print(f"[*] Scanning {network}...")
    print()

    active_hosts = []

    def scan_ip(ip):
        result = subprocess.run(
            ["ping", "-n", "1", "-w", "500", str(ip)],
            stdout=subprocess.DEVNULL
        )

        if result.returncode == 0:
            active_hosts.append(ip)
            print(ip, "is UP")

    with ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(scan_ip, network.hosts())

    print()
    print("[*] Scan completed.")
    print(f"[*] Found {len(active_hosts)} active host(s).")

    return active_hosts


if __name__ == "__main__":
    network_input = input("Enter network (e.g. 192.168.1.0/24): ")

    try:
        network = ipaddress.ip_network(network_input)
    except ValueError:
        print("[!] Invalid network address.")
        exit()

    active_hosts = discover_hosts(network)