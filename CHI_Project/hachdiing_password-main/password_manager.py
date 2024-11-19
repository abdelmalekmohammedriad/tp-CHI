import getpass
from hash_utils import hash_password, save_data, load_data
from display_utils import display_title


def set_master_password():
    display_title("Set Master Password")
    username = input("Enter username: ").strip() 

    while True:
        master_password = getpass.getpass("Enter new master password: ")
        confirm_password = getpass.getpass("Confirm master password: ")
        
        if master_password == confirm_password:
            hashed_master = hash_password(master_password)
            data = load_data('master_password.json')  
            data[username] = hashed_master  
            save_data(data, 'master_password.json')  
            print(f"✅ Master password set successfully for user '{username}'.")
            break
        else:
            print("⚠️ Passwords do not match. Please try again.")


def verify_master_password():
    data = load_data('master_password.json')  
    if not data:
        print("⚠️ No users found. Please register first.")
        return False
    
    username = input("Enter username: ").strip()  
    master_password = getpass.getpass("Enter master password: ")
    hashed_master = hash_password(master_password)
    
    if data.get(username) == hashed_master:  
        print("✅ Access granted.")
        return True
    else:
        print("❌ Incorrect username or password. Access denied.")
        return False


def choose_action():
    display_title("Password Manager")
    while True:
        print("[1] ➤ Register new user (First time setting master password)")
        print("[2] ➤ Login with existing master password")
        choice = input("Choose an option: ").strip()
        
        if choice == '1':
            set_master_password()
            return True
        elif choice == '2':
            if verify_master_password():
                return True
            else:
                print("❌ Incorrect master password. Please try again.")
        else:
            print("⚠️ Invalid option. Please choose a valid option.")


if __name__ == "__main__":
    choose_action()
