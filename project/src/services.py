import os
from validations import validateInt

def validateClient():
    attempts = 3
    password = 1234

    while attempts > 0: 
        pin = validateInt("Insert your pin: ")

        if pin == password:
            print("Successful authentication ")
            break
        else:
            attempts -= 1
            print(f"Incorrect PIN, you have these attempts left: {attempts} ")
    if attempts == 0:
        print("Blocked accunt")
        exit()

