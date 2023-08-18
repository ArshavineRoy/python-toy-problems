import tkinter as tk


class App:
    def __init__(self, root):
        self.root = root

        self.root.geometry("800x500")
        self.root.title("Python Toy Problems")

                # 1. 24-HOUR TIME CONVERTER
        self.label = tk.Label(self.root, text="Time Converter", font=('Arial', 14, "bold"))
        self.label.pack(padx=10,pady=10)

        self.description = tk.Label(self.root, text="A time converter that seamlessly converts time from 12-hour format to 24-hour format. \n Please enter time in 12-hour format below, e.g., 12:08 am", font=('Arial', 11))
        self.description.pack()



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()