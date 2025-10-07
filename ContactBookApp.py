import json
import re

# Load contacts from file
def load_contacts():
    try:
        with open("contacts.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Save contacts to file
def save_contacts():
    with open("contacts.json", "w") as f:
        json.dump(contacts, f, indent=4)

# Input validators
def valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def valid_mobile(mobile):
    return mobile.isdigit() and len(mobile) in [10, 11, 12]

# ----------------- MAIN PROGRAM -----------------
contacts = load_contacts()

while True:
    print("\n===== Contact Book App =====")
    print("1. Create Contact")
    print("2. View Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Count Contacts")
    print("7. View All Contacts")
    print("8. Exit")

    choice = input("Enter your choice = ").strip()

    # 1️⃣ CREATE
    if choice == "1":
        name = input("Enter Name = ").strip()
        if name in contacts:
            print(f"Contact name '{name}' already exists!")
        else:
            age = input("Enter Age = ").strip()
            email = input("Enter Email = ").strip()
            mobile = input("Enter Mobile Number = ").strip()

            if not age.isdigit():
                print("Invalid age. Please enter a number.")
                continue
            if not valid_email(email):
                print("Invalid email format.")
                continue
            if not valid_mobile(mobile):
                print("Invalid mobile number.")
                continue

            contacts[name] = {"age": int(age), "email": email, "mobile": mobile}
            save_contacts()
            print(f"Contact '{name}' created successfully!")

    # 2️⃣ VIEW
    elif choice == "2":
        name = input("Enter contact name to view = ").strip()
        if name in contacts:
            c = contacts[name]
            print("\n--- Contact Details ---")
            print(f"Name   : {name}")
            print(f"Age    : {c['age']}")
            print(f"Email  : {c['email']}")
            print(f"Mobile : {c['mobile']}")
        else:
            print("Contact not found.")

    # 3️⃣ UPDATE
    elif choice == "3":
        name = input("Enter contact name to update = ").strip()
        if name in contacts:
            age = input("Enter updated Age = ").strip()
            email = input("Enter updated Email = ").strip()
            mobile = input("Enter updated Mobile Number = ").strip()

            if not age.isdigit() or not valid_email(email) or not valid_mobile(mobile):
                print("Invalid input. Please enter correct details.")
                continue

            contacts[name] = {"age": int(age), "email": email, "mobile": mobile}
            save_contacts()
            print(f"Contact '{name}' updated successfully!")
        else:
            print("Contact not found.")

    # 4️⃣ DELETE
    elif choice == "4":
        name = input("Enter contact name to delete = ").strip()
        if name in contacts:
            del contacts[name]
            save_contacts()
            print(f"Contact '{name}' deleted successfully!")
        else:
            print("Contact not found.")

    # 5️⃣ SEARCH
    elif choice == "5":
        search_name = input("Enter contact name or part of it to search = ").strip().lower()
        found = False
        for name, c in contacts.items():
            if search_name in name.lower():
                print("\n--- Contact Found ---")
                print(f"Name   : {name}")
                print(f"Age    : {c['age']}")
                print(f"Email  : {c['email']}")
                print(f"Mobile : {c['mobile']}")
                found = True
        if not found:
            print("No contact found with that name.")

    # 6️⃣ COUNT
    elif choice == "6":
        print(f"Total contacts in your book: {len(contacts)}")

    # 7️⃣ VIEW ALL CONTACTS
    elif choice == "7":
        if contacts:
            print("\n--- All Contacts ---")
            for name, c in contacts.items():
                print(f"\nName   : {name}")
                print(f"Age    : {c['age']}")
                print(f"Email  : {c['email']}")
                print(f"Mobile : {c['mobile']}")
        else:
            print("No contacts found.")

    # 8️⃣ EXIT
    elif choice == "8":
        print("Goodbye... Closing the program.")
        break

    else:
        print("Invalid choice! Please enter a valid option.")
