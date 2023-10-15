# Define product catalog as a dictionary
product_catalog = {
    'Boots': {
        '001': {'name': 'Leather Boots', 'price': 200},
        '002': {'name': 'Suede Boots', 'price': 150},
        '003': {'name': 'Ankle Boots', 'price': 180}
    },
    'Coats': {
        '004': {'name': 'Wool Coat', 'price': 500},
        '005': {'name': 'Parka Coat', 'price': 350},
        '006': {'name': 'Trench Coat', 'price': 450}
    },
    'Jackets': {
        '007': {'name': 'Leather Jacket', 'price': 575},
        '008': {'name': 'Denim Jacket', 'price': 250},
        '009': {'name': 'Bomber Jacket', 'price': 1000}
    },
    'Caps': {
        '010': {'name': 'Baseball Cap', 'price': 50},
        '011': {'name': 'Beanie', 'price': 40},
        '012': {'name': 'Bucket Hat', 'price': 45}
    }
}
# Define user and admin credentials as dictionaries
user_credentials = {'username': 'user', 'password': 'password'}
admin_credentials = {'username': 'admin', 'password': 'password'}
# Define cart as a dictionary
cart = {}
# Define function to display welcome message
def display_welcome_message():
    print('Welcome to the Demo Marketplace')
# Define function to handle user login
def user_login():
    username = input('Enter username: ')
    password = input('Enter password: ')
    if username == user_credentials['username'] and password == user_credentials['password']:
        print('Login successful')
        return True
    else:
        print('Invalid credentials')
        return False
# Define function to handle admin login
def admin_login():
    username = input('Enter username: ')
    password = input('Enter password: ')
    if username == admin_credentials['username'] and password == admin_credentials['password']:
        print('Login successful')
        return True
    else:
        print('Invalid credentials')
        return False
# Define function to display product catalog
def display_catalog():
    for category, products in product_catalog.items():
        print(category)
        print('---------------------')
        for product_id, product_details in products.items():
            print(product_id, product_details['name'], product_details['price'])
        print()
# Define function to add item to cart
def add_to_cart():
    product_id = input('Enter product ID: ')
    quantity = int(input('Enter quantity: '))
    if product_id in cart:
        cart[product_id] += quantity
    else:
        cart[product_id] = quantity
    print('Item added to cart')
# Define function to remove item from cart
def remove_from_cart():
    product_id = input('Enter product ID: ')
    if product_id in cart:
        del cart[product_id]
        print('Item removed from cart')
    else:
        print('Item not in cart')
# Define function to display cart contents
def display_cart():
    if cart:
        print('Cart contents:')
        print('--------------')
        for product_id, quantity in cart.items():
            product_details = None
            for category, products in product_catalog.items():
                if product_id in products:
                    product_details = products[product_id]
                    break
            if product_details:
                print(product_id, product_details['name'], product_details['price'], quantity)
        print('--------------')
        total_price = sum(product_details['price'] * quantity for product_id, quantity in cart.items())
        print('Total price:', total_price)
    else:
        print('Cart is empty')
# Define function to handle payment checkout
def checkout():
    payment_option = input('Select payment option (Net banking, PayPal, UPI, etc.): ')
    if payment_option:
        print('Your order is successfully placed')
    else:
        print('Please select a payment option')
# Define function to add new product to catalog
def add_product():
    if admin_login():
        category = input('Enter category: ')
        product_id = str(len(product_catalog[category]) + 1).zfill(3)
        name = input('Enter product name: ')
        price = int(input('Enter product price: '))
        product_catalog[category][product_id] = {'name': name, 'price': price}
        print('Product added to catalog')
# Define function to modify existing product in catalog
def modify_product():
    if admin_login():
        product_id = input('Enter product ID: ')
        if product_id in cart:
            name = input('Enter new product name (leave blank to keep the same): ')
            price = input('Enter new product price (leave blank to keep the same): ')
            if name:
                product_catalog[category][product_id]['name'] = name
            if price:
                product_catalog[category][product_id]['price'] = price
            print('Product modified')
        else:
            print('Product not found in catalog')
# Define function to remove product from catalog
def remove_product():
    if admin_login():
        product_id = input('Enter product ID: ')
        if product_id in cart:
            del product_catalog[category][product_id]
            print('Product removed from catalog')
        else:
            print('Product not found in catalog')
# Define function to add new category to catalog
def add_category():
    if admin_login():
        category = input('Enter new category: ')
        product_catalog[category] = {}
        print('Category added to catalog')
# Define function to remove category from catalog
def remove_category():
    if admin_login():
        category = input('Enter category to remove: ')
        if category in product_catalog:
            del product_catalog[category]
            print('Category removed from catalog')
        else:
            print('Category not found in catalog')
# Main program loop
while True:
    display_welcome_message()
    print('1. Login')
    print('2. View catalog')
    print('3. Add item to cart')
    print('4. Remove item from cart')
    print('5. View cart')
    print('6. Checkout')
    print('7. Add product to catalog')
    print('8. Modify product in catalog')
    print('9. Remove product from catalog')
    print('10. Add category to catalog')
    print('11. Remove category from catalog')
    print('12. Exit')
    choice = input('Enter choice: ')
    if choice == '1':
        user_type = input('Enter user type (user/admin): ')
        if user_type == 'user':
            user_login()
        elif user_type == 'admin':
            admin_login()
        else:
            print('Invalid user type')
    elif choice == '2':
        display_catalog()
    elif choice == '3':
        add_to_cart()
    elif choice == '4':
        remove_from_cart()
    elif choice == '5':
        display_cart()
    elif choice == '6':
        checkout()
    elif choice == '7':
        add_product()
    elif choice == '8':
        modify_product()
    elif choice == '9':
        remove_product()
    elif choice == '10':
        add_category()
    elif choice == '11':
        remove_category()
    elif choice == '12':
        break
    else:
        print('Invalid choice')