from tkinter import ttk
from .avatar_params_tab import AvatarParamsTab
from .input_controller_tab import InputControllerTab
from .osc_config_tab import OSCConfigTab

class App:
    def __init__(self, root, sender):
        self.root = root
        self.root.title("VRChat OSC Sender")

        self.notebook = ttk.Notebook(root)

        self.avatar_params_frame = ttk.Frame(self.notebook)
        AvatarParamsTab(self.avatar_params_frame, sender)
        self.notebook.add(self.avatar_params_frame, text="Avatar params")

        self.input_controller_frame = ttk.Frame(self.notebook)
        InputControllerTab(self.input_controller_frame, sender)
        self.notebook.add(self.input_controller_frame, text="Input Controller")

        self.osc_config_frame = ttk.Frame(self.notebook)
        OSCConfigTab(self.osc_config_frame)
        self.notebook.add(self.osc_config_frame, text="OSC config")

        self.notebook.pack(padx=10, pady=10)
