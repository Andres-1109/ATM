The consultBalance function is a simple yet essential part of the ATM program. Its purpose is to display the current account balance to the user in a clear and readable format. It receives the balance as an input parameter and prints it using an informative message: "Your balance is: {balance}".

This function ensures that users can easily check their available funds at any point during their session. While it does not modify the balance or interact with other operations, it plays a key role in providing transparency and user confidence by showing real-time account information.

The registerOperation function logs every user transaction in the operationsHistory list. It records the type of operation—balance inquiry, withdrawal, or deposit—and includes the amount when applicable. This ensures a clear, chronological record of all actions, allowing users to review their session activity reliably.

The updateBalance function handles changes to the account balance. It receives the current balance and a numeric amount, then returns the updated balance after adding (for deposits) or subtracting (for withdrawals). Together, these functions maintain accurate balance tracking and a transparent transaction history, forming the core of the ATM’s financial logic.

The validateInt function ensures that all user inputs requiring integers are correctly entered. It uses a continuous loop that prompts the user with a custom message, attempting to convert the input to an integer. If the input is invalid (letters, symbols, or decimals), a ValueError is caught, and the user is informed with the message: "Invalid input, please enter an integer." The loop continues until a valid integer is provided.

This function prevents the program from crashing due to incorrect input types and is used across the ATM system for menu selection, PIN entry, operation counts, and transaction amounts, ensuring robust and error-free input handling.