def validateInt(message):
    while True:
        try:
            value = int(input(message))
            return value
        except ValueError:
            print("Invalid input, please enter an integer.")