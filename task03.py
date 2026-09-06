import json

try:
    with open("contacts.json", "r") as file:
        contacts = json.load(file)
except:
    contacts = []

while True:
    print("\n--- Contact Book ---")
    print("1. Add contact")
    print("2. List contacts")
    print("3. Search contact")
    print("4. Edit contact")
    print("5. Delete contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }

        contacts.append(contact)

        with open("contacts.json", "w") as file:
            json.dump(contacts, file, indent=4)

        print("Contact added successfully!")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            print("\n--- Contacts ---")

            for contact in contacts:
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                print()

    elif choice == "3":
        search = input("Enter name to search: ")

        found = False

        for contact in contacts:
            if search.lower() in contact["name"].lower():
                print("\nName:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                found = True

        if not found:
            print("No contact found.")

    elif choice == "4":
        name = input("Enter name of contact to edit: ")

        found = False

        for contact in contacts:
            if contact["name"].lower() == name.lower():
                contact["phone"] = input("Enter new phone: ")
                contact["email"] = input("Enter new email: ")
                found = True

                with open("contacts.json", "w") as file:
                    json.dump(contacts, file, indent=4)

                print("Contact updated successfully!")
                break

        if not found:
            print("No contact found.")

    elif choice == "5":
        name = input("Enter name of contact to delete: ")

        found = False

        for contact in contacts:
            if contact["name"].lower() == name.lower():
                contacts.remove(contact)

                with open("contacts.json", "w") as file:
                    json.dump(contacts, file, indent=4)

                print("Contact deleted successfully!")
                found = True
                break

        if not found:
            print("No contact found.")

    elif choice == "6":
        print("Goodbye!")
        break