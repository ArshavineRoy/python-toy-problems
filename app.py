#!/usr/bin/env python3
import tkinter as tk
from datetime import datetime
from tkinter import messagebox
import re


class App:
    def __init__(self, root):
        self.root = root

        self.root.geometry("800x750")
        self.root.title("Python Toy Problems")

        # 1. TIME CONVERTER GUI
        self.label = tk.Label(self.root, text="Time Converter", font=('Arial', 14, "bold"))
        self.label.pack(padx=10,pady=(30, 10))

        self.description = tk.Label(self.root, text="A time converter that seamlessly converts time from 12-hour format to 24-hour format. \n Please enter time in 12-hour format below, e.g., 12:08 am", font=('Arial', 11))
        self.description.pack()

            # input field & button frame
        self.input_frame = tk.Frame(self.root)

            # input field & state management
        self.time_entry = tk.StringVar() # stores and updates str values, more like useState in React. 

        self.user_entry = tk.Entry(self.input_frame, font=('Arial', 16), textvariable=self.time_entry) # Connect to Entry widget to state manager, self.time_entry, via textvariable
        self.user_entry.pack(side='left', padx=10, pady=10)

            # convert time button
        self.convert_time_button = tk.Button(self.input_frame, text="Convert Time", bg='#a3e635', activebackground='#e879f9', command=self.convert_time) #command=self.show_message -- for displaying messages
        self.convert_time_button.pack(side='left', pady=10)

        self.input_frame.pack()

            # Output
            # labels can have their own variables
        self.time_output_str = tk.StringVar() # store & update the result of the time conversion 
        
        self.time_output = tk.Label(self.root, text="12:08", font=('Arial', 12, 'bold'), fg='red', textvariable=self.time_output_str)
        self.time_output.pack(pady=(20, 0))


        # 2.  Positive Number Checker
        self.label = tk.Label(self.root, text="Two Positives Checker", font=('Arial', 14, "bold"))
        self.label.pack(padx=10, pady=(20, 10))

        self.positives_description = tk.Label(self.root, text="An algorithm that compares three integers a, b, and c and returns True \n if exactly two of them are positive numbers, and False otherwise. \n Enter three integers below.", font=('Arial', 11))
        self.positives_description.pack(pady=2)

            # Positives labels and entry fields
        self.positives_frame = tk.Frame(self.root)
        self.positives_frame.rowconfigure(0, weight=1)
        self.positives_frame.rowconfigure(1, weight=1)
        self.positives_frame.rowconfigure(2, weight=1)

        self.input_a = tk.StringVar()
        self.label1 = tk.Label(self.positives_frame, text="a:", font=('Arial', 16))
        self.entry1 = tk.Entry(self.positives_frame, font=('Arial', 16), width=8, textvariable=self.input_a)
        self.label1.grid(row=0, column=0, pady=4)
        self.entry1.grid(row=0, column=1, pady=4, padx=3)
        

        self.input_b = tk.StringVar()
        self.label2 = tk.Label(self.positives_frame, text="b:", font=('Arial', 16))
        self.entry2 = tk.Entry(self.positives_frame, font=('Arial', 16), width=8, textvariable=self.input_b)
        self.label2.grid(row=1, column=0, pady=4)
        self.entry2.grid(row=1, column=1, pady=4, padx=3)
        
        self.input_c = tk.StringVar()
        self.label3 = tk.Label(self.positives_frame, text="c:", font=('Arial', 16))
        self.entry3 = tk.Entry(self.positives_frame, font=('Arial', 16), width=8, textvariable=self.input_c)
        self.label3.grid(row=2, column=0, pady=4)
        self.entry3.grid(row=2, column=1, pady=4, padx=3)


        self.positives_frame.pack()

            # Positives Output
        self.bool_output_state = tk.StringVar() # store & update the result 
        
        self.bool_output = tk.Label(self.root, text='True', font=('Arial', 12, 'bold'), fg='blue', textvariable=self.bool_output_state)
        self.bool_output.pack(pady=4)

            # Two Positives Button
        self.button = tk.Button(self.root, text="Exactly Two Positives?", bg='#a3e635', activebackground='#e879f9', command=self.positive_numbers)
        self.button.pack(pady=(2, 5))


        # 3. HIGHEST CONSONANT VALUE GUI
        self.label = tk.Label(self.root, text="Highest Consonant Value", font=('Arial', 14, "bold"))
        self.label.pack(padx=10,pady=(30, 10))

        self.consonants_description = tk.Label(self.root, text="Easily get the highest value of consonant substrings. Consonants are any letters of the alphabet except 'aeiou'. \n For example, in the word 'strength', the consonant substrings 'str' = 19 + 20 + 18 = 57 \n and 'ngth'= 14 + 7 + 20 + 8 = 49. The highest is 57.", font=('Arial', 11))
        self.consonants_description.pack()

            # Consonants input field + button
        self.consonants_input_frame = tk.Frame(self.root)

            # input field & button frame
        self.consonant_frame = tk.Frame(self.root)

            # input field & state management
        self.string_entry_state = tk.StringVar() # stores and updates str values, more like useState in React. 

        self.string_entry = tk.Entry(self.consonant_frame, font=('Arial', 16), textvariable=self.string_entry_state) 
        self.string_entry.pack(side='left', padx=10, pady=10)

            # Consonant button
        self.consonant_button = tk.Button(self.consonant_frame, text="Calculate Value", bg='#a3e635', activebackground='#e879f9', command=self.highest_consonant)
        self.consonant_button.pack(side='left', pady=10)

        self.consonant_frame.pack()

            # Consonant Output
        self.consonant_output_str = tk.StringVar() # store & update the result of the time conversion 
        
        self.consonant_output = tk.Label(self.root, text="12:08", font=('Arial', 12, 'bold'), fg='red', textvariable=self.consonant_output_str)
        self.consonant_output.pack(pady=(20, 0))


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


    # 2. Two positives logic

    def positive_numbers(self):
        try:
            a = int(self.input_a.get())
            b = int(self.input_b.get())
            c = int(self.input_c.get())
            
            result = self.calculate_positives(a, b, c)
            self.bool_output_state.set(result)

        except ValueError:
            self.bool_output_state.set("Please enter integer values only!")
    
    def calculate_positives(self, a, b, c):
        matches = [num for num in [a, b, c]  if num > 0]
        return 'True' if len(matches) == 2 else 'False'
    
    # 3. Highest consonant value logic

    def highest_consonant(self):
        string = self.string_entry_state.get()
        self.calculate_value(string)

    def calculate_value(self, string):
        try:
            if string:
                substrings = re.findall(r"[^aeiou\d\W]+", string.lower())

                substring_totals = []

                for substring in substrings:
                    total_unicode = 0
                    for char in substring:
                        total_unicode += (ord(char) - 96)
                    substring_totals.append(total_unicode)

                highest_value = max(substring_totals)

                self.consonant_output_str.set(f'The highest consonant substring value in your entry is {highest_value}')

            else:
                self.consonant_output_str.set("Oops! You entered an empty string!")
        except ValueError:
            self.consonant_output_str.set("You must enter a string!")
        


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()