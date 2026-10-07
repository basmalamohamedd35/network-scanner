# Python Network Scanner

A simple Python-based TCP network scanner designed for learning network enumeration, socket programming, and basic cybersecurity concepts in local or lab environments.

## Features

* Network input validation
* Active host discovery using ICMP ping
* Concurrent host scanning using `ThreadPoolExecutor`
* TCP port scanning
* User-defined port ranges
* Port input validation and duplicate removal
* Basic service identification for common ports
* Scan time tracking
* Active host summary
* Open port results
* Automatic scan report generation

## Project Structure

```text
network-scanner/
├── scanner.py
├── port-scanner.py
├── scan_results.txt
└── README.md
```

## How It Works

The scanner follows these steps:

```text
Network Input
      ↓
Network Validation
      ↓
Host Discovery
      ↓
Active Hosts
      ↓
Port Input
      ↓
TCP Port Scanning
      ↓
Basic Service Identification
      ↓
Result Collection
      ↓
Scan Report
```

## Requirements

* Python 3.x
* Windows operating system
* A local network or authorized lab environment

The project uses Python standard-library modules, so no external packages are required.

## Usage

Run the scanner from the project directory:

```bash
python port-scanner.py 192.168.1.0/24 22,80,443
```

### Arguments

**Network**

The target network to scan.

Example:

```text
192.168.1.0/24
```

**Ports**

A comma-separated list of TCP ports to scan.

Example:

```text
22,80,443
```

## Example Output

```text
[*] Scanning 192.168.1.0/24...

192.168.1.1 is UP
192.168.1.8 is UP
192.168.1.14 is UP

[*] Scan completed.
[*] Found 3 active host(s).

[*] Scanning ports on 192.168.1.1...
  80/tcp OPEN (HTTP)
  443/tcp OPEN (HTTPS)

[*] Scanning ports on 192.168.1.8...
  No open ports found.
```

## Scan Report

The scanner automatically saves the results to:

```text
scan_results.txt
```

Example:

```text
========================================
Network Scan Report
========================================
Network: 192.168.1.0/24
Scan Time: 2026-10-07 17:32:41
Active Hosts: 3
Ports Requested: 3

Host Summary:
----------------------------------------
192.168.1.1 - 2 open port(s)
192.168.1.8 - 0 open port(s)
192.168.1.14 - 0 open port(s)

Open Ports:
----------------------------------------
192.168.1.1:80/tcp OPEN (HTTP)
192.168.1.1:443/tcp OPEN (HTTPS)
```

## Technologies & Concepts

This project was built to practice:

* Python
* `socket`
* TCP/IP
* IP addressing
* Network discovery
* Port scanning
* ICMP ping
* TCP connections
* Concurrency
* `ThreadPoolExecutor`
* Input validation
* File handling
* `argparse`
* Basic service identification
* Security enumeration concepts

## Limitations

This is a learning-focused network scanner and does not attempt to replace professional tools such as Nmap.

Current limitations include:

* ICMP-based host discovery
* TCP connect scanning
* Basic service identification based on port numbers
* No service/version fingerprinting
* No UDP scanning
* No operating-system detection
* No vulnerability detection

## Security Notice

This project is intended for **your own devices, networks, and authorized laboratory environments**.

Do not scan networks or systems without permission.

## Learning Purpose

The project was developed as part of a cybersecurity self-study journey to understand how network enumeration and TCP port scanning work at the programming level.
