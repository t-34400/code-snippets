import tkinter as tk
from tkinter import ttk
from models.osc_sender_config import osc_sender_config

class OSCConfigTab:
    def __init__(self, root):
        self.root = root
        osc_sender_config.generate_variables_if_needed()
        self.remote_ip_var = osc_sender_config.remote_ip_var
        self.remote_port_var = osc_sender_config.remote_port_var

        self.remote_ip_label = tk.Label(self.root, text="Remote IP address:", anchor="w")
        self.remote_ip_label.pack(pady=5)

        self.remote_ip_entry = tk.Entry(self.root, textvariable=self.remote_ip_var, width=40)
        self.remote_ip_entry.pack()

        self.remote_port_label = tk.Label(self.root, text="Remote port:", anchor=tk.W)
        self.remote_port_label.pack(pady=5)

        self.remote_port_entry = tk.Entry(self.root, textvariable=self.remote_port_var, width=40)
        self.remote_port_entry.pack()
