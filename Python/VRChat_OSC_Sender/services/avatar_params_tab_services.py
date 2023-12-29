from models.osc_sender_config import osc_sender_config

class AvatarParamsTabServices:
    def __init__(self, sender, address_var, selected_type_var, value_var):
        self.sender = sender
        self.address_var = address_var
        self.selected_type_var = selected_type_var
        self.value_var = value_var
        osc_sender_config.generate_variables_if_needed()

    def send_avatar_params(self):
        address = self.address_var.get()
        type = self.selected_type_var.get()
        value_string = self.value_var.get()

        value = AvatarParamsTabServices.try_parse(type, value_string)
        if value is not None:
            self.sender.send(address, [value])

    def try_parse(type, value_string):
        try:
            if type == "Int":
                return int(value_string)
            elif type == "Float":
                return float(value_string)
            elif type == "Bool":
                return bool(value_string)
            else:
                print(f"Failed to parse value string. Unknown value type: {type}")
                return None
        except:
            print("Failed to parse value string. Invalid value string")
            return None