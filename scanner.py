import socket
from pathlib import Path
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

target = "127.0.0.1"
default_ports = [80, 443, 135]


def get_ports():
    while True:
        ports_text = input(
            "Enter localhost ports separated by commas, or press Enter for defaults: "
        ).strip()

        if not ports_text:
            return default_ports

        try:
            ports = []

            for item in ports_text.split(","):
                item = item.strip()

                if "-" in item:
                    start_text, end_text = item.split("-", 1)
                    start_port = int(start_text.strip())
                    end_port = int(end_text.strip())

                    if start_port > end_port:
                        raise ValueError

                    ports.extend(range(start_port, end_port + 1))
                else:
                    ports.append(int(item))

        except ValueError:
            print("Use port numbers or ranges, for example: 80,443,130-135")
            continue

        if all(1 <= port <= 65535 for port in ports):
            return ports

        print("Port numbers must be between 1 and 65535.")


ports = get_ports()

def scan_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scanner:
        scanner.settimeout(1)
        result = scanner.connect_ex((target, port))

    try:
        service = socket.getservbyport(port, "tcp")
    except OSError:
        service = "Unknown service"

    if result == 0:
        return f"Port {port} ({service}) is open"
    else:
        return f"Port {port} ({service}) is closed"


scan_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

start_time = datetime.now()

results = [
    f"Scan time: {scan_time}",
    f"Target: {target}",
    ""
]

with ThreadPoolExecutor(max_workers=min(10, len(ports))) as executor:
    messages = executor.map(scan_port, ports)

for message in messages:
    print(message)
    results.append(message)

elapsed = (datetime.now() - start_time).total_seconds()
summary = f"Scan completed in {elapsed:.2f} seconds"

print(summary)
results.extend(["", summary])

results_file = Path(__file__).with_name("scan_results.txt")
results_file.write_text("\n".join(results), encoding="utf-8")

print(f"Results saved to: {results_file}")