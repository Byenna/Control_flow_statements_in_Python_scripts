# Practice_writing_simple_Python_scripts
A few hands-on Scripts to help you practice writing simple Python scripts

# A step by step guide on how to...

**1 ...write a Python script that takes a student's score as input and outputs their corresponding grade based on the following criteria:**
```
A score of 90 or above gets an 'A'
A score between 80 and 89 gets a 'B'
A score between 70 and 79 gets a 'C'
A score between 60 and 69 gets a 'D'
A score below 60 gets an 'F'
```

Step 1: Take Input from the User
First, you need to take input from the user. You can do this using the `input()` function. Ask the user to enter their score and store it in a variable. Here's an example:

`score = int(input("Enter the student's score: "))`

Step 2: Define the Grade Criteria
Next, we need to define the grade criteria. As per the given criteria, we have five different grade ranges. You can use if-elif-else statements to determine the grade based on the given score. Here's an example:

```
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
```

Step 3: Output the Grade
Finally, we need to output the grade to the user. You can use the `print()` function to display the grade. Here's an example:

`print("The student's grade is:", grade)`

Putting it all together, here's the complete Python script:

```
score = int(input("Enter the student's score: "))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print("The student's grade is:", grade)
```

That's it! You have successfully written a Python script that takes a student's score as input and outputs their corresponding grade based on the given criteria.