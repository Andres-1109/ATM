### PIN Validation System

This program validates a user's access PIN.
A constant is used to store the correct PIN, ensuring that its value cannot be modified during execution.

The program also includes an attempt counter that limits the number of login attempts to three.

A `while` loop is used to allow the user to enter the PIN until the maximum number of attempts is reached. Inside the loop, an `if` statement checks whether the entered PIN matches the correct one.

* If the PIN is correct, access is granted.
* If the PIN is incorrect, the program shows how many attempts are left.

If the number of attempts reaches zero, the account is blocked and access is denied.
