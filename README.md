# Practice_writing_simple_Python_scripts
A few hands-on Scripts to help you practice writing simple Python scripts

# A step by step guide on how to...

**2 ...write a Python script that prompts the user to enter a year and determines whether it is a leap year or not. A leap year is divisible by 4 but not by 100, except for years that are divisible by 400. The script should print "Leap year" or "Not a leap year" accordingly.


Step 1: Take Input from the User
First, you need to ask the user to enter a year and store it in a variable. You can do this using the `input()` function. Here's an example:

`year = int(input("Enter a year: "))`

Step 2: Determine if it is a Leap Year
To determine if a year is a leap year or not, you need to check if it meets the following conditions:
- It is divisible by 4 but not by 100 OR
- It is divisible by 400
You can use if-else statements to check these conditions and determine if the year is a leap year or not. Here's an example:

```
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")
```

Step 3: Output the Result
Finally, you can use the `print()` function to display whether the year is a leap year or not. Here's an example:

```
print("The year", year, "is a leap year.")  # if it is a leap year
print("The year", year, "is not a leap year.")  # if it is not a leap year
```

Putting it all together, here's the complete Python script:

```
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")
```

That's it! You have successfully written a Python script that prompts the user to enter a year and determines whether it is a leap year or not. The script will print "Leap year" or "Not a leap year" accordingly.