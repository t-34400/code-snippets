class InputControllerTabServices:
    axis_address_prefix = "/input/"
    button_address_prefix = "/input/"

    def __init__(self, sender):
        self.sender = sender

    def send_axis_value(self, axis, value):
        address = self.axis_address_prefix + axis
        self.sender.send(address, [value])

    def send_button_value(self, button, value):
        address = self.button_address_prefix + button
        self.sender.send(address, [value])
