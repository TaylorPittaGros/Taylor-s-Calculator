from app import operations
from app.utils import get_number

def run():
    while True:
        print("\n1. Add\n2. Subtract\n3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            a = get_number("A: ")
            b = get_number("B: ")
            print("Result:", operations.add(a, b))

        elif choice == "2":
            a = get_number("A: ")
            b = get_number("B: ")
            print("Result:", operations.subtract(a, b))

        elif choice == "3":
            break

        else:
            print("Invalid")

run()