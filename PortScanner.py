import socket

print("Created by ArdaZortlatan. Only for education.")
target = input("Enter IP address or domain name: ")
port_range = range(1, 65536)
print("Scanning please wait.")

open_ports = []

try:
    ip = socket.gethostbyname(target)
    print(f"Target IP: {ip}\n")

    for port in port_range:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.001)

        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
            print(f"Port {port} is open")

        sock.close()

    if len(open_ports) == 0:
        print("No open ports found.")
    else:
        print("Port scan completed.")

    input("Press Enter to exit...")

except socket.gaierror:
    print("Invalid IP address or domain name.")
    input("Press Enter to exit...")
