from validations import validateInt

def validateClient():
    """Valida el PIN del cliente. Bloquea la cuenta tras 3 intentos fallidos."""
    attempts = 3
    password = 1234

    while attempts > 0:
        pin = validateInt("Insert your PIN: ")

        if pin == password:
            print("Successful authentication.\n")
            return True
        else:
            attempts -= 1
            print(f"Incorrect PIN. Attempts left: {attempts}")

    print("Blocked account. Goodbye.")
    exit()

def consultar_saldo(balance, history):
    """Muestra el saldo actual."""
    print(f"\n  Saldo actual: ${balance:.2f}\n")
    history.append(f"Consulta de saldo: ${balance:.2f}")
    return balance


def retirar_dinero(balance, history):
    """Retira dinero si hay saldo suficiente."""
    amount = validateInt("\n  ¿Cuánto desea retirar? $")
    if amount <= 0:
        print("  El monto debe ser mayor a cero.")
    elif amount > balance:
        print(f"  Saldo insuficiente. Su saldo es ${balance:.2f}")
    else:
        balance -= amount
        print(f"  Retiro exitoso. Saldo restante: ${balance:.2f}\n")
        history.append(f"Retiro: -${amount:.2f} | Saldo: ${balance:.2f}")
    return balance


def depositar_dinero(balance, history):
    """Deposita dinero en la cuenta."""
    amount = validateInt("\n  ¿Cuánto desea depositar? $")
    if amount <= 0:
        print("  El monto debe ser mayor a cero.")
    else:
        balance += amount
        print(f"  Depósito exitoso. Saldo actual: ${balance:.2f}\n")
        history.append(f"Depósito: +${amount:.2f} | Saldo: ${balance:.2f}")
    return balance


def ver_historial(history):
    """Muestra el historial de operaciones."""
    print("\n  ── Historial de operaciones ──")
    if not history:
        print("  No hay operaciones registradas.")
    else:
        for i, op in enumerate(history, 1):
            print(f"  {i}. {op}")
    print()

