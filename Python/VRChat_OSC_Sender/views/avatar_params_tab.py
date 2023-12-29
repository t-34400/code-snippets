import tkinter as tk
from tkinter import ttk
from services.avatar_params_tab_services import AvatarParamsTabServices

class AvatarParamsTab:
    def __init__(self, root, sender):
        self.address_var = tk.StringVar()
        self.value_var = tk.StringVar()
        self.services = AvatarParamsTabServices(sender, self.address_var, self.value_var)

        self.sender_group = ttk.LabelFrame(root, text="Avatar Parameter Sender")
        self.sender_group.pack(padx=10, pady=10, fill="both", expand=True)

        self.address_label = tk.Label(self.sender_group, text="Address:", anchor="w")
        self.address_label.pack(pady=5)

        self.address_entry = tk.Entry(self.sender_group, textvariable=self.address_var)
        self.address_entry.pack()

        self.value_label = tk.Label(self.sender_group, text="Value:", anchor=tk.W)
        self.value_label.pack(pady=5)

        self.value_entry = tk.Entry(self.sender_group, textvariable=self.value_var)
        self.value_entry.pack()

        self.send_button = tk.Button(self.sender_group, text="Send avatar parameter", command=self.services.send_avatar_params)
        self.send_button.pack(pady=10)