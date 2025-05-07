# __The-Traffic-WatchDog__
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
This program, developed by Mario Ockersz, processes traffic data stored in CSV files (e.g., traffic_dataDDMMYYYY.csv). It validates user input for dates, extracts metrics like vehicle counts and speeds, calculates statistics, and displays a histogram of vehicle frequency by hour. The results are saved to a text file (results.txt) for record-keeping.
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
📌 Features
✔ CSV Data Processing – Extract key traffic metrics (vehicles, speed, junctions).
✔ Interactive Histograms – Visualize hourly traffic flow with tkinter.
✔ Date Validation – Ensures correct input format and checks leap years.
✔ Rain Tracking – Calculates total rain hours for the selected date.
✔ Peak Hour Detection – Identifies busiest traffic times.


🛠 Installation
Clone the repo:
```
git clone https://github.com/MarioOckersz/Traffic-WatchDog.git
cd Traffic-WatchDog
```
To run this program, you need:

Python 3.6+: The program uses standard Python libraries.
Ensure Python is Installed:Verify Python version:
python3 --version
Tkinter: Usually included with Python 
ensure it's installed (sudo apt-get install python3-tk on Linux if needed).
CSV Files: Traffic data in the format traffic_dataDDMMYYYY.csv (e.g., traffic_data21062024.csv).

🚀 Usage
Run the script:
```
python Traffic-WatchDog.py
```
View Results:

The program processes the CSV and displays metrics in the console.
A Tkinter window shows a histogram of vehicle frequency by hour.
Results are appended to results.txt.

📋 CSV File Format Required

```
  _____________________________
/                             \
|    MUST HAVE THESE HEADERS:  |
|______________________________|
       \   ^__^
        \  (oo)\_______
           (__)\       )\/\
               ||----w |
               ||     ||
```
🔍 Header Details
```
JunctionName,Date,timeOfDay,travel_Direction_in,travel_Direction_out,
Weather_Conditions,JunctionSpeedLimit,VehicleSpeed,VehicleType,elctricHybrid
```
❗ Important Notes
Missing headers will crash the program!

Spellings must exactly match (e.g., ```elctricHybrid ≠ electricHybrid```).

Sample CSV: ```traffic_data15062024.csv```

Contributing
Contributions are welcome! To contribute:

This project is licensed under the MIT License. See the LICENSE file for details.

Developed by Mario Ockersz, 2024.
