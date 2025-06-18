# ===================================
# Simplified Shop Management / Self Checkout Machine
# ===================================
# Developed by. Reyner Thaddeus Purwanto
# JCDS - 0612


# /************************************/
from tabulate import tabulate as tb
import csv
from datetime import datetime as dt
# /************************************/

# /===== Data Model =====/
# Create your data model here
log = [
    {"purchase id": 1, "item": "glass", "quantity": 2, "price": 15000, "total amount": 30000},
    {"purchase id": 2, "item": "pen", "quantity": 3, "price": 7500, "total amount": 22500},
    {"purchase id": 3, "item": "umbrella", "quantity": 1, "price": 20000, "total amount": 20000},
    {"purchase id": 4, "item": "note book", "quantity": 5, "price": 12000, "total amount": 60000},
    {"purchase id": 5, "item": "utensil set", "quantity": 1, "price": 30000, "total amount": 30000}
] # Example data model


# /===== Feature Program =====/
# Create your feature program here
def read():
    """Function for reading the data
    """

    if not log:
        print("No purchase recorded yet.")
        return

    search_method = validation("Display all purchases (A) or search by Purchase ID (S)?: ", str).lower()
    if search_method == "s":
        try:
            search_id = validation("Enter Purchase ID: ", int)
        except:
            print("Wrong input (not ID), showing all purchases")
            selected_data = log
        else:
            selected_data = [selected_id for selected_id in log if selected_id["purchase id"] == search_id]
    else:
        selected_data = log

    print("\n== List of Purchases ==")
    print(tb(selected_data, headers = "keys", tablefmt = "github", numalign = "right", stralign = "left"))
    
    return

def create():
    """Function for creating the data
    """
    create_confirmation = "n"
    while create_confirmation == "n":
        print("\n== Add Customer's Purchase ==")
        purchase_id = len(log) + 1
        item        = validation("Item purchased: ", str).lower()
        qty         = validation("Quantity purchased (input whole numbers): ", int)
        price       = validation("Item price (input whole numbers): ", int)
        total_amount = qty * price
        # while price <=0: # Shorten into another function later
        #     print("Enter positive amount")
        #     price   = int(input("Price for item: "))
        print(f"The purchase is {qty} {item}, with total amount of Rp.{total_amount}.")
        create_confirmation = str(input("Are you sure (y/n)/(cancel): ")).lower().strip()
        if create_confirmation == "n":
            create_confirmation == "n"
        elif create_confirmation == "y":
            create_confirmation == "y"
            new_purchase = {"purchase id": purchase_id, "item": item, "quantity": qty, "price": price, "total amount": total_amount}
            log.append(new_purchase)
            print("Purchase has been added!")
        else:
            break
    return

def create_loop():
    """Function to check if the user wants to finish creating a purchase
    """
    print("\n== Additional Purchase ==")
    finish_create = input("Add another purchase? (y/n): ").lower().strip()
    if finish_create == "n":
        return True
    elif finish_create == "y":
        return False
    else:
        print("Invalid input")

def update():
    """Function for updating the data
    """
    print("\n== Update Customer's Purchase ==")
    change_purchase = validation("Type the purchase id you wish to change: ", int)
    found = False

    for purchase in log:
        if change_purchase == purchase["purchase id"]:
            found = True
            change_confirmation = "n"
            print(tb([purchase], headers="keys", tablefmt="github", numalign="right", stralign="left"))
            
            while change_confirmation == "n":
                print("\nChange the purchase below")
                new_item = validation("Add new item: ", str).lower()
                new_quantity = validation("Add new quantity: ", int)
                new_price = validation("Add new price: ", int)
                new_total_amount = new_price * new_quantity

                print("\nNew Changes")
                print("Item", new_item)
                print("Quantity: ", new_quantity)
                print("Price: ", new_price)
                print("Amount: ",new_total_amount)

                change_confirmation = input("Are you sure of the change? (y/n): ").lower().strip()
                if change_confirmation == "n":
                    cancel = input("Do you wish to cancel and exit change? (y/n): ").lower().strip()
                    if cancel == "y":
                        return
                elif change_confirmation == "y":
                    purchase["item"] = new_item
                    purchase["quantity"] = new_quantity
                    purchase["price"] = new_price
                    purchase["total amount"] = new_total_amount
                    return

            
    if not found:
        print("Purchase ID not found, please refer to recorded purchases or recheck your ID.")

    return

def delete():
    """Function for deleting the data
    """

    print("\n== Delete Customer's Purchase ==")
    delete_purchase = int(input("Type the purchase id you wish to delete: "))
    found = False

    for purchase in log:
        if delete_purchase == purchase["purchase id"]:
            found = True
            print(tb([purchase], headers="keys", tablefmt="github", numalign="right", stralign="left"))
            
            delete_confirmation = input("Are you sure in deleting this purchase log? (y/n): ").lower().strip()
            if delete_confirmation == 'y':
                log.remove(purchase)
                print(f"Purchase log with ID of {delete_confirmation} has been deleted")
            else:
                print("Delete is cancelled.")
            return

    return

def exit():
    """Function for exiting the program
    """
    print("\n == Exit Confirmation ==")
    exit_confirmation = input("Are you sure you are done? (y/n): ").lower().strip()
    if exit_confirmation == "y":
        return False

def validation(message, type_convertion):
    """Function for validating input
    """
    while True:
        subtitu = input(message).strip()
        try:
            convert = type_convertion(subtitu)
            return convert
        except:
            print(f"Input invalid, make sure you input {type_convertion}!")
        

# /===== Main Program =====/
# Create your main program here
def main():
    program = True
    while program == True:
        """Function for main program
        """
        print("\n=== Simple Shop Management ===")
        print("1. List all purchase")
        print("2. Add a purchase")
        print("3. Edit a purchase")
        print("4. Delete a purchase")
        print("5. Finish the purchases")
        input_user = input("\nWhat do you want to do: ")
        if input_user == "1":
            read()
        elif input_user == "2":
            finish_create = False
            while finish_create == False:   
                create()
                finish_create = create_loop()
        elif input_user == "3":
            update()
        elif input_user == "4":
            delete()
        elif input_user == "5":
            program = exit()
        else:
            print("Input is not valid !")


if __name__ == "__main__":
    main()