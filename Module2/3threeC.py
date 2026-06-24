contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Gabriel": "555-9999"
}

name = input("Enter a name: ")
if name in contacts:
    print(f"{name}'s number is {contacts[name]}")
else:
    print("Contact not found.")

response = input("Add a new contact? (yes/no): ").lower()
if response == "yes":
    new_name = input("Enter name: ")
    new_number = input("Enter phone number: ")
    contacts[new_name] = new_number
    print(f"Contact added. Contacts: {contacts}")
else:
    print("No new contact added.")