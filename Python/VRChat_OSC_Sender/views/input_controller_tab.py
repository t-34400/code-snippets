import tkinter as tk
from tkinter import ttk
from models.input_controller_params import InputControllerParams

class InputControllerTab:
    def __init__(self, root, sender):
        self.input_controller_params = InputControllerParams()
        # self.services = 

        self.axes_group = ttk.LabelFrame(root, text="Axes")
        self.axes_group.pack(padx=10, pady=10, fill="both", expand=True, anchor=tk.W)

        for index, axis in enumerate(self.input_controller_params.axes):
            label = tk.Label(self.axes_group, text=axis, anchor=tk.W)
            label.grid(row=index, column=0, sticky="e", padx=5, pady=5)

            variable = self.input_controller_params.axis_vars[axis]
            # variable.trace_add("write", lambda *args: on_var_change(variable))
            
            scale = tk.Scale(self.axes_group, from_=-1.0, to=1.0, variable=variable, orient="horizontal", length=200, resolution=0.05)
            scale.grid(row=index, column=1, sticky="e", padx=5, pady=0)

            scale = tk.Entry(self.axes_group, textvariable=variable)
            scale.grid(row=index, column=2, sticky="e", padx=5, pady=0)
        