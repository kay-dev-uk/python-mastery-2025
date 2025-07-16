
def contact_book():
    list_of_contacts = {}
    def add_contact():
        contact_name = input('Name: ')
        contact_phone = input('Phone: ')
        list_of_contacts[contact_name] = contact_phone
        print(contact_name + ' was saved successfully!')
        display_menu()

    def view_contacts():
        for k,v in list_of_contacts.items():
            print('Name: ' + k + '\nPhone: ' + v + '\n--- --- ---')
        display_menu()
        
    def display_menu():
        print('1. Add Contact\n2. View All Contacts\n3. Quit')
        user_selection = input('Please, select one of the options from above: ')
        if user_selection == '1':
            add_contact()
        elif user_selection == '2':
            view_contacts()
        elif user_selection == '3':
            print('Goodbye')
            return
            
    display_menu()

contact_book()
