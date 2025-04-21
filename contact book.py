import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts = load_contacts()
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    save_contacts(contacts)
    print("Contact added successfully.")

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
    else:
        print("\nContact List:")
        for idx, contact in enumerate(contacts, 1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")

def search_contact():
    search = input("Enter name or phone number to search: ").lower()
    contacts = load_contacts()
    found = False
    for contact in contacts:
        if search in contact['name'].lower() or search in contact['phone']:
            print("\nFound Contact:")
            for key, value in contact.items():
                print(f"{key.capitalize()}: {value}")
            found = True
            break
    if not found:
        print("Contact not found.")

def update_contact():
    name = input("Enter the name of the contact to update: ").lower()
    contacts = load_contacts()
    for contact in contacts:
        if contact["name"].lower() == name:
            print("Leave blank to keep current value.")
            contact["phone"] = input(f"New phone [{contact['phone']}]: ") or contact["phone"]
            contact["email"] = input(f"New email [{contact['email']}]: ") or contact["email"]
            contact["address"] = input(f"New address [{contact['address']}]: ") or contact["address"]
            save_contacts(contacts)
            print("Contact updated.")
            return
    print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ").lower()
    contacts = load_contacts()
    new_contacts = [c for c in contacts if c["name"].lower() != name]
    if len(new_contacts) != len(contacts):
        save_contacts(new_contacts)
        print("Contact deleted.")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\n=== Contact Manager ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
