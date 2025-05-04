# Traffic-WatchDog
🚦📈 Unlock traffic insights in a flash! 🚛

Traffic Data Analysis Program
```
                   ,  o ' .
                  .  -  -  o
                  o . _ ` '  ` ; .
 ________________________________  H___
P                           MARIO| H ..\
|                         _______| H |_\\
|                        |.========H -  |
B_,-._,-._______________/ |,-._,-._H_,-.)
--`-'-`-'------------------`-'-`-'---`-'--Mo⠀⠀⠀⠀

```

Welcome to the Traffic Data Analysis Program! This Python application processes traffic data from CSV files, analyzes vehicle metrics, and visualizes the results using a Tkinter-based histogram. It’s designed to provide insights into traffic patterns at two junctions: Elm Avenue/Rabbit Road and Hanley Highway/Westway.
Table of Contents

#Overview
#Features
#Prerequisites
#Installation
#Usage
#Program Structure
#Sample Output
#Contributing
#License

Overview
This program, developed by Mario Ockersz (Student ID: w2119866), processes traffic data stored in CSV files (e.g., traffic_dataDDMMYYYY.csv). It validates user input for dates, extracts metrics like vehicle counts and speeds, calculates statistics, and displays a histogram of vehicle frequency by hour. The results are saved to a text file (results.txt) for record-keeping.
+-----------------+
|  Input Date     |
| (DD MM YYYY)    |
+-----------------+
        |
        v
+-----------------+
|  Load CSV File  |
| (traffic_data)  |
+-----------------+
        |
        v
+-----------------+
| Process Metrics |
| (Vehicles, Speed)|
+-----------------+
        |
        v
+-----------------+
| Display Results |
| (Console, File) |
+-----------------+
        |
        v
+-----------------+
| Tkinter Histogram|
| (Vehicle/Hour)  |
+-----------------+

Features

Input Validation: Ensures valid date input (DD MM YYYY) with checks for leap years and month-specific day limits.
Data Processing: Analyzes CSV data to compute metrics like total vehicles, electric vehicles, and speeding incidents.
Visualization: Displays a histogram comparing vehicle frequency at two junctions using Tkinter.
Persistence: Saves analysis results to results.txt.
Multi-File Support: Processes multiple CSV files in a loop until the user exits.

Prerequisites
To run this program, you need:

Python 3.6+: The program uses standard Python libraries.
Tkinter: Usually included with Python; ensure it's installed (sudo apt-get install python3-tk on Linux if needed).
CSV Files: Traffic data in the format traffic_dataDDMMYYYY.csv (e.g., traffic_data21062024.csv).

Installation

Clone the Repository:
git clone https://github.com/your-username/traffic-data-analysis.git
cd traffic-data-analysis


Ensure Python is Installed:Verify Python version:
python3 --version


Prepare CSV Files:Place your traffic data CSV files (e.g., traffic_data21062024.csv) in the same directory as w2119866.py. The CSV should have columns like JunctionName, Date, timeOfDay, VehicleType, etc.


Usage

Run the Program:
python3 w2119866.py


Enter Date:

Input the day (DD), month (MM), and year (YYYY) when prompted.
Example: For traffic_data21062024.csv, enter 21 06 2024.


View Results:

The program processes the CSV and displays metrics in the console.
A Tkinter window shows a histogram of vehicle frequency by hour.
Results are appended to results.txt.


Analyze Another File:

Choose Y to process another CSV or N to exit.



  _____
 |     |  Enter Date: 21 06 2024
 |_____|  File: traffic_data21062024.csv
      |
      v
  _____
 |     |  Metrics: Total Vehicles, Trucks, etc.
 |_____|  Histogram: Vehicle Frequency
      |
      v
  _____
 |     |  Save to: results.txt
 |_____|  Continue? (Y/N)

Program Structure
The program is organized into several components:

Input Validation (validate_date_input, validate_continue_input):Ensures valid user input for dates and continuation prompts.

CSV Processing (process_csv_data):Reads CSV files, computes metrics (e.g., total vehicles, speeding vehicles), and handles errors like missing files.

Display (display_outcomes):Prints analysis results to the console.

File Output (save_results_to_file):Appends results to results.txt.

Histogram (HistogramApp):Uses Tkinter to create a bar chart comparing vehicle counts by hour at both junctions.

Main Loop (MultiCSVProcessor):Orchestrates the workflow, allowing multiple file processing.


Key metrics include:

Total vehicles, trucks, electric vehicles, and two-wheeled vehicles.
Buses heading north from Elm Avenue/Rabbit Road.
Percentage of trucks and scooters.
Peak traffic hours and rain duration.

Sample Output
For traffic_data21062024.csv, the console output might look like:
___Starting traffic data analysis___

Please enter the day of the survey in the format DD: 21
Please enter the month of the survey in the format MM: 06
Please enter the year of the survey in the format YYYY: 2024
Processing data from traffic_data21062024.csv...

--- Traffic Analysis Outcomes ---
File Name: traffic_data21062024.csv
The total number of vehicles recorded: 1234
The total number of trucks recorded: 150
The total number of electric vehicles: 300
...
Peak Hour on Hanley Highway/Westway is between: Between 8:00 and 9:00
Total Hours of Rain on Selected Date: 3

Saving results to results.txt file...
Displaying histogram for 21/06/2024...
Do you want to analyze another dataset? (Y/N):

The histogram shows orange bars for Hanley Highway/Westway and green bars for Elm Avenue/Rabbit Road, with a legend and hourly labels.
Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a branch (git checkout -b feature/your-feature).
Commit changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a Pull Request.

Please ensure your code follows PEP 8 style guidelines and includes comments for clarity.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Developed by Mario Ockersz, 2024. For educational purposes at [Your University].
