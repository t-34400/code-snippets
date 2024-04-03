import cv2
import socket
import argparse
from multiprocessing import Process
from tqdm import tqdm

def main(host, port):
    s_input = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_input.connect((host, port))

    print("Device: ", s_input.recv(64).decode('utf-8'))
    print("Width? ", int.from_bytes(s_input.recv(2), "big"))
    print("Height? ", int.from_bytes(s_input.recv(2), "big"))

    s_output = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_output.bind(('127.0.0.1', 27184))
    s_output.listen(1)

    p = Process(target=client)
    p.start()

    out_conn, addr = s_output.accept()

    while True:
        out_conn.send(s_input.recv(1))
    p.join()
    

def client():
    cap = cv2.VideoCapture("tcp://127.0.0.1:27184")
    print(cap)

    for _ in tqdm(range(1000)):
        r, img = cap.read()
        if not r:
            continue
        cv2.imshow("", img)
        cv2.waitKey(20)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Decode and render H264 data from a socket.")
    parser.add_argument("--host", type=str, default="127.0.0.1", help="Host IP address")
    parser.add_argument("--port", type=int, default=12345, help="Port number")
    args = parser.parse_args()

    main(args.host, args.port)
    client()
