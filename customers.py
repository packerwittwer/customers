import firebase_admin, sys, time, re
from firebase_admin import credentials, firestore

cred = credentials.Certificate('customers.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
orders = db.collection('orders').get()

def main():
    # CREATE A MENU:
    while True:
        print('Select an option:\n[1] Display All Orders\n[2] Add New Order\n[3] Update An Order\n[4] Search By Name\n[5] Delete Order\n[0] Quit\n-> ', end='')
        try:
            choice = int(input())
            if choice in range(0, 6):
                # run the specified function
                choice_dict[choice]()

            else:
                print("Invalid option")
        except ValueError:
            print("Invalid option, please enter a number.")
            # time.sleep(1)
        input('Press \'enter\' to continue...\n')

# FUNCTIONS
# 1 display all orders with the customer name first
def display():
    displayed = []
    orders = db.collection('orders').get()
    for i, order in enumerate(orders, start=1):
        results = order.to_dict()
        # '**results' is dictionary unpacking/spread. it takes all the remaining values from results (after the 'name' key value pair was removed) and adds them to the order_dict dictionary
        ordered_dict = {'name' : results.pop('name'), **results}
        print(f'[{i}] {ordered_dict}')
        displayed.append(order.id)

    return displayed

# 2 add new order
def add_order():
    new_order = {}
    # create a list of options to add to the order
    order_options = ['name', 'type', 'size', 'liner', 'liner color', 'spring steel', 'scale color', 'pendant', 'drawstring color']
    for item in order_options:
        field = input(f'{item}: ').lower()
        new_order.update({item : field})
    
    db.collection('orders').add(new_order)

# 3 update an order
def update_order():
    display_choice = (input('Do you want to:\n[1] Display all orders\n[2] Search for a name\n'))
    if not display_choice.isdigit():
        print('Invalid choice')
    else:
        if not orders:
            print('No orders available')
            return

        display_choice = int(display_choice)
        if display_choice not in [1, 2]:
            print('Invalid choice')
            return
            
        if display_choice == 1:
            order_ids = display()
        else:
            order_ids = search()

        try:
            to_be_changed = int(input('Which order do you want to change? '))
        except Exception as e:
            print(f'Error: {e}')
            return
        
        if not order_ids:
            print('No results')
            return
        try:
            selected_order_id = order_ids[to_be_changed - 1]
            field = input('Enter the field to update (e.g. name): ').lower().replace(' ', '_')
            new_status = input('Enter the new value: ').lower()
            db.collection('orders').document(selected_order_id).update({field: new_status})
            change = db.collection('orders').document(selected_order_id).get()
            print(f'Order updated:\n{change.to_dict()}')
        except Exception as e:
            print(f'Error: {e}')

# 4 search for an order by customer name
def search():
    displayed = []
    try:
        name = input('Search: ').lower()
        searched = db.collection('orders').where('name', '==', name).get()
        if searched:
            for i, customer in enumerate(searched, start=1):
                results = customer.to_dict()
                ordered_dict = {'name' : results.pop('name'), **results}
                print(f' [{i}] {ordered_dict}')
                displayed.append(customer.id)
        else:
            print('No results')
    except:
        print('No results')
    
    return displayed
    

# 5 delete an order
def delete_order():
    doc_ids = []
    try:
        name = input('Search for name: ').lower()
        searched = db.collection('orders').where('name', '==', name).get()
        if searched:
            for i, customer in enumerate(searched, start=1):
                results = customer.to_dict()
                ordered_dict = {'name' : results.pop('name'), **results}
                doc_ids.append(customer.id)
                print(f'[{i}] {ordered_dict}')

            num = int(input('Which item do you want to delete? ')) - 1
            if num in range(len(doc_ids)):
                order_id = doc_ids[num]
                db.collection('orders').document(order_id).delete()
        else:
            print('No results')
        print()
    except Exception as e:
        print(f'Error: {e}')


choice_dict = {1 : display,
               2 : add_order,
               3 : update_order,
               4 : search,
               5 : delete_order,
               0 : sys.exit}


if __name__ == '__main__':
    main()





# test adding an order
    # test_order = {'name' : "jonny",
    #                  'type' : 'scale',
    #                  'size' : 'medium',
    #                  'color' : 'black blue green speckled',
    #                  'liner' : 'true'}
    # db.collection('orders').add(test_order)
# test deleting an order
    # id = 'vxMiyfBpEQFmIveJqfPI'
    # db.collection('orders').document(id).delete()