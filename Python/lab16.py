def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b


def modulus(a, b):
    if b == 0:
        return None
    return a % b


def power(base, exp=2):
    return base ** exp


def format_number(num):
    return f"{num:.2f}"


history = []

while True:
    print("\n" + "=" * 40)
    print("     ENTERPRISE MODULAR UTILITY CALCULATOR")
    print("=" * 40)

    print("\nSelect an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus / Remainder (%)")
    print("6. Power / Exponentiation (Default: Square)")
    print("7. View Calculation History")
    print("8. Exit")

    choice = input("\nEnter your choice (1-8): ")

    if choice == "1":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = add(a, b)
        record = f"{a} + {b} = {format_number(result)}"

    elif choice == "2":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = subtract(a, b)
        record = f"{a} - {b} = {format_number(result)}"

    elif choice == "3":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = multiply(a, b)
        record = f"{a} * {b} = {format_number(result)}"

    elif choice == "4":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        result = divide(a, b)

        if result is None:
            print("[ERROR] Division by zero is not allowed.")
            continue

        record = f"{a} / {b} = {format_number(result)}"

    elif choice == "5":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        result = modulus(a, b)

        if result is None:
            print("[ERROR] Modulus by zero is not allowed.")
            continue

        record = f"{a} % {b} = {format_number(result)}"

    elif choice == "6":
        base = float(input("Enter base number: "))
        exp_input = input("Enter exponent (press Enter for default square): ")

        if exp_input.strip() == "":
            result = power(base)
            record = f"{base} ^ 2 = {format_number(result)}"
        else:
            exp = float(exp_input)
            result = power(base, exp)
            record = f"{base} ^ {exp} = {format_number(result)}"

    elif choice == "7":
        print("\n--- Calculation History ---")

        if len(history) == 0:
            print("No calculations performed yet.")
        else:
            for i, item in enumerate(history, 1):
                print(f"{i}. {item}")

        continue

    elif choice == "8":
        print("\nThank you for using the Utility Calculator!")
        print("Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice. Please enter a number from 1 to 8.")
        continue

    history.append(record)
    print("\n[RESULT]", record)