#Author: Mario Ockersz
#Date: 21/12/2024
#Student ID: w2119866
import os
import csv
from collections import defaultdict
from datetime import datetime, timedelta
import calendar
import tkinter as tk
from tkinter import messagebox

# Task A: Input Validation
def validate_date_input():
    """
    Prompts the user for a date in DD MM YYYY format, validates the input.
    """
    while True:
        try:
            print("Current working directory:", os.getcwd())

            DD = int(input("Please enter the day of the survey in the format DD: "))
            if 1 <= DD <= 31:
                break
            else:
                print("Invalid day. Please enter a number between 1 and 31.")
        except ValueError:
            print("Invalid input. Please enter a number for the day.")

    while True:
        try:
            MM = int(input("Please enter the month of the survey in the format MM: "))
            if 1 <= MM <= 12:
                break
            else:
                print("Invalid month. Please enter a number between 1 and 12.")
        except ValueError:
            print("Invalid input. Please enter a number for the month.")

    while True:
        try:
            YYYY = int(input("Please enter the year of the survey in the format YYYY: "))
            if YYYY >= 2000:
                break
            else:
                print("Invalid year. Please enter a year greater than or equal to 2000.")
        except ValueError:
            print("Invalid input. Please enter a number for the year.")

    # Check for valid days in February and other months
    if MM == 2:
      # if the year divisable by 4
      # and divisable by 400 or diviable by 100 then its a leap year
        if YYYY % 4 == 0 and (YYYY % 100 != 0 or YYYY % 400 == 0):  # Leap year
            if DD > 29: # if its a leap year days greter than 29 will be rejected
                print(f"Invalid day for {calendar.month_name[MM]} in a leap year. Maximum is 29.")
                return validate_date_input()
        else:
            if DD > 28: # Then if its not a leap year dates more than 28 will be rejected
                print(f"Invalid day for {calendar.month_name[MM]} in a non-leap year. Maximum is 28.")
                return validate_date_input()
    elif MM in [4, 6, 9, 11]:  # 30-day months
        if DD > 30:
            print(f"Invalid day for {calendar.month_name[MM]}. Maximum is 30.")
            return validate_date_input()

    return DD, MM, YYYY

def validate_continue_input():
    """
    Prompts the user to decide whether to load another dataset.
    """
    while True:
        choice = input("Do you want to analyze another dataset? (Y/N): ").strip().upper()
        if choice in ['Y', 'N']:
            return choice == 'Y'
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

