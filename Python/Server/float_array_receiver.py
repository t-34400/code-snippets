import socket
import argparse
from datetime import datetime

def parse_arguments():
    parser = argparse.ArgumentParser(description="UDP Server")
    parser.add_argument("--port", type=int, default=5005, help="Port to use")
    return parser.parse_args()

def generate_filename():
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    return f"{timestamp}.bin"

def main():
    args = parse_arguments()

    udp_ip = "127.0.0.1"
    udp_port = args.port

    filename = generate_filename()

    recvSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    recvSocket.bind((udp_ip, udp_port))
    recvSocket.settimeout(1)

    print(f"UDP server started on {udp_ip}:{udp_port}.")

    received_data_count = 0

    try:
        while True:
            try:
                print(f"\rFilename: {filename}, Received {received_data_count} data.", end="", flush=True)

                data, _ = recvSocket.recvfrom(1024)

                # After completing the data measurement, the measurement application periodically send an empty byte.
                if len(data) == 0: 
                    filename = generate_filename()
                    if received_data_count != 0:
                        print('')
                        received_data_count = 0
                    continue

                with open(filename, "ab") as file:
                    file.write(data)

                received_data_count += 1

            except TimeoutError:
                pass

    except KeyboardInterrupt:
        if received_data_count == 0:
            print('\r', end="")
        else:
            print()
        print("KeyboardInterrupt detected. Stopping the UDP server.")
    finally:
        recvSocket.close()


    """ 保存したデータの読み込みサンプル
    import sys
    import numpy as np

    with open(filename, 'rb') as file:
        data = np.frombuffer(file.read(), dtype=np.float32)
        if sys.byteorder == 'big':
            data = data.byteswap()

        data.reshape(-1, 71)

        print(data)
    """

if __name__ == "__main__":
    main()
