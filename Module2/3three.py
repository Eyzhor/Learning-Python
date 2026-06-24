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

print("Add a new contact? (yes/no)")
response = input().lower()
if response == "yes":
    new_name = input("Enter the name of the new contact: ")
    while True:
        try:
            new_number = int(input("Enter the phone number of the new contact: "))
        except ValueError:
            print("Invalid phone number. Please enter a valid number.")
        else:
            contacts[new_name] = new_number
            print("Contact added.")
            print(f"Contacts: {contacts}")
            break
        
if response == "no":
    print("No new contact added.")