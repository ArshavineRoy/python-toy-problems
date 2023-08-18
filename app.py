import tkinter as tk


class App:
    def __init__(self, root):
        self.root = root

        self.root.geometry("800x500")
        self.root.title("Python Toy Problems")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()