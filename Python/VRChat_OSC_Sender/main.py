import tkinter as tk
from views.app import App
from osc.osc_sender import OSCSender


if __name__ == "__main__":
    root = tk.Tk()
    sender = OSCSender()

    app = App(root, sender)
    root.mainloop()

