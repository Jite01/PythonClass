def display_menu():
	welcometext = """ 
	Welcome to Jessica's E-store:
	1 --> View Products
	2 --> Add to Cart
	3 --> Remove from Cart
	4 --> View Cart
	5 --> Checkout
	6 --> Exit
	"""
	
	return welcometext
	print(welcometext)

def menu_response_switch():
	display_menu() 
	menu_response = int(input())
	match menu_response:
		case 1: view_products()
		case 2: view_cart()
		case 3: remove_from_cart()
		case 4: view_cart()
		case 5: checkout()
		case 6: exit()


menu_response_switch()

def view_products():
	cart = []
	display_products()

	

		
	
	add_response = int(input())
	
	match view_options:
		case 1: add_to_cart(caseproduct[add_response])
		case 2: add_to_cart(caseproduct[add_response])
		case 3: add_to_cart(caseproduct[add_response])
	
def display_products():
	products = [[],[[]],[[]],[[]]]
	products = ["",["Laptop",[1000]],["Phone",[500]],["HeadPhone",[100]]]
	print("What Would you Like To Purchase?\n", product[1],"-->100\n", product[2]," --> $500\n", product[3]," --> $100\n")

	
def add_to_cart(index: int):
	cart.append(add_response)
	print(f"{product[add_response]}","has been added to your cart")

def view_cart():
	if len(cart) == 0:
		print("Your Cart is Empty...")
	print(cart)
	return cart

def remove_from_cart(): 
	print(cart)
	print("what would you like to remove from cart?")
	
	
	
	

	

	