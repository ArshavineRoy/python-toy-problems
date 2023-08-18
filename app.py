import tkinter as tk
from datetime import datetime
from tkinter import messagebox


class App:
    def __init__(self, root):
        self.root = root

        self.root.geometry("800x500")
        self.root.title("Python Toy Problems")

        # 1. TIME CONVERTER GUI
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



        # Bind on_close method to main window closing to customize the closing event: 'Do you want to quit?' dialog box.
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)



    # LOGIC

    # Method for prompting user for confirmation on closing the main window
    def on_close(self):
        if messagebox.askyesno(title="", message="Do you want to quit this application?"):
            self.root.destroy()     # Destroy main window if yes is selected


    # 1. Time conversion logic
    def convert_time(self):
        try:
            time = self.time_entry.get()
            converted_time = self.time_converter(time)

            self.time_output_str.set(f'Time in 24-hour format: {converted_time}')
            
        except ValueError:
            self.time_output_str.set("Please use the correct time format.") # MESSAGE BOX


    def time_converter(self, time):

        parsed_time = datetime.strptime(time, '%I:%M %p')

        return parsed_time.strftime('%H:%M')



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()