import tkinter as tk


class App:
    def __init__(self, root):
        self.root = root

        self.root.geometry("800x500")
        self.root.title("Python Toy Problems")

        # 1. TIME CONVERTER
        self.label = tk.Label(self.root, text="Time Converter", font=('Arial', 14, "bold"))
        self.label.pack(padx=10,pady=10)

        self.description = tk.Label(self.root, text="A time converter that seamlessly converts time from 12-hour format to 24-hour format. \n Please enter time in 12-hour format below, e.g., 12:08 am", font=('Arial', 11))
        self.description.pack()

            # input field & button frame
        self.input_frame = tk.Frame(self.root)

            # input field & state management
        self.time_entry = tk.StringVar() # stores and updates str values, more like useState in React. 

        self.user_entry = tk.Entry(self.input_frame, font=('Arial', 12), textvariable=self.time_entry) # Connect to Entry widget to state manager, self.time_entry, via textvariable
        self.user_entry.pack(side='left', padx=10, pady=10)

            # convert time button
        self.convert_time_button = tk.Button(self.input_frame, text="Convert Time", command=self.convert_time) #command=self.show_message -- for displaying messages
        self.convert_time_button.pack(side='left', pady=10)

        self.input_frame.pack()

            # Output
            # labels can have their own variables
        self.time_output_str = tk.StringVar() # store & update the result of the time conversion 
        
        self.time_output = tk.Label(self.root, text="12:08", font=('Arial', 12, 'bold'), fg='red', textvariable=self.time_output_str)
        self.time_output.pack()





if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()