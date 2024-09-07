import argparse
from port_utils import find_unused_ports
import config

def main():
    parser = argparse.ArgumentParser(description="Find unused ports within a specified range.")
    parser.add_argument("start", type=int, help="Start of port range")
    parser.add_argument("end", type=int, help="End of port range")
    parser.add_argument("--host", default=config.DEFAULT_HOST, help=f"Host to check (default: {config.DEFAULT_HOST})")
    args = parser.parse_args()

    unused_ports = find_unused_ports(args.start, args.end, args.host)
    
    if unused_ports:
        print(f"Unused ports between {args.start} and {args.end} on {args.host}:")
        for port in unused_ports:
            print(port)
    else:
        print(f"No unused ports found between {args.start} and {args.end} on {args.host}")

if __name__ == "__main__":
    main()
