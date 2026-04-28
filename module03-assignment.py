# Module 3 Assignment: String Manipulation, User Input, and Formatted Output

# Welcome message
print("=" * 50)
print("CUSTOMER ORDER PROCESSING SYSTEM")
print("=" * 50)
print("Please enter the following information:\n")

# TODO: Collect customer information
# Use input() with the exact prompts specified
# Apply .strip() and appropriate formatting
customer_name = input("Enter customer name: ").strip().title()
customer_email = input("Enter customer email: ").strip().lower()
# TODO: Collect order information
# Remember to strip whitespace from all inputs
product_name = input("Enter product name: ").strip().title()
quantity = int(input("Enter quantity: ").strip())
unit_price = float(input("Enter unit price: ").strip())
# TODO: Process the information
# 1. Convert quantity to int and unit_price to float
quantity = int(quantity)
unit_price = float(unit_price)
# Make sure quantity and unit_price are both positive numbers 
if quantity < 1 :
    print("The Quantity HAS TO BE a positive number, redo please and make sure it is positive :)")
    exit("restart to do again")
if unit_price < 1 :
    print("The Unit price HAS TO BE a positive number, redo and make sure it is positive :)")
    exit("restart to do again")
# 2. Calculate subtotal = quantity * unit_price
subtotal = quantity * unit_price
# If the quantity number is >= 10 then do a discount of 10% to the subtotal or else its just 0
discount = subtotal * 0.10 if quantity >= 10 else 0
# 3. Calculate tax_amount = (subtotal - discount) * 0.085 only if quantity >= 10 if not then discount is just 0
tax_amount = subtotal * 0.085
# 4. Calculate order_total = (subtotal + tax_amount) - discount only if quantity >= 10 if not then discount is just 0
order_total = subtotal + tax_amount
# TODO: Display order summary
# Use f-strings to format the output as shown in the example
print("==" * 13 )
print("ORDER SUMMARY")
print("=" * 13)
print(f"Customer: {customer_name}") 
print(f"Email: {customer_email}") 
print(f"Product: {product_name}") 
print(f"Quantity: {quantity}") 
print(f"Unit Price: ${unit_price:,.2f}")
print(f"Subtotal: ${subtotal:,.2f}")
print(f"Tax (8.5%): ${tax_amount:,.2f}")
print(f"Order Total: ${order_total:,.2f}")