from tkinter import ttk
from .avatar_params_tab import AvatarParamsTab

class App:
    def __init__(self, root, sender):
        self.root = root
        self.root.title("VRChat OSC Sender")

        self.notebook = ttk.Notebook(root)

        self.avatar_params_frame = ttk.Frame(self.notebook)
        AvatarParamsTab(self.avatar_params_frame, sender)
        self.notebook.add(self.avatar_params_frame, text="Tab 1")

        self.notebook.pack(padx=10, pady=10)
