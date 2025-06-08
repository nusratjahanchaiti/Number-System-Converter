import time
from colorama import init, Fore, Style
init(autoreset=True)

def convert_from_decimal(n):
    print(Fore.MAGENTA + f"\n--- From Decimal ({n}) ---")
    print(f"Binary      : {bin(n)[2:]}")
    print(f"Octal       : {oct(n)[2:]}")
    print(f"Hexadecimal : {hex(n)[2:].upper()}")

def convert_from_binary(b):
    try:
        n = int(b, 2)
        print(Fore.BLUE + f"\n--- From Binary ({b}) ---")
        print(f"Decimal     : {n}")
        print(f"Octal       : {oct(n)[2:]}")
        print(f"Hexadecimal : {hex(n)[2:].upper()}")
    except ValueError:
        print(Fore.RED + "Invalid binary number.")

def convert_from_octal(o):
    try:
        n = int(o, 8)
        print(Fore.CYAN + f"\n--- From Octal ({o}) ---")
        print(f"Decimal     : {n}")
        print(f"Binary      : {bin(n)[2:]}")
        print(f"Hexadecimal : {hex(n)[2:].upper()}")
    except ValueError:
        print(Fore.RED + "Invalid octal number.")

def convert_from_hex(h):
    try:
        n = int(h, 16)
        print(Fore.CYAN + f"\n--- From Hexadecimal ({h}) ---")
        print(f"Decimal     : {n}")
        print(f"Binary      : {bin(n)[2:]}")
        print(f"Octal       : {oct(n)[2:]}")
    except ValueError:
        print(Fore.RED + "Invalid hexadecimal number.")

def print_theory():
    print(Fore.MAGENTA + "\n=== Theory of Number System Conversion ===")
    print(Fore.WHITE + "Number systems use different bases to represent numbers:")
    print("- Binary (base 2): Uses digits 0 and 1.")
    print("- Octal (base 8): Uses digits 0 to 7.")
    print("- Decimal (base 10): Uses digits 0 to 9.")
    print("- Hexadecimal (base 16): Uses 0 to 9 and A to F.")
    print("Conversions rely on base arithmetic and positional value.\n")

def print_menu():
    print(Fore.CYAN + "                          ========================================")
    print(Fore.CYAN + "                                  Number System Converter ")
    print(Fore.CYAN + "                          ========================================\n")
    print(Fore.GREEN + "1." + Fore.WHITE + " Convert a Number")
    print(Fore.MAGENTA + "2." + Fore.WHITE + " Theory of Number Systems")
    print(Fore.RED + "3." + Fore.WHITE + " Exit")

while True:
    print_menu()
    choice = input(Fore.YELLOW + "Enter your choice (1-3): ")

    if choice == '1':
        print(Fore.GREEN + "\nChoose input number system:")
        print("1. Decimal\n2. Binary\n3. Octal\n4. Hexadecimal")
        base_choice = input("Enter option (1-4): ")
        num = input("Enter the number: ")

        if base_choice == '1':
            convert_from_decimal(int(num))
        elif base_choice == '2':
            convert_from_binary(num)
        elif base_choice == '3':
            convert_from_octal(num)
        elif base_choice == '4':
            convert_from_hex(num)
        else:
            print(Fore.RED + "Invalid number system option.")
    
    elif choice == '2':
        print_theory()
    
    elif choice == '3':
        print(Fore.GREEN + "\nExiting... Thank you for using the converter!")
        time.sleep(1)  # 1-second delay
        print(Fore.GREEN + "Have a great day and keep learning! :)\n")
        break

    else:
        print(Fore.RED + "Invalid menu choice. Please enter 1, 2, or 3.")