import socket
from pathlib import Path
from datetime import datetime

target = "127.0.0.1"
ports = [80, 443, 135]


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

results = [
    f"Scan time: {scan_time}",
    f"Target: {target}",
    ""
]

for port in ports:
    message = scan_port(port)
    print(message)
    results.append(message)

results_file = Path(__file__).with_name("scan_results.txt")
results_file.write_text("\n".join(results), encoding="utf-8")

print(f"Results saved to: {results_file}")