import ipaddress
import msvcrt
import os
from hash_rgstr import ethent


def display_menu():
    print("\n------------------ Hello welcome in our project of Computer Science Calculator------------------")

    while True:
       
        print("1. Calculate the transforming between the binary/decimal/octal/hexadecimal systems")
        print("2. Calculate Network Information")
        print("3. Exit")
        choice = input("Choose an option (1-2-3): ").strip()
        if choice == "1":
            display_menu1()
        elif choice == "2":
            display_menu2()
        elif choice == "3":
            print("see you next time!!")
            break
        else:
            print("Invalid option. Please choose 1 or 2.")
        os.system('cls')
def display_menu2():
    print("\n------------------ IP Address Planning Tool ------------------")
    print("1. Calculate Network Information")
    print("2. Back")
    while True:
        choice = input("Choose an option (1-2): ").strip()

        if choice == "1":
            ip_with_prefix = input("Enter an IP address with CIDR prefix (e.g., 192.168.1.0/24): ").strip()
            calculate_network_info(ip_with_prefix)
            print("Press any key to continue...")
            char = msvcrt.getch()
            break
        elif choice == "2":
            break
        else:
            print("Invalid option. Please choose 1 or 2.")

def calculate_network_info(ip_with_prefix):
    try:
        network = ipaddress.ip_network(ip_with_prefix, strict=False)

        print(f"\nNetwork: {network.network_address}")
        print(f"Netmask: {network.netmask}")
        print(f"Broadcast Address: {network.broadcast_address}")
        print(f"Total Hosts: {network.num_addresses}")
        print(f"Available Hosts: {network.num_addresses - 2} (excluding network and broadcast)")
        print(f"Usable Host Range: {list(network.hosts())[0]} - {list(network.hosts())[-1]}")
    except ValueError as e:
        print(f"Error: {e}. Please enter a valid CIDR notation (e.g., 192.168.1.0/24).")

def decimal_to_binary(decimal_number):
    return bin(decimal_number)[2:]

def decimal_to_octal(decimal_number):
    return oct(decimal_number)[2:]

def decimal_to_hexadecimal(decimal_number):
    return hex(decimal_number)[2:].upper()

def binary_to_decimal(binary_number):
    return int(binary_number, 2)

def octal_to_decimal(octal_number):
    return int(octal_number, 8)

def hexadecimal_to_decimal(hex_number):
    return int(hex_number, 16)

def display_menu1():
    print("\n*** Number System Conversion ***")
    print("1. Decimal to Binary")
    print("2. Decimal to Octal")
    print("3. Decimal to Hexadecimal")
    print("4. Binary to Decimal")
    print("5. Octal to Decimal")
    print("6. Hexadecimal to Decimal")
    print("7. Back")
    while True:
        choice = input("Choose an option (1-7): ").strip()
        if choice == "1":
            number = int(input("Enter a decimal number: "))
            print(f"Binary: {decimal_to_binary(number)}")
        elif choice == "2":
            number = int(input("Enter a decimal number: "))
            print(f"Octal: {decimal_to_octal(number)}")
        elif choice == "3":
            number = int(input("Enter a decimal number: "))
            print(f"Hexadecimal: {decimal_to_hexadecimal(number)}")
        elif choice == "4":
            binary = input("Enter a binary number: ").strip()
            print(f"Decimal: {binary_to_decimal(binary)}")
        elif choice == "5":
            octal = input("Enter an octal number: ").strip()
            print(f"Decimal: {octal_to_decimal(octal)}")
        elif choice == "6":
            hexadecimal = input("Enter a hexadecimal number: ").strip()
            print(f"Decimal: {hexadecimal_to_decimal(hexadecimal)}")
        elif choice == "7":
            break
        else:
            print("Invalid option. Please choose a number between 1 and 7.")
def main():
    ethent()
    display_menu()
    
if __name__ == "__main__":
    main()
