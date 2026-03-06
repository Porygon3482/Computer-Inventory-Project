"""
Name:
Assignment: Project 2, inventory.py
Date: 3/4/2026
Summary:
This is the main program for the computer inventory system. It displays a menu,
validates user input, creates Linux/Windows computer objects, and manages them
in a linked structure sorted by year purchased.
"""

from Computer import Linux, Windows
from linked import linkedComputer


def validate_ip(ip_string):
    """
    Validates an IP address using the following rules:
    - Must have exactly 4 parts separated by periods
    - Each part must be a number from 0 to 255
    - Cannot be 0.0.0.0
    :param ip_string: the IP address string entered by the user
    :return: True if valid, False otherwise
    """
    parts = ip_string.split(".")

    if len(parts) != 4:
        return False

    for part in parts:
        if not part.isdigit():
            return False
        if len(part) > 3:
            return False
        if int(part) < 0 or int(part) > 255:
            return False

    if ip_string == "0.0.0.0":
        return False

    return True


def add_computer(inventory):
    """
    Prompts the user for computer details, validates input,
    creates a Linux or Windows object, and adds it to the inventory.
    :param inventory: the linkedComputer object
    """
    # Validate IP address
    while True:
        ip = input("Enter the computer's IP address: ").strip()
        if validate_ip(ip):
            break
        print("Invalid IP address. Please try again.")

    # Validate year
    while True:
        year = input("Enter the year purchased: ").strip()
        if year.isdigit() and int(year) >= 1970:
            year = int(year)
            break
        print("Invalid year. Please enter a valid year (1970 or later).")

    os = input("Enter the operating system: ").strip()

    # Determine Windows or Linux based on OS name
    if "windows" in os.lower():
        space = input("Enter the C drive capacity: ").strip()
        computer = Windows(ip, year, os, space)
    else:
        space = input("Enter the file system capacity: ").strip()
        computer = Linux(ip, year, os, space)

    inventory.add(computer)
    print("\nComputer added successfully.")


def remove_computer(inventory):
    """
    Prompts user for how many computers to remove, removes them
    from the front of the linked structure, and prints each one.
    :param inventory: the linkedComputer object
    """
    if inventory._size == 0:
        print("\nNo computers in inventory to remove.")
        return

    while True:
        count = input("How many computers do you want to remove: ").strip()
        if count.isdigit() and 0 < int(count) <= inventory._size:
            count = int(count)
            break
        print(f"Invalid number. Please enter a value between 1 and {inventory._size}.")

    print("\nYou have removed the following computer(s):")
    print_header()

    for _ in range(count):
        removed = inventory.remove()
        print(removed)


def list_computers(inventory):
    """
    Prints all computers in the inventory as a formatted table.
    :param inventory: the linkedComputer object
    """
    if inventory._size == 0:
        print("\nNo computers in inventory.")
        return

    print()
    print_header()
    for computer in inventory:
        print(computer)


def print_header():
    """Prints the formatted table header."""
    print(f"{'Year purchased':<16} {'IP address':<20} {'Storage space':<25} {'Operating system'}")
    print("-" * 78)


def main():
    inventory = linkedComputer()

    while True:
        print("\n MENU")
        print("L  List all computers in your inventory")
        print("A  Add a computer")
        print("R  Remove some computers")
        print("Q  Quit")
        choice = input("\n...your choice: ").strip().upper()

        if choice == "L":
            list_computers(inventory)
        elif choice == "A":
            add_computer(inventory)
        elif choice == "R":
            remove_computer(inventory)
        elif choice == "Q":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter L, A, R, or Q.")


if __name__ == "__main__":
    main()