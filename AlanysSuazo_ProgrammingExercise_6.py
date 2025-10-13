# Alanys Suazo
# Assignment: Programming Exercise 6
# The purpose of this assignment is to practice importing and using re(regular expressions) in Python
#  as re has many practical applications. The code is to validate the user input and categorize it as
#  a zip code, a phone number, or a social security number, while other forms of input will be deemed invalid

#importing regular expressions
import re

#function tests input
def validate_input(value:str):
    #these are the numbers formats
    patterns = {
        "phone": re.compile(r'\d{3}-\d{3}-\d{4}$'),
        "zip": re.compile(r'\d{5}$'),
        "ssn": re.compile(r'\d{3}-\d{2}-\d{4}$')
    }
    #this part chacks that the input matches everything completely
    for label, pattern in patterns.items():
        if pattern.fullmatch(value):
            return f"{label} '{value}' is Valid."
    return f"'{value}' does not match the requirements."

# the user interface that takes in inputs
def main():
    print('Format Tester (Phone,Zip,SSN)')
    #loop for program to run
    while True:
        user_input = input("Enter the number to validate (or 'q' to quit): ").strip()
        if user_input.lower() == 'q':
            print("Exiting program. Goodbye.")
            break
        print(validate_input(user_input))

# calling
if __name__ =="__main__":
    main()