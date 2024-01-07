import asyncio

class EchoServerProtocol:
    _protocol = None

    def __init__(self):
        self.file_base_path = "received_message"
        self.id = 0

    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        self.id += 1

        file_path = f"{self.file_base_path}_{self.id}.bin"
        with open(file_path, "wb") as file:
            file.write(data)
            print(f"Received message {self.id}, saved to {file_path}")

    def connection_lost(self, _):
        print("Connection lost.")

async def main():
    loop = asyncio.get_event_loop()

    transport, _ = await loop.create_datagram_endpoint(
        lambda: EchoServerProtocol(),
        local_addr=('127.0.0.1', 12351))

    try:
        await asyncio.sleep(3600)
    finally:
        transport.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
