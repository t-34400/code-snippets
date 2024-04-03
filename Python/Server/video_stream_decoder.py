import cv2
import socket
import numpy as np
import time
import argparse
import struct

def main(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    sock.settimeout(5)

    while True:
        try:
            size_bytes = sock.recv(4)
            if len(size_bytes) < 4:
                break

            size = struct.unpack('>i', size_bytes)[0]
            print('size = ', size)
            
            received_bytes = b''
            while len(received_bytes) < size:
                data = sock.recv(size - len(received_bytes))
                if not data:
                    break

                received_bytes += data
                print('data len = ', len(data))

            frame = cv2.imdecode(np.frombuffer(data, dtype=np.uint8), cv2.IMREAD_UNCHANGED)

            if frame:
                cv2.imshow('Frame', frame)

            if cv2.waitKey(1) & 0xFF == 27:
                break

        except socket.timeout:
            time.sleep(1)

    sock.close()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Decode and render H264 data from a socket.")
    parser.add_argument("--host", type=str, default="127.0.0.1", help="Host IP address")
    parser.add_argument("--port", type=int, default=12345, help="Port number")
    args = parser.parse_args()

    main(args.host, args.port)
