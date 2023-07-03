# Taking input from the user. Ask the user to enter their score and store it in a variable called score.

score = int(input("Enter your score: "))

# use if-elif-else statements to determine the grade
# A score of 90 or above gets an 'A'
# A score between 80 and 89 gets a 'B'
# A score between 70 and 79 gets a 'C'
# A score between 60 and 69 gets a 'D'
# A score below 60 gets an 'F'

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# Output the Grade

print(f"Your score is: {grade}")