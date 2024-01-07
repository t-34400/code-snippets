import sys
import argparse
import socket
import struct


def parse_arguments():
    parser = argparse.ArgumentParser(description="UDP Server")
    parser.add_argument("--port", type=int, default=5005, help="Port to use")
    parser.add_argument('--data', required=True, nargs="*", type=float) 
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_arguments()

    UDP_IP = "127.0.0.1"
    UDP_PORT = args.port

    data_to_send = args.data
    data_to_send = struct.pack('<%sf' % len(data_to_send), *data_to_send)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(data_to_send, (UDP_IP, UDP_PORT))