# Task B: Process CSV Data
def process_csv_data(file_path):
    """
    Processes the CSV data and extracts metrics.
    """
    outcomes = {
        "File Name": file_path,
        "The total number of vehicles recorded" : 0,
        "The total number of trucks recorded" : 0,
        "The total number of electric vehicles": 0,
        "The total number of two-wheeled vehicles": 0,
        "The total number of Busses leaving Elm Avenue/Rabbit Road heading North": 0,
        "The total number of Vehicles through both junctions not turning left or right": 0,
        "The percentage of total vehicles recorded that are trucks for this date(%)": 0,
        "The average number of Bikes per hour": 0,
        "The total number of Vehicles recorded as over the speed limit": 0,
        "The total number of vehicles recorded at Elm Avenue/Rabbit Road": 0,
        "The total number of vehicles recorded at Hanley Highway/Westway": 0,
        "Scooters percentage recorded through the Elm Avenue (%)": 0,
        "The highest number of vehicles in an hour on Hanley Highway/Westway": 0,
        "Peak Hour on Hanley Highway/Westway is between": "", # empty string for text
        "Total Hours of Rain on Selected Date": timedelta(), # Setting up as a timedelta object for duration
    }

    vehicles_per_hour_hanley = [0] * 24
    bikes_per_hour = [0] * 24
    traffic_data = []

    # Reading from the CSV file
    try:
        with open(file_path, mode='r') as file: #opening the csv file in read mode & (with) for automatic file close
            reader = csv.DictReader(file) # Reads the CSV file into dict formate
            reader.fieldnames = [header.strip() for header in reader.fieldnames] 
            headers = reader.fieldnames  # Get the headers of the CSV
            print(f"CSV Headers: {headers}")  # Printing the csv file headers for making sure file is not corrupted

            last_time = None # initializes a variable to keep track of the last timestamp

            sorted_rows = sorted(reader, key=lambda row: datetime.strptime(f"{row['Date']} {row['timeOfDay']}", "%d/%m/%Y %H:%M:%S"))
            

            for row in sorted_rows: # loop itrates over each row in the csv file
                try:
                    date_str = row['Date'] # extracts the date from the row
                    time_str = row['timeOfDay'] # extracts the time of day from the row
                    speed_limit = int(row['JunctionSpeedLimit']) # extracts and converts the speed limit to an integer
                    vehicle_type = row['VehicleType'] # extracts the vehicle type from the row.
                    vehicle_speed = int(row['VehicleSpeed']) # extracts and converts the vehicle speed to an integer
                    weather_conditions = row['Weather_Conditions'] # extracts the weather conditions from the row

                    outcomes["The total number of vehicles recorded"] += 1

                    if vehicle_type == "Truck":
                        outcomes["The total number of trucks recorded"] += 1

                    if row['elctricHybrid'] == "True":
                        outcomes["The total number of electric vehicles"] += 1

                    if vehicle_type in ["Motorcycle", "Scooter", "Bicycle"]:
                        outcomes["The total number of two-wheeled vehicles"] += 1

                    if row['JunctionName'] == "Elm Avenue/Rabbit Road" and row['travel_Direction_out'] == "N" and vehicle_type == "Buss":
                        outcomes["The total number of Busses leaving Elm Avenue/Rabbit Road heading North"] += 1

                    if row['travel_Direction_in'] == row['travel_Direction_out']:
                        outcomes["The total number of Vehicles through both junctions not turning left or right"] += 1

                    if vehicle_speed > speed_limit:
                        outcomes["The total number of Vehicles recorded as over the speed limit"] += 1

                    time_hour = datetime.strptime(f"{date_str} {time_str}", "%d/%m/%Y %H:%M:%S").hour
                    if row['JunctionName'] == "Hanley Highway/Westway":
                        vehicles_per_hour_hanley[time_hour] += 1 # if the above if statement is true then it will added to list

                    # Count bikes per hour
                    if vehicle_type == "Bicycle":
                        bikes_per_hour[time_hour] += 1 # if the above condition is true then it will be added to list

                    current_time = datetime.strptime(f"{date_str} {time_str}", "%d/%m/%Y %H:%M:%S")

                    if 'Rain' in weather_conditions:
                        if last_time is not None:
                            time_difference = current_time - last_time
                            outcomes["Total Hours of Rain on Selected Date"] += time_difference

                        last_time = current_time
                    else:
                        last_time = None

                    if row['JunctionName'] == "Elm Avenue/Rabbit Road":
                        outcomes["The total number of vehicles recorded at Elm Avenue/Rabbit Road"] += 1

                        if vehicle_type == "Scooter":
                            outcomes["Scooters percentage recorded through the Elm Avenue (%)"] += 1

                    elif row['JunctionName'] == "Hanley Highway/Westway":
                        outcomes["The total number of vehicles recorded at Hanley Highway/Westway"] += 1
                except KeyError as e: # to handle missing keys
                    print(f"KeyError: {e} not found in the row. Skipping this row.")
                    continue
                
            
            total_bikes = sum(bikes_per_hour)
            
            hours_with_bikes = sum(1 for count in bikes_per_hour)
            outcomes["The average number of Bikes per hour"] = round(total_bikes / hours_with_bikes if hours_with_bikes > 0 else 0)

            total_scooters = outcomes["Scooters percentage recorded through the Elm Avenue (%)"]
            total_vehicles_at_elm_avenue = outcomes["The total number of vehicles recorded at Elm Avenue/Rabbit Road"]
            if total_vehicles_at_elm_avenue > 0:
                outcomes["Scooters percentage recorded through the Elm Avenue (%)"] = (total_scooters * 100) // total_vehicles_at_elm_avenue
            else:
                outcomes["Scooters percentage recorded through the Elm Avenue (%)"] = 0
            
            if outcomes["The total number of vehicles recorded"] > 0:
                outcomes["The percentage of total vehicles recorded that are trucks for this date(%)"] = round((outcomes["The total number of trucks recorded"] * 100) / outcomes["The total number of vehicles recorded"])

            
            peak_hour_max_hanley = max(vehicles_per_hour_hanley, default=0) # finding the maximum and seting if empty list its 0
            peak_hours_hanley = [hour for hour, count in enumerate(vehicles_per_hour_hanley) if count == peak_hour_max_hanley]

            if peak_hours_hanley:
                outcomes["Peak Hour on Hanley Highway/Westway is between"] = ", ".join([f"Between {hour}:00 and {hour + 1}:00" for hour in peak_hours_hanley])
                outcomes["The highest number of vehicles in an hour on Hanley Highway/Westway"] = peak_hour_max_hanley
            
            outcomes["Total Hours of Rain on Selected Date"] = round(outcomes["Total Hours of Rain on Selected Date"].total_seconds() / 3600)
            
    except FileNotFoundError:
        print(f"File not found {file_path}")

    return outcomes, traffic_data

# Task C: Display Outcomes
def display_outcomes(outcomes):
    """
    Displays the processed outcomes.
    """
    print("\n--- Traffic Analysis Outcomes ---")
    for key, value in outcomes.items():
        print(f"{key}: {value}")

