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
        self.sender_group.pack(padx=10, pady=10, fill="both", expand=True)

        self.sender_param_frame = tk.Frame(self.sender_group)
        self.sender_param_frame.pack()

        self.address_label = tk.Label(self.sender_param_frame, text="Address:")
        self.address_label.grid(row=0, column=0)

        self.address_entry = tk.Entry(self.sender_param_frame, textvariable=self.address_var, width=40)
        self.address_entry.grid(row=0, column=1, columnspan=2)

        self.value_label = tk.Label(self.sender_param_frame, text="Value:")
        self.value_label.grid(row=1, column=0)

        self.dropdown = ttk.Combobox(self.sender_param_frame, values=types, textvariable=self.selected_type_var, width=10)
        self.dropdown.grid(row=1, column=1)

        self.value_entry = tk.Entry(self.sender_param_frame, textvariable=self.value_var)
        self.value_entry.grid(row=1, column=2)
        
        self.send_button = tk.Button(self.sender_group, text="Send avatar parameter", command=self.services.send_avatar_params)
        self.send_button.pack(side=tk.TOP, pady=10)
