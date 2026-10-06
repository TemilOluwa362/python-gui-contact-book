import tkinter as tk
contacts = {}
while True:
    print("----- MENU -----")
    print("1. Add a contact. ")
    print("2. View contacts. ")
    print("3. Search contacts. ")
    print("4. Delete contacts. ")
    print("5. Exit. ")
    print("----------------")
    try:
        choice = int(input("Select an option: "))
    except ValueError:
        print("Invalid! Enter a number.")
        continue
    if choice == 1:
        name = input("Enter contact name: ").title()
        phone_number = input("Enter contact number: ") 
        phone_number = "+234" + phone_number[1:]
        email = input("Enter contact email: ")
        contacts[name] = {"Phone": phone_number, "Email": email}
        print("Contact added!")
    elif choice == 2:
        if not contacts:
            print("No contacts added yet.")
        else:
            for name, contact_info in contacts.items():
                print(name)
                print(contact_info["Phone"])
                print(contact_info["Email"]) 
    elif choice == 3:
        contact_search = input("Enter the name to be searched: ").title()
        if contact_search in contacts:
            print(contact_search)
            print(contacts[contact_search]["Phone"])
            print(contacts[contact_search]["Email"])
        else:
            print("Contact not found!")
    elif choice == 4:
        delete_contact = input("What contact do you want to delete: ").title()
        if delete_contact in contacts:
            del contacts[delete_contact]
            print("Contact deleted!")
        else:
            print("Contact not found!")
    elif choice == 5:
        break
    else:
        print("Invalid option! Choose from options 1-5")