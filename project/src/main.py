from services import validateClient
from menu import menu

if __name__ == "__main__":
    balance = float(1000)
    operationsHistory = []

    validateClient()
    menu(balance, operationsHistory)