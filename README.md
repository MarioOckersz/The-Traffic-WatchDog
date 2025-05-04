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
```
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
```
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
```
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

```

Contributing
Contributions are welcome! To contribute:

This project is licensed under the MIT License. See the LICENSE file for details.

Developed by Mario Ockersz, 2024.
