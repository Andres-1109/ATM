def validateInt(message):
    """Solicita un entero al usuario, rechazando entradas inválidas."""
    while True:
        try:
            value = int(input(message))
            return value
        except ValueError:
            print("Invalid input, please enter an integer.")