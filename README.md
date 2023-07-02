# Practice_writing_simple_Python_scripts
A few hands-on Scripts to help you practice writing simple Python scripts

# A step by step guide on how to...

**4 ...write a Python script that takes a number 'n' as input and prints the Fibonacci series up to the 'n'th term. The Fibonacci series starts with 0 and 1, and each subsequent term is the sum of the two preceding terms.**


Step 1: Take Input from the User
Start by asking the user to enter the number 'n' and store it in a variable. You can do this using the `input()` function. Here's an example:

`n = int(input("Enter a number: "))`

Step 2: Initialize the First Two Terms
In the Fibonacci sequence, the first two terms are 0 and 1. Create two variables to store these initial terms. Here's an example:

```
term1 = 0
term2 = 1
```

Step 3: Generate the Terms in the Fibonacci Series
To generate the terms in the Fibonacci series, you can use a while loop. Start the loop with a counter set to 0, and continue until the counter reaches the desired 'n' value. In each iteration of the loop, calculate the next term by adding the previous two terms and update the values of the variables accordingly. Here's an example:

```
counter = 0
while counter < n:
    print(term1, end=" ")
    term_temp = term1 + term2
    term1 = term2
    term2 = term_temp
    counter += 1
```

Step 4: Output the Fibonacci Series
Within the loop, print each term in the Fibonacci series using the `print()` function. Add the `end=" "` parameter to print the terms on the same line with spaces in between. Here's an example:

`print(term1, end=" ")`

Putting it all together, here's the complete Python script:

```
n = int(input("Enter a number: "))

term1 = 0
term2 = 1

counter = 0
while counter < n:
    print(term1, end=" ")
    term_temp = term1 + term2
    term1 = term2
    term2 = term_temp
    counter += 1
```

That's it! You have successfully written a Python script that takes a number 'n' as input and prints the Fibonacci series up to the 'n'th term. The script will generate the Fibonacci series starting with 0 and 1, and each subsequent term will be the sum of the two preceding terms.