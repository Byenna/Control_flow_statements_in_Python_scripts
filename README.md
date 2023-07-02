# Practice_writing_simple_Python_scripts
A few hands-on Scripts to help you practice writing simple Python scripts

# A step by step guide on how to...

**3 ...write a Python script that generates a random number between 1 and 100 and lets the user guess the number. The script should provide feedback to the user after each guess, indicating whether their guess was too high, too low, or correct. The script should continue until the user guesses the correct number.**

Step 1: Import the Required Modules
To generate a random number, we need to import the `random` module. Add this line of code at the beginning of your script:

`import random`

Step 2: Generate a Random Number
Next, we need to generate a random number between 1 and 100 using the `random.randint()` function. Store this generated number in a variable. Here's an example:

`random_number = random.randint(1, 100)`

Step 3: Take Input from the User
Ask the user to enter their guess and store it in a variable using the `input()` function. Here's an example:

`guess = int(input("Enter your guess (between 1 and 100): "))`

Step 4: Check if the Guess is Correct
Use an if-elif-else statement to check if the guess is too high, too low, or correct. Here's an example:

```
if guess > random_number:
    print("Too high!")
elif guess < random_number:
    print("Too low!")
else:
    print("Correct!")
```

Step 5: Repeat Until Correct Guess
To repeat the guessing process until the user guesses the correct number, you can use a while loop. Enclose your guessing logic in a while loop that keeps running until the guess is correct. Here's an example:

```
while guess != random_number:
    if guess > random_number:
        print("Too high!")
    else:
        print("Too low!")
    
    guess = int(input("Enter your guess (between 1 and 100): "))

print("Correct!")
```
Putting it all together, here's the complete Python script:

```
import random

random_number = random.randint(1, 100)

guess = int(input("Enter your guess (between 1 and 100): "))

while guess != random_number:
    if guess > random_number:
        print("Too high!")
    else:
        print("Too low!")
    
    guess = int(input("Enter your guess (between 1 and 100): "))

print("Correct!")
```

That's it! You have successfully written a Python script that generates a random number between 1 and 100 and lets the user guess the number. The script will provide feedback to the user after each guess, indicating whether their guess was too high, too low, or correct. The script will continue until the user guesses the correct number.
