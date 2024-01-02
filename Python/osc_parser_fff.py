import struct

def decode(bytes):
    null_index = bytes.find(b'\x00')
    if null_index != -1:
        address_pattern_bytes = bytes[:null_index]
        address_pattern = address_pattern_bytes.decode('ascii')
        print(address_pattern)
        consumed_size = null_index + 4 & ~3
    else:
        return

    remaining = bytes[consumed_size:]
    print(remaining)
    null_index = remaining.find(b'\x00')
    print(null_index)
    if null_index != -1:
        type_tags_pattern_bytes = remaining[:null_index]
        type_tags_pattern = type_tags_pattern_bytes.decode('ascii')
        print(type_tags_pattern)
        print(consumed_size, null_index)
        consumed_size = (consumed_size + null_index) + 4 & ~3
        print(consumed_size)
    else:
        return
    
    remaining = bytes[consumed_size:]
    print(remaining)
    print(struct.unpack('>f', remaining[0:4]), struct.unpack('>f', remaining[4:8]), struct.unpack('>f', remaining[8:12]))
    print(remaining[12:])

file_path = "received_message_6.bin"

with open(file_path, "rb") as file:
    bytes = file.read()

print(bytes)
decode(bytes)