# Task D: Save Results to File
def save_results_to_file(outcomes, file_name="results.txt"):
    """
    Saves the processed outcomes to a text file.
    """
    with open(file_name, mode='a') as file:
        file.write("\n--- Traffic Analysis Outcomes ---\n")
        for key, value in outcomes.items():
            file.write(f"{key}: {value}\n")
        file.write("\n")

        
        
# Histogram Application
class HistogramApp:
    def __init__(self, traffic_data, selected_date):
        self.traffic_data = traffic_data # Stores the traffic data
        self.date = selected_date  # Stores the selected date for the histogram
        self.root = tk.Tk()     # Create the main Tkinter window
        self.canvas = None 
        self.scrollbar = None
        self.frame = None
        self.scroll_frame = None

    def setup_window(self): # Set up the main window with title and layout
        self.root.title(f"Traffic Histogram for {self.date}")
        
        # Create main frame
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        # Create frame for scroll region fro horizontal scrolling
        self.scroll_frame = tk.Frame(self.frame)
        self.scroll_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create canvas with scrollbar
        self.canvas = tk.Canvas(self.scroll_frame, width=1200, height=600)
        self.scrollbar = tk.Scrollbar(self.scroll_frame, orient=tk.HORIZONTAL, command=self.canvas.xview)
        self.canvas.configure(xscrollcommand=self.scrollbar.set)
        
        # Pack scrollbar and canvas
        self.scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        # Create exit button with styling
        self.exit_button = tk.Button(self.frame, text="Exit", command=self.root.destroy, 
                                   bg='red', fg='white', font=('Arial', 12))
        self.exit_button.pack(pady=10)
        
        # Bind mouse wheel to horizontal scroll
        self.canvas.bind('<MouseWheel>', self.on_mousewheel)
        self.canvas.bind('<Shift-MouseWheel>', self.on_shift_mousewheel)

        # Handle mouse wheel scrolling (vertical scrolling)
    def on_mousewheel(self, event):
        self.canvas.xview_scroll(int(-1 * (event.delta / 120)), "units")
        
        # Handle shift + mouse wheel scrolling (horizontal scrolling)
    def on_shift_mousewheel(self, event):
        self.canvas.xview_scroll(int(-1 * (event.delta / 120)), "units")

    def draw_histogram(self):
        # Process the traffic data to get hourly data for each junction
        hourly_data_hanley, hourly_data_elm = self.process_traffic_data()
        if not hourly_data_hanley and not hourly_data_elm:
            
             # Show error message if no data is available for the selected date
            messagebox.showerror("Error", "No data available for the selected date.")
            return
         # Determine the maximum number of vehicles in any hour
        max_vehicles = max(max(hourly_data_hanley.values(), default=0), max(hourly_data_elm.values(), default=0))
            
        # Configure canvas scroll region
        self.canvas.configure(scrollregion=(0, 0, 1500, 650))
            
        # Draw axes
        self.canvas.create_line(50, 550, 1500, 550)  # X axis
        self.canvas.create_line(50, 550, 50, 50)     # Y axis
        
        bar_width = 20 # Set the width of each bar
        gap_between_hours = 10 # Set the gap between bars for each hour
        
        # Draw bars for Hanley Highway/Westway
        for hour in range(24):
            vehicles_count = hourly_data_hanley.get(hour, 0)
            x1 = 50 + hour * (bar_width * 2 + gap_between_hours)
            y1 = 550 - (vehicles_count / max_vehicles * 500) if max_vehicles > 0 else 550
            
            # Draw bar for hanly road
            self.canvas.create_rectangle(x1, y1, x1 + bar_width - 2, 550, fill='DarkOrange1')
            
            # Add text label with vehicle count above the bar
            self.canvas.create_text(x1 + bar_width / 2 - 1, y1 - 10, text=str(vehicles_count))
            # Label for hours on x-axis
            self.canvas.create_text(x1 + bar_width / 2 - 1, 570, text=f"{hour}:00")
        
        # Draw bars for Elm Avenue/Rabbit Road
        for hour in range(24):
            vehicles_count = hourly_data_elm.get(hour, 0)
            x1 = (50 + hour * (bar_width *2 + gap_between_hours)) + bar_width 
            y1 = (550 - (vehicles_count / max_vehicles *500)) if max_vehicles > 0 else 550
        
            # Draw bar 
            self.canvas.create_rectangle(x1, y1, x1 + bar_width -2, 550, fill='SpringGreen2')
            # Add text label with vehicle count above the bar
            self.canvas.create_text(x1 + bar_width /2 -1, y1 -10, text=str(vehicles_count))
        
        # Title and labels 
        self.canvas.create_text(600, 20,
                              text=f"Vehicle Frequency Histogram for {self.date}",
                              font=("Arial", 16))
        self.canvas.create_text(20, 300, text="Number of Vehicles", angle=90)
        self.canvas.create_text(600, 590, text="Time of the Day")

    def add_legend(self):
        """
        Adds a legend to the histogram to indicate which bar corresponds to which junction.
        """
        hanley_color = "DarkOrange"
        elm_color = "springGreen2"
        
        legend_x = 1100 
        legend_y = 50 
        
        # Hanley Highway/Westway Legend 
        self.canvas.create_rectangle(legend_x + 150,
                                   legend_y,
                                   legend_x + 170,
                                   legend_y + 20,
                                   fill=hanley_color)
        
        self.canvas.create_text(legend_x,
                              legend_y + 10,
                              text="Hanley Highway/Westway",
                              anchor="w")
        
        # Elm Avenue/Rabbit Road Legend 
        self.canvas.create_rectangle(legend_x + 150,
                                   legend_y + 30,
                                   legend_x + 170,
                                   legend_y + 50,
                                   fill=elm_color)
        
        self.canvas.create_text(legend_x,
                              legend_y + 40,
                              text="Elm Avenue/Rabbit Road",
                              anchor="w")

    def run(self):
        self.setup_window()
        self.draw_histogram()
        self.add_legend()
        self.root.mainloop()

    def process_traffic_data(self):
            # Initialize dictionaries to hold the hourly vehicle count for Hanley Highway and Elm Avenue
        hourly_data_hanley = defaultdict(int)
        hourly_data_elm = defaultdict(int)
        
        try:
            # Open the CSV file containing traffic data
            with open(self.traffic_data, 'r') as file:
                reader = csv.DictReader(file) # Create a CSV dictionary reader object
                for row in reader:
                    date_str = row['Date'] # Extract the date from the current row
                    if date_str == self.date:
                        time_str = row['timeOfDay']
                        hour = datetime.strptime(time_str, "%H:%M:%S").hour
                        
                        if row['JunctionName'] == "Hanley Highway/Westway":
                            hourly_data_hanley[hour] += 1
                        elif row['JunctionName'] == "Elm Avenue/Rabbit Road":
                            hourly_data_elm[hour] += 1
        except Exception as e:
            print(f"Error processing traffic data: {e}")
            
        return hourly_data_hanley, hourly_data_elm
      

