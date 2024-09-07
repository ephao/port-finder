import socket

def is_port_in_use(port, host='localhost'):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind((host, port))
            return False
        except socket.error:
            return True

def find_unused_ports(start_port, end_port, host='localhost'):
    unused_ports = []
    for port in range(start_port, end_port + 1):
        if not is_port_in_use(port, host):
            unused_ports.append(port)
    return unused_ports
