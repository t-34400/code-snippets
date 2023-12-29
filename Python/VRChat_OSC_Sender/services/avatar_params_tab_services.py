from models.osc_sender_config import osc_sender_config

class AvatarParamsTabServices:
    def __init__(self, sender, address_var, value_var):
        self.sender = sender
        self.address_var = address_var
        self.value_var = value_var
        osc_sender_config.generate_variables_if_needed()

    def send_avatar_params(self):
        address = self.address_var.get()
        value = self.value_var.get()

        self.sender.send(address, [value])