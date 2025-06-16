# ===================================
# Simplified Shop Management / Self Checkout Machine
# ===================================
# Developed by. Reyner Thaddeus Purwanto
# JCDS - 0612


# /************************************/

# /===== Data Model =====/
# Create your data model here
log = [] # Example data model


# /===== Feature Program =====/
# Create your feature program here
def read():
    """Function for reading the data
    """

    if not log:
        print("No purchase recorded yet.")
    else:
        print("== List of Purchases ==")
        print("-----------------------")
        print("Purchase ID    |Item    |Quantity    |Total Price")
        print("-----------------------")
            # TODO: Gunakan loop untuk menampilkan semua film
            # Format: "Judul (Genre, Tahun)"
        for purchase in log:
            print(f"{purchase['purchase id']}    |{purchase['item']}    |{purchase['qty']}    |{purchase['total price']}")
    
    return

def create():
    """Function for creating the data
    """
    confirmation = "n"
    while confirmation == "n":
        print("\n== Add Customer Purchase ==")
        purchase_id = len(log) + 1
        item        = str(input("Item purchased: ")).lower().strip()
        qty         = int(input("Quantity purchased: "))
        price       = int(input("Price for item: "))
        total_price = qty * price
        # while price <=0: # Shorten into another function later
        #     print("Enter positive amount")
        #     price   = int(input("Price for item: "))
        print(f"The purchase is {qty} {item}, with total amount of Rp.{total_price}.")
        confirmation = str(input("Are you sure (y/n): ")).lower().strip()
    
    new_purchase = {"purchase id": purchase_id, "item": item, "qty": qty, "price": price, "total price": total_price}
    log.append(new_purchase)
    print("Purchase has been added!")
    return

def update():
    """Function for updating the data
    """
    return

def delete():
    """Function for deleting the data
    """
    return

# /===== Main Program =====/
# Create your main program here
def main():
    """Function for main program
    """
    print("\n=== Simple Shop Management ===")
    print("1. List all purchase")
    print("2. Add a purchase")
    print("3. Edit a purchase")
    print("4. Delete a purchase")
    input_user = input("\nWhat do you want to do: ")
    if input_user == "1":
        read()
    elif input_user == "2":
        create()
    elif input_user == "3":
        update()
    elif input_user == "4":
        delete()
    else:
        print("Input is not valid !")


if __name__ == "__main__":
    main()