# Main Program
class MultiCSVProcessor:
    def __init__(self):
        """
        Initializes the application for processing multiple CSV files.
        """
        self.current_data = []
        self.processed_files = []

    def load_csv_file(self, DD, MM, YYYY):
        """
        Loads a CSV file based on the date provided.
        """
        # Construct the file path using the provided date (DD, MM, YYYY)
        file_path = f"traffic_data{DD:02d}{MM:02d}{YYYY}.csv"
        try:
            with open(file_path, 'r') as file:
                # Read the first line of the file to get the header (column names)
                header = file.readline().strip().split(',')
                
                # Process data lines
                data = []
                for line in file:
                    values = line.strip().split(',')
                    if len(values) == len(header):
                         # Create a dictionary for the row by zipping headers and values together
                        row_data = dict(zip(header, values))
                        data.append(row_data)
                
                self.current_data = data
                # Add the file path to the list of processed files
                self.processed_files.append(file_path)
                return True
        except FileNotFoundError:
            print(f"Error: File {file_path} does not exist. Please check your input date.")
            return False
        except Exception as e:
            print(f"Error loading file: {e}")
            return False

    def clear_previous_data(self):
        """
        Clears data from the previous run.
        """
        if 'results.txt' in os.listdir():
           with open('results.txt', 'w') as f:
               f.write("")
               

    def process_files(self):
       """
       Main loop for handling multiple CSV files until the user decides to quit.
       """
       counter = 0 
       while True:
           if counter >= 1: 
               print("Erasing the previous data...\n") 
           self.clear_previous_data() 
           print("\n___Starting traffic data analysis___\n")
           DD, MM, YYYY = validate_date_input()
           file_name = f"traffic_data{DD:02d}{MM:02d}{YYYY}.csv"
           
           if os.path.isfile(file_name):
               print(f"Processing data from {file_name}...")
               results,_=process_csv_data(file_name)
               display_outcomes(results)
               print(f"Saving results to results.txt file...\n")
               print(f"Displaying histogram for {DD:02d}/{MM:02d}/{YYYY}...")
               save_results_to_file(results)

               selected_date=f"{DD:02d}/{MM:02d}/{YYYY}"
               app=HistogramApp(file_name ,selected_date)
               app.run()
               counter += 1 
               if not validate_continue_input():
                   print("Exiting the program...")
                   break 
           else:
               print("Current working directory:", os.getcwd())
               print(f"File {file_name} does not exist. Please check your input date.")

# Program Runner
if __name__ == "__main__":
    processor = MultiCSVProcessor()
    processor.process_files()