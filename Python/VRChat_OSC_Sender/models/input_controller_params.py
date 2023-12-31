import tkinter as tk

class InputControllerParams:
    axes = [
        "Vertical",
        "Horizontal",
        "LookHorizontal",
        "UseAxisRight",
        "GrabAxisRight",
        "MoveHoldFB",
        "SpinHoldCwCcw",
        "SpinHoldUD",
        "SpinHoldLR",
    ]

    buttons = [
        "MoveForward",
        "MoveBackward",
        "MoveLeft",
        "MoveRight",
        "LookLeft",
        "LookRight",
        "Jump",
        "Run",
        "ComfortLeft",
        "ComfortRight",
        "DropRight",
        "UseRight",
        "GrabRight",
        "DropLeft",
        "UseLeft",
        "GrabLeft",
        "PanicButton",
        "QuickMenuToggleLeft",
        "QuickMenuToggleRight",
        "Voice"
    ]

    def __init__(self):
        self.axis_vars = {}
        for axis in self.axes:
            self.axis_vars[axis] = tk.DoubleVar()
        
        self.button_vars = {}
        for button in self.buttons:
            self.button_vars[button] = tk.BooleanVar()
        
        self.chat_text_var = tk.StringVar()
        self.keyboard_bypass_var = tk.BooleanVar()