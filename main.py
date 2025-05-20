import tkinter as tk
from gui import Event_Organizer_App


def main():
    root = tk.Tk()
    app = Event_Organizer_App(root)
    app.style.configure("Green.TButton", foreground="white", background="#4CAF50")
    root.mainloop()


if __name__ == "__main__":
    main()
