# Assignment #0.6: 
# 1) Create a Python file inside the Assignment folder to calculate seconds, minutes, and hours in a year.
# 2) Push it to your GitHub and send the GitHub link to me.

years = int(input("Enter number of years: "))

days = years * 365
hours = days * 24
seconds = hours * 3600
numberOfDaysInYear= 365
numberOfHoursInYear = 8760
numberOfSecondsInYear = 31536000

print(f"{years} years equal to {days} days, {hours} hours, and {seconds} seconds.")
print(f" While 1 year equal to {numberOfDaysInYear} days, {numberOfHoursInYear} hours, and {numberOfSecondsInYear} seconds.")