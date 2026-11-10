Temperature Monitor and Alarm Checker

What it does:

This is a Python program that monitors five temperature readings from a machine. It calculates the highest, lowest and average temperatures and warns the user when a reading exceeds the safe temperature limit.

How to run it:

Install Python 3, then run:

python Temperature_monitor.py

Sample output:

Enter the safe temperature limit: 80

Enter temperature reading 1: 40
Enter temperature reading 2: 50
Enter temperature reading 3: 60
Enter temperature reading 4: 75
Enter temperature reading 5: 90

----- TEMPERATURE REPORT -----

All readings: [40, 50, 60, 75, 90]
Highest temperature: 90
Lowest temperature: 40
Average temperature: 63.0

WARNING! Machine temperature is above the safe limit.

Temperature trend: Increasing!

Temperature monitoring completed.

My own twist:

I added a Temperature Trend Detector. This feature identifies whether the machine’s temperature is consistently increasing, decreasing, or fluctuating. It helps users notice possible overheating trends.

What I learned:

I learned how to use Python functions, lists, loops and conditional statements. I also learned how to handle invalid user input using exception handling.

Author:

Anwankuo Christopher Marvin 
ND1 Mechatronics Engineering
Yaba College of Technology (YabaTech).



What happens when a machine starts getting hotter than its safe operating temperature? 🌡️

For my Python programming project, I chose to build a Temperature Monitor and Alarm Checker.

My program collects five temperature readings, calculates the highest, lowest and average temperatures, and alerts the user whenever the safe temperature limit is exceeded.

One challenging part was making sure the program could handle incorrect inputs. I solved this by using Python’s exception handling to prevent the program from crashing when someone enters something other than a number.

I also added my own feature: a Temperature Trend Detector. It identifies whether the temperature is increasing, decreasing or fluctuating.

Working on this project helped me understand how functions, lists, loops and conditional statements work together to solve practical problems.

As an ND1 Mechatronics Engineering student at YabaTech, I’m excited to keep learning, building and improving my programming skills.
