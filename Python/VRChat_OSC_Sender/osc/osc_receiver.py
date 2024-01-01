from pythonosc.osc_server import BlockingOSCUDPServer
from pythonosc.dispatcher import Dispatcher
import threading


class OSCReceiver:
    server_lock = threading.Lock()
    server = None

    def __init__(self, config):
        self.config = config

        self.dispatcher = Dispatcher()
        self.dispatcher.set_default_handler(self.osc_callback)

        self.run_server()
        self.config.register_config_change_callback(self.run_server)


    def run_server(self):
        thread = threading.Thread(target=self.run_server_async)
        thread.start()

    def run_server_async(self):
        local_ip, local_port = self.config.get_local_ip_and_port()

        self.server_lock.acquire()

        if self.server is not None:
            self.server.shutdown()
        server = BlockingOSCUDPServer((local_ip, local_port), self.dispatcher)
        self.server = server

        self.server_lock.release()

        print(f"Listening for OSC messages on {local_ip}:{local_port}")

        server.serve_forever()

        print(f"OSC server shutting down. {local_ip}:{local_port}")


    def close(self):
        self.server_lock.acquire()

        if self.server is not None:
            self.server.shutdown()
            self.server = None

        self.server_lock.release()


    def osc_callback(address, *args):
        print(f"Receive: {address}, {args}")

