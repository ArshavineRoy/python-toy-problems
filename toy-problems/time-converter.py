from datetime import datetime

def time_converter(time):

    parsed_time = datetime.strptime(time, '%I:%M %p')

    return parsed_time.strftime('%H%M')
try:
    converted_time = time_converter(input("Enter time to be converted: "))
    
    print(converted_time)
except ValueError:
    print("Please use the format hh:mm am or pm. Example: 12:08 am")