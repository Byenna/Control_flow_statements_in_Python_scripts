# Practice_writing_simple_Python_scripts
A few hands-on Scripts to help you practice writing simple Python scripts

# A step by step guide on how to...

**5 ..write a Python script that prompts the user to enter a string and checks whether the string is a palindrome or not. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.**


Step 1: Take Input from the User
Start by asking the user to enter a string and store it in a variable. You can do this using the `input()` function. Here's an example:

`string = input("Enter a string: ")`

Step 2: Reverse the String
To check whether the string is a palindrome or not, we need to reverse the string. You can use string slicing with a step of -1 to reverse the string. Store the reversed string in a new variable. Here's an example:

`reversed_string = string[::-1]`

Step 3: Check if it is a Palindrome
To check if the string is a palindrome, compare the original string with the reversed string. If they are same, then the string is a palindrome. Use an if-else statement to determine and output the result. Here's an example:

```
if string == reversed_string:
    print("Palindrome")
else:
    print("Not a palindrome")
```
Putting it all together, here's the complete Python script:

```
string = input("Enter a string: ")

reversed_string = string[::-1]

if string == reversed_string:
    print("Palindrome")
else:
    print("Not a palindrome")
```
That's it! You have successfully written a Python script that prompts the user to enter a string and checks whether the string is a palindrome or not. The script will output "Palindrome" if the string reads the same forward and backward, and "Not a palindrome" otherwise.

# EXTRA (if you are a true lady-dev👠)

If you are looking to add CSS styling to the output of the script when running it in a browser or a GUI interface, you would need to use HTML/CSS in conjunction with your Python script. Here's an example of how you can achieve that:

**Python code:**

```
def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string


def main():
    string = input("Enter a string: ")
    
    if is_palindrome(string):
        print('<p class="palindrome">Palindrome</p>')
    else:
        print('<p class="not-palindrome">Not a palindrome</p>')


if __name__ == "__main__":
    main()
```
-----------------------------------------------------------------------------
**HTML/CSS code:**
```
<!DOCTYPE html>
<html>
<head>
    <style>
        .palindrome {
            color: green;
        }
        
        .not-palindrome {
            color: red;
        }
    </style>
</head>
<body>
    <script>
        // Run the Python script and capture the output
        const pythonOutput = '<<OUTPUT OF PYTHON SCRIPT>>';

        // Display the output in the browser
        document.write(pythonOutput);
    </script>
</body>
</html>
```
-----------------------------------------------------------------------------
In this example, instead of printing the output directly in the Python script, we capture the output as a string and replace `<<OUTPUT OF PYTHON SCRIPT>>` in the HTML code with that output. This way, you can run an HTML file in a browser and see the styled output. The CSS rules defined in the `<style>` section will be applied to the output text based on their class names (`palindrome` and `not-palindrome`).
Remember to replace `<<OUTPUT OF PYTHON SCRIPT>>` with the actual output of your Python script. Also, make sure to save the HTML file with a `.html` extension and open it in a web browser to see the styled output.