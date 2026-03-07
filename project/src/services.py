def consultBalance(balance):
    print(f"Your balance is: {balance}")

def registerOperation(option, operationsHistory, amount=None):
    if option == 1:
        operation = ("Consult Balance")
    elif option == 2:
        operation = (f"Withdraw Money: ${amount}")
    elif option == 3:
        operation = (f"Deposit Money: ${amount}")
    operationsHistory.append(operation)

def updateBalance(balance, amount):
    balance += amount
    return balance