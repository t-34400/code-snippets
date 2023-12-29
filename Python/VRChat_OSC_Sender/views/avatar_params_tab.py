import tkinter as tk
from tkinter import ttk
from services.avatar_params_tab_services import AvatarParamsTabServices

class AvatarParamsTab:
    def __init__(self, root, sender):
        types = [ "Int", "Bool", "Float" ]

        self.address_var = tk.StringVar()
        self.address_var.set("/avatar/parameters/VelocityZ")
        self.selected_type_var = tk.StringVar()
        self.selected_type_var.set(types[0])
        self.value_var = tk.StringVar()
        self.value_var.set("0")

        self.services = AvatarParamsTabServices(sender, self.address_var, self.selected_type_var, self.value_var)

        self.sender_group = ttk.LabelFrame(root, text="Avatar Parameter Sender")
        self.sender_group.pack(padx=10, pady=10, fill="both", expand=True, anchor=tk.W)

        self.address_label = tk.Label(self.sender_group, text="Address:", anchor="w")
        self.address_label.pack(pady=5)

        self.address_entry = tk.Entry(self.sender_group, textvariable=self.address_var, width=40)
        self.address_entry.pack(padx=5)

        self.value_label = tk.Label(self.sender_group, text="Value:")
        self.value_label.pack(pady=5)

        self.input_frame = tk.Frame(self.sender_group)
        self.input_frame.pack(anchor=tk.W, fill=tk.X)
        
        self.dropdown = ttk.Combobox(self.input_frame, values=types, textvariable=self.selected_type_var, width=10)
        self.dropdown.pack(side=tk.LEFT, padx=5)

        self.value_entry = tk.Entry(self.input_frame, textvariable=self.value_var)
        self.value_entry.pack(fill=tk.X, side=tk.LEFT, padx=5)
        
        self.send_button = tk.Button(self.sender_group, text="Send avatar parameter", command=self.services.send_avatar_params)
        self.send_button.pack(side=tk.TOP, pady=10)
