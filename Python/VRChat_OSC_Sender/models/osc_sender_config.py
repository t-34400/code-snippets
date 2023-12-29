import tkinter as tk

class OSCSenderConfig:
    remote_ip_var = None
    remote_port_var = None

    def get_remote_ip(self):
        if self.remote_ip_var is None:
            return "127.0.0.1"
        return self.remote_ip_var.get()
    
    def get_remote_port(self):
        if self.remote_port_var is None:
            return 9000
        return self.remote_port_var.get()
    
    def generate_variables_if_needed(self):
        if self.remote_ip_var is None:
            self.remote_ip_var = tk.StringVar()
            self.remote_ip_var.set("127.0.0.1")
        if self.remote_port_var is None:
            self.remote_port_var = tk.IntVar()
            self.remote_port_var.set(9000)


osc_sender_config = OSCSenderConfig()