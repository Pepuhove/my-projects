class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contact_list(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone_number}")

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term in (contact.name or contact.phone_number)]
        if results:
            for result in results:
                print(f"Name: {result.name}, Phone: {result.phone_number}")
        else:
            print("Contact not found.")

    def update_contact(self, old_name, new_contact_details):
        for contact in self.contacts:
            if contact.name == old_name:
                contact.name = new_contact_details.get("name", contact.name)
                contact.phone_number = new_contact_details.get("phone_number", contact.phone_number)
                contact.email = new_contact_details.get("email", contact.email)
                contact.address = new_contact_details.get("address", contact.address)
                print(f"Contact '{old_name}' updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, contact_name):
        self.contacts = [contact for contact in self.contacts if contact.name != contact_name]
        print(f"Contact '{contact_name}' deleted successfully.")


def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter Name: ")
            phone_number = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_manager.add_contact(new_contact)

        elif choice == "2":
            contact_manager.view_contact_list()

        elif choice == "3":
            search_term = input("Enter name or phone number to search: ")
            contact_manager.search_contact(search_term)

        elif choice == "4":
            old_name = input("Enter the name of the contact to update: ")
            new_name = input("Enter new name (press enter to keep the current name): ")
            new_phone = input("Enter new phone number (press enter to keep the current phone number): ")
            new_email = input("Enter new email (press enter to keep the current email): ")
            new_address = input("Enter new address (press enter to keep the current address): ")

            new_contact_details = {
                "name": new_name,
                "phone_number": new_phone,
                "email": new_email,
                "address": new_address,
            }
            contact_manager.update_contact(old_name, new_contact_details)

        elif choice == "5":
            contact_name = input("Enter the name of the contact to delete: ")
            contact_manager.delete_contact(contact_name)

        elif choice == "6":
            print("Exiting Contact Management System.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
