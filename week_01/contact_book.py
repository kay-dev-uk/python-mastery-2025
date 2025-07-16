import csv
FILENAME = "contacts.csv"

def display_menu():
    # Displays the menu
    print('1. Add Contact\n2. View All Contacts\n3. Search for Contact\n4. Quit')
        

def add_contact(contacts):
    # Adds a new contact to the dictionary
    contact_name = input('Name: ')
    contact_phone = input('Phone: ')
    contacts[contact_name] = contact_phone
    print(f"'{contact_name}' was saved successfully!")

def view_contacts(contacts):
    # Displays all contacts
    if not contacts:
        print("Contact book is empty.")
        return
    for name,phone in contacts.items():
        print('Name: ' + name + '\nPhone: ' + phone + '\n--- --- ---')

def load_contacts():
    pass

def save_contacts(contacts):
    with open(FILENAME, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'Phone Number'])
        for name,phone in contacts.items():
            writer.writerow([name, phone])
         
def main():
    contacts = {}
    while True:
        display_menu()
        user_selection = input('Please, select (1-4): ')
        if user_selection == '1':
            add_contact(contacts)
        elif user_selection == '2':
            view_contacts(contacts)
        elif user_selection == '3':
            print('Search not yet implemented')
        elif user_selection == '4':
            print('Goodbye')
            save_contacts(contacts)
            break
        else:
            print('Invalid choice. Please, enter a number between 1 and 4')


if __name__ == "__main__":
    main()
