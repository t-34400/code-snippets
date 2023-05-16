import serial

PORT_NAME = 'COM1'
BAUD_RATE = 9600
TIMEOUT_SEC = 1

with serial.Serial(PORT_NAME, BAUD_RATE, TIMEOUT_SEC) as ser:
    while True:
        data = ser.readline()
        if data:
            print(data)
