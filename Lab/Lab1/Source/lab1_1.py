import re

def validate_password(): # function to validate the password using regular expression module
    valid_password = True
    while valid_password: # iterate the loop until users enters valid password
        password = input('Enter the password:')
        if len(password) < 6 or len(password) > 16: #checking whether the length is in between 6-16 characters
            print('Invalid Password:Password does not match the length[6-16] of the characters')
        elif not re.search("[a-z]",password): #checking whether password contains lower case
            print('Invalid Password:Password does not contain lower case')
        elif not re.search("[A-Z]",password): # checking whether password contains upper case
            print('Invalid Password:Password does not contain upper case')
        elif not re.search("[0-9]",password):# checking whether password contains digits
            print('Invalid Password:Password does not contain digits')
        elif not re.search("[$@!*]",password): #checking the password for special characters
            print('Invalid Password:Password does not contain special characters')
        else:
            print('Password is valid') # set the valid_password to false if it matches all the given criteria
            valid_password = False;


validate_password()