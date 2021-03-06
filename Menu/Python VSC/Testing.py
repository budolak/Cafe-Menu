# Testing

import csv
import random
from os import path

user_orderlist = []
absolute_path = path.abspath(path.curdir)


def table_reservation():
    total_tables = 20
    reserved_tables = random.randint(0, 21)
    empty_tables = total_tables - reserved_tables
    if total_tables == reserved_tables:
        print("Sorry, All the tables are reserved at the moment.\n")
    elif reserved_tables < total_tables:
        print("The number of empty tables are {} out of {} at the Restaurant.\n".format(empty_tables, total_tables))
    return empty_tables


def user_order_ftn():
    add = input(
        "\nWhich item do u want to add to your Order List, \"OR\" go back to menu(M/m)? ")
    return add


def menu_starters():
    with open(path.join(absolute_path, "menu_starters.csv"), "r") as rf:
        csv_reader = csv.DictReader(rf, delimiter=",")
        print()
        print("Starters Menu".center(25))
        print(F"No. \t Item \t\t Price")
        for line in csv_reader:
            print(line["No."]+")", line["Item"], "\t", line["Price"])


def menu_steaks():
    with open(path.join(absolute_path, "menu_steaks.csv"), "r") as rf:
        csv_reader = csv.DictReader(rf, delimiter=",")
        print()
        print("Steak Menu".center(25))
        print("No. \t Item \t\t\t Price")
        for line in csv_reader:
            if line["No."] == "1":
                print(line["No."]+")", line["Item"], "\t", line["Price"])
            else:
                print(line["No."]+")", line["Item"], "\t\t", line["Price"])


def menu_burgers():
    with open(path.join(absolute_path, "menu_burgers.csv"), "r") as rf:
        csv_reader = csv.DictReader(rf, delimiter=",")
        print()
        print("Burgers Menu".center(25))
        print("No. \tItem\t\t\tPrice")
        for line in csv_reader:
            if line["No."] == "1":
                print(line["No."]+")", line["Item"], "\t", line["Price"])
            else:
                print(line["No."]+")", line["Item"], "\t\t", line["Price"])


def menu_pizza():
    with open(path.join(absolute_path, "menu_pizza.csv"), "r") as rf:
        csv_reader = csv.DictReader(rf)
        print()
        print("Pizza Menu".center(25))
        print("No. \t Item\t  S   M   L")
        for line in csv_reader:
            print(line["No."]+")", line["Item"], line["Small Size Price"],
                  line["Medium Size Price"], line["Large Size Price"])


def menu_drinks():
    with open(path.join(absolute_path, "menu_drinks.csv"), "r") as rf:
        csv_reader = csv.DictReader(rf, delimiter=",")
        print()
        print("Drinks Menu".center(25))
        print("No. \tItem \t\tPrice")
        for line in csv_reader:
            if line["No."] == "4":
                print(line["No."]+")", line["Item"], "\t", line["Price"])
            elif line["No."] == "5":
                print(line["No."]+")", line["Item"], "", line["Price"])
            else:
                print(line["No."]+")", line["Item"], "\t\t", line["Price"])


valid_quantity = 0


def inventory(file_to_open, item_selected):
    global valid_quantity
    valid_quantity = 0

    if file_to_open == 1:
        with open(path.join(absolute_path, "menu_starters.csv"), "r", newline="") as rf:
            csv_reader = csv.DictReader(rf, delimiter=",")
            csv_reader_list = list(csv_reader)

        with open(path.join(absolute_path, "menu_starters.csv"), "w", newline="") as wf:
            headers = ["No.", "Item", "Price", "Inventory"]
            csv_writer = csv.DictWriter(wf, fieldnames=headers, delimiter=",")
            csv_writer.writeheader()
            for line in range(len(csv_reader_list)):
                if csv_reader_list[line]["No."] == item_selected:
                    while True:
                        try:
                            item_quantity = int(input("Quantity of the \"{}\" item: ".format(csv_reader_list[line]["Item"])))
                        except ValueError:
                            print("Value Error, Try Again.\n")
                        else:
                            if item_quantity > 0:
                                break
                            else:
                                print("Invalid Item Quantity, Try Again.")
                    if item_quantity <= int(csv_reader_list[line]["Inventory"]):
                        valid_quantity = item_quantity
                        new_quantity = str(int(csv_reader_list[line]["Inventory"]) - item_quantity)
                        csv_writer.writerow( {"No.": csv_reader_list[line]["No."], "Item": csv_reader_list[line]["Item"], "Price": csv_reader_list[line]["Price"], "Inventory": new_quantity} )
                    elif item_quantity > int(csv_reader_list[line]["Inventory"]):
                        csv_writer.writerow( {"No.": csv_reader_list[line]["No."], "Item": csv_reader_list[line]["Item"], "Price": csv_reader_list[line]["Price"], "Inventory": csv_reader_list[line]["Inventory"]} )
                        print("Sorry, the \"{}\" item remaining quantity is: {}.\n".format(csv_reader_list[line]["Item"], csv_reader_list[line]["Inventory"]))
                else:
                    csv_writer.writerow( {"No.": csv_reader_list[line]["No."], "Item": csv_reader_list[line]["Item"], "Price": csv_reader_list[line]["Price"], "Inventory": csv_reader_list[line]["Inventory"]} )

    elif file_to_open == 2:
        with open(path.join(absolute_path, "menu_steaks.csv"), "r", newline="") as rf:
            csv_reader = csv.DictReader(rf, delimiter=",")
            csv_reader_list = list(csv_reader)

        with open(path.join(absolute_path, "menu_steaks.csv"), "w", newline="") as wf:
            headers = ["No.", "Item", "Price", "Inventory"]
            csv_writer = csv.DictWriter(wf, fieldnames=headers, delimiter=",")
            csv_writer.writeheader()
            for line in range(len(csv_reader_list)):
                if csv_reader_list[line]["No."] == item_selected:
                    while True:
                        try:
                            item_quantity = int(input("Quantity of the \"{}\" item: ".format(csv_reader_list[line]["Item"])))
                        except ValueError:
                            print("Value Error, Try Again.\n")
                        else:
                            if item_quantity > 0:
                                break
                            else:
                                print("Invalid Item Quantity, Try Again.")
                    if item_quantity <= int(csv_reader_list[line]["Inventory"]):
                        valid_quantity = item_quantity
                        new_quantity = str(int(csv_reader_list[line]["Inventory"]) - item_quantity)
                        csv_writer.writerow( {"No.": csv_reader_list[line]["No."], "Item": csv_reader_list[line]["Item"], "Price": csv_reader_list[line]["Price"], "Inventory": new_quantity} )
                    elif item_quantity > int(csv_reader_list[line]["Inventory"]):
                        csv_writer.writerow( {"No.": csv_reader_list[line]["No."], "Item": csv_reader_list[line]["Item"], "Price": csv_reader_list[line]["Price"], "Inventory": csv_reader_list[line]["Inventory"]} )
                        print("Sorry, the \"{}\" item remaining quantity is: {}.\n".format(csv_reader_list[line]["Item"], csv_reader_list[line]["Inventory"]))
                else:
                    csv_writer.writerow( {"No.": csv_reader_list[line]["No."], "Item": csv_reader_list[line]["Item"], "Price": csv_reader_list[line]["Price"], "Inventory": csv_reader_list[line]["Inventory"]} )
    
    elif file_to_open == 3:
        with open(path.join(absolute_path, "menu_burgers.csv"), "r", newline="") as rf:
            csv_reader = csv.DictReader(rf, delimiter=",") 
            csv_reader_list = list(csv_reader)

        with open(path.join(absolute_path, "menu_burgers.csv"), "w", newline="") as wf:
            headers = ["No.", "Item", "Price", "Inventory"]
            csv_writer = csv.DictWriter(wf, fieldnames=headers ,delimiter=",")
            csv_writer.writeheader()
            for line in range(len(csv_reader_list)):
                if csv_reader_list[line]["No."] == item_selected:
                    while True:
                        try:
                            item_quantity = int(input("Quantity of the \"{}\" item: ".format(csv_reader_list[line]["Item"])))
                        except ValueError:
                            print("Value Error, Try Again.\n")
                        else:
                            if item_quantity > 0:
                                break
                            else:
                                print("Invalid Item Quantity, Try Again.")
                    if item_quantity <= int(csv_reader_list[line]["Inventory"]):
                        valid_quantity = item_quantity
                        new_quantity = str(int(csv_reader_list[line]["Inventory"]) - item_quantity)
                        csv_writer.writerow( {"No.": csv_reader_list[line]["No."], "Item": csv_reader_list[line]["Item"], "Price": csv_reader_list[line]["Price"], "Inventory": new_quantity} )
                    elif item_quantity > int(csv_reader_list[line]["Inventory"]):
                        csv_writer.writerow( {"No.": csv_reader_list[line]["No."], "Item": csv_reader_list[line]["Item"], "Price": csv_reader_list[line]["Price"], "Inventory": csv_reader_list[line]["Inventory"]} )
                        print("Sorry, the \"{}\" item remaining quantity is: {}.\n".format(csv_reader_list[line]["Item"], csv_reader_list[line]["Inventory"]))
                else:
                    csv_writer.writerow( {"No.": csv_reader_list[line]["No."], "Item": csv_reader_list[line]["Item"], "Price": csv_reader_list[line]["Price"], "Inventory": csv_reader_list[line]["Inventory"]} )
    
    elif file_to_open == 4:
        with open(path.join(absolute_path, "menu_pizza.csv"), "r",  newline="") as rf:
            csv_reader = csv.DictReader(rf, delimiter=",")
            csv_reader_list = list(csv_reader)

        with open(path.join(absolute_path, "menu_pizza.csv"), "w", newline="") as wf:
            headers = ["No.", "Item", "Small Size Price", "Medium Size Price", "Large Size Price", "Inventory"]
            csv_writer = csv.DictWriter(wf, fieldnames=headers, delimiter=",")
            csv_writer.writeheader()
            for line in range(len(csv_reader_list)):
                if csv_reader_list[line]["No."] ==  item_selected:
                    while True:
                        try:
                            item_quantity = int(input("Quantity of the \"{}\" item: ".format(csv_reader_list[line]["Item"])))
                        except ValueError:
                            print("Value Error, Try Again.")
                        else:
                            if item_quantity > 0:
                                break
                            else:
                                print("Invalid Item Quantity, Try Again.")
                    if item_quantity <= int(csv_reader_list[line]["Inventory"]):
                        valid_quantity = item_quantity
                        new_quantity = str(int(csv_reader_list[line]["Inventory"]) - item_quantity)
                        csv_writer.writerow( {"No.": csv_reader_list[line]["No."], "Item": csv_reader_list[line]["Item"], "Small Size Price": csv_reader_list[line]["Small Size Price"], "Medium Size Price": csv_reader_list[line]["Medium Size Price"], "Large Size Price": csv_reader_list[line]["Large Size Price"], "Inventory": new_quantity} )
                    elif item_quantity > int(csv_reader_list[line]["Inventory"]):
                        csv_writer.writerow( {"No.": csv_reader_list[line]["No."], "Item": csv_reader_list[line]["Item"], "Small Size Price": csv_reader_list[line]["Small Size Price"], "Medium Size Price": csv_reader_list[line]["Medium Size Price"], "Large Size Price": csv_reader_list[line]["Large Size Price"], "Inventory": csv_reader_list[line]["Inventory"]} )
                        print("Sorry, the \"{}\" item remaining quantity is: {}.\n".format(csv_reader_list[line]["Item"], csv_reader_list[line]["Inventory"]))
                else:
                    csv_writer.writerow( {"No.": csv_reader_list[line]["No."], "Item": csv_reader_list[line]["Item"], "Small Size Price": csv_reader_list[line]["Small Size Price"], "Medium Size Price": csv_reader_list[line]["Medium Size Price"], "Large Size Price": csv_reader_list[line]["Large Size Price"], "Inventory": csv_reader_list[line]["Inventory"]} )

    elif file_to_open == 5:
        with open(path.join(absolute_path, "menu_drinks.csv"), "r", newline="") as rf:
            csv_reader = csv.DictReader(rf, delimiter=",")
            csv_reader_list = list(csv_reader)
        
        with open(path.join(absolute_path, "menu_drinks.csv"), "w", newline="") as wf:
            headers = ["No.", "Item", "Price", "Inventory"]
            csv_writer = csv.DictWriter(wf, fieldnames=headers, delimiter=",")
            csv_writer.writeheader()
            for line in range(len(csv_reader_list)):
                if csv_reader_list[line]["No."] == item_selected:
                    while True:
                        try:
                            item_quantity = int(input("Quantity of the \"{}\" item: ".format(csv_reader_list[line]["Item"])))
                        except ValueError:
                            print("Value Error, Try Again.\n")
                        else:
                            if item_quantity > 0:
                                break
                            else:
                                print("Invalid Item Quantity, Try Again.")
                    if item_quantity <= int(csv_reader_list[line]["Inventory"]):
                        valid_quantity = item_quantity
                        new_quantity = str(int(csv_reader_list[line]["Inventory"]) - item_quantity)
                        csv_writer.writerow( {"No.": csv_reader_list[line]["No."], "Item": csv_reader_list[line]["Item"], "Price": csv_reader_list[line]["Price"], "Inventory": new_quantity} )
                    elif item_quantity > int(csv_reader_list[line]["Inventory"]):
                        csv_writer.writerow( {"No.": csv_reader_list[line]["No."], "Item": csv_reader_list[line]["Item"], "Price": csv_reader_list[line]["Price"], "Inventory": csv_reader_list[line]["Inventory"]} )
                        print("Sorry, the \"{}\" item remaining quantity is: {}.\n".format(csv_reader_list[line]["Item"], csv_reader_list[line]["Inventory"]))
                else:
                    csv_writer.writerow( {"No.": csv_reader_list[line]["No."], "Item": csv_reader_list[line]["Item"], "Price": csv_reader_list[line]["Price"], "Inventory": csv_reader_list[line]["Inventory"]} )


def menu():
    while True:
        print("Menu".center(15))
        print("1) Starters")
        print("2) Steaks")
        print("3) Burgers")
        print("4) Pizza")
        print("5) Drinks")

        while True:
            try:
                open_menu = int(input("\nInput the number of which menu you want to open: "))
            except ValueError:
                print("Value Error, Please Try Again.")
            else:
                if open_menu in range(1, 6):
                    break
                else:
                    print("You can only select between 1 to 5.")

        if open_menu == 1:
            menu_starters()
            control = user_order_ftn()
            if control == "1" or control == "2" or control == "3" or control == "4":
                inventory_call = inventory(open_menu, control)
                with open(path.join(absolute_path, "menu_starters.csv"), "r") as rf:
                    csv_reader = csv.DictReader(rf, delimiter=",")
                    for line in csv_reader:
                        if valid_quantity > 0:
                            if line["No."] == control:
                                user_orderlist.append({"Item": line["Item"], "Price": int(line["Price"]), "Quantity": valid_quantity, "File": 1})
                                print("The item has been added to your order list.\n")
            elif control == "M" or control == "m":
                continue
            else:
                print("Invalid Item Selection, Please Try Again.\n")
                continue

        elif open_menu == 2:
            menu_steaks()
            control = user_order_ftn()
            if control == "1" or control == "2" or control == "3" or control == "4":
                inventory_call = inventory(open_menu, control)
                with open(path.join(absolute_path, "menu_steaks.csv"), "r") as rf:
                    csv_reader = csv.DictReader(rf, delimiter=",")
                    for line in csv_reader:
                        if valid_quantity > 0:
                            if line["No."] == control:
                                user_orderlist.append({"Item": line["Item"], "Price": int(line["Price"]), "Quantity": valid_quantity, "File": 2})
                                print("The item has been added to your order list.\n")
            elif control == "M" or control == "m":
                continue
            else:
                print("Invalid Item Selection, Please Try Again.\n")

        elif open_menu == 3:
            menu_burgers()
            control = user_order_ftn()
            if control == "1" or control == "2" or control == "3" or control == "4":
                inventory_call = inventory(open_menu, control)
                with open(path.join(absolute_path, "menu_burgers.csv"), "r") as rf:
                    csv_reader = csv.DictReader(rf, delimiter=",")
                    for line in csv_reader:
                        if valid_quantity > 0:
                            if line["No."] == control:
                                user_orderlist.append({"Item": line["Item"], "Price": int(line["Price"]), "Quantity": valid_quantity, "File": 3})
                                print("The Item has been added to your order list.\n")
            elif control == "M" or control == "m":
                continue
            else:
                print("Invalid Item Selection, Please Try Again.\n")

        elif open_menu == 4:
            menu_pizza()
            control = user_order_ftn()
            if control == "1" or control == "2" or control == "3":
                while True:
                    size = input("Select the size of pizza? (S/M/L): ")
                    if size == "S" or size == "M" or size =="L":
                        break
                    else:
                        print("Invalid Size, Try Again.")
                inventory_call = inventory(open_menu, control)
                with open(path.join(absolute_path, "menu_pizza.csv"), "r", newline="") as rf:
                    csv_reader = csv.DictReader(rf, delimiter=",")
                    for line in csv_reader:
                        if valid_quantity > 0:
                            if line["No."] == control and size == "S":
                                user_orderlist.append( {"Item": line["Item"], "Price": int(line["Small Size Price"]), "Quantity": valid_quantity, "File": 4} )
                                print("The Item has been added to your order list.\n")
                            elif line["No."] == control and size == "M":
                                user_orderlist.append( {"Item": line["Item"], "Price": int(line["Medium Size Price"]), "Quantity": valid_quantity, "File": 4} )
                                print("The Item has been added to your order list.\n")
                            elif line["No."] == control and size == "L":
                                user_orderlist.append( {"Item": line["Item"], "Price": int(line["Large Size Price"]), "Quantity": valid_quantity, "File": 4} )
                                print("The Item has been added to your order list.\n")
            elif control == "M" or control == "m":
                continue
            else:
                print("Invalid Item Selection, Please Try Again.\n")

        elif open_menu == 5:
            menu_drinks()
            control = user_order_ftn()
            if control == "1" or control == "2" or control == "3" or control == "4" or control == "5" or control == "6": 
                inventory_call = inventory(open_menu, control) 
                with open(path.join(absolute_path,  "menu_drinks.csv"), "r") as rf:
                    csv_reader = csv.DictReader(rf, delimiter=",")
                    for line in csv_reader:
                        if valid_quantity > 0:
                            if line["No."] == control:
                                user_orderlist.append( {"Item": line["Item"], "Price": int(line["Price"]), "Quantity": valid_quantity, "File": 5} )
                                print("The Item has been added to your order list.\n")
            elif control == "M" or control == "m":
                continue
            else:
                print("Invalid Item Selection, Please Try Again.\n")

        while True:
            check = input("Do u want to add an item (1), OR exit the menu (2): ")
            if check == "1" or check == "2":
                break
            else:
                print("Wrong Input, Please Try Again.\n")
        if check == "1":
            continue
        elif check == "2":
            break

    for each_dict in range(len(user_orderlist)):
        user_orderlist[each_dict]["No."] = str(each_dict + 1)


def add_to_inventory(item):
    if item["File"] == 1:
        with open(path.join(absolute_path, "menu_starters.csv"), "r", newline="") as rf:
            csv_reader = csv.DictReader(rf, delimiter=",")
            file_list = list(csv_reader)
        with open(path.join(absolute_path, "menu_starters.csv"), "w", newline="") as wf:
            headers = ['No.', 'Item', 'Price', 'Inventory']
            writeFile = csv.DictWriter(wf, fieldnames=headers, delimiter=",")
            writeFile.writeheader()
            for line in file_list:
                if line["Item"] == item["Item"]:
                    new_value = str(item["Quantity"] + int(line["Inventory"]))
                    writeFile.writerow( {"No.": line["No."], "Item": line["Item"], "Price": line["Price"], "Inventory": new_value} )
                else:
                    writeFile.writerow( {"No.": line["No."], "Item": line["Item"], "Price": line["Price"], "Inventory": line["Inventory"]} )

    elif item["File"] == 2:
        with open(path.join(absolute_path, "menu_steaks.csv"), "r", newline="") as rf:
            csv_reader = csv.DictReader(rf, delimiter=",")
            file_list = list(csv_reader)
        with open(path.join(absolute_path, "menu_steaks.csv"), "w", newline="") as wf:
            headers = ['No.', 'Item', 'Price', 'Inventory']
            writeFile = csv.DictWriter(wf, fieldnames=headers, delimiter=",")
            writeFile.writeheader()
            for line in file_list:
                if line["Item"] == item["Item"]:
                    new_value =  str(item["Quantity"] + int(line["Inventory"]))
                    writeFile.writerow( {"No.": line["No."], "Item": line["Item"], "Price": line["Price"], "Inventory": new_value} )
                else:
                    writeFile.writerow( {"No.": line["No."], "Item": line["Item"], "Price": line["Price"], "Inventory": line["Inventory"]} )

    elif item["File"] == 3:
        with open(path.join(absolute_path, "menu_burgers.csv"), "r", newline="") as rf:
            csv_reader = csv.DictReader(rf, delimiter=",")
            file_list = list(csv_reader)
        with open(path.join(absolute_path, "menu_burgers.csv"), "w", newline="") as wf:
            headers = ['No.', 'Item', 'Price', 'Inventory']
            writeFile = csv.DictWriter(wf, fieldnames=headers, delimiter=",")
            writeFile.writeheader()
            for line in file_list:
                if line["Item"] == item["Item"]:
                    new_value = str(item["Quantity"] + int(line["Inventory"]))
                    writeFile.writerow( {"No.": line["No."], "Item": line["Item"], "Price": line["Price"], "Inventory": new_value} )
                else:
                    writeFile.writerow( {"No.": line["No."], "Item": line["Item"], "Price": line["Price"], "Inventory": line["Inventory"]} )

    elif item["File"] == 4:
        with open(path.join(absolute_path, "menu_pizza.csv"), "r", newline="") as rf:
            csv_reader = csv.DictReader(rf, delimiter=",")
            file_list = list(csv_reader)
        with open(path.join(absolute_path, "menu_pizza.csv"), "w", newline="") as wf:
            headers = ["No.", "Item", "Small Size Price", "Medium Size Price", "Large Size Price", "Inventory"]
            writeFile = csv.DictWriter(wf, fieldnames=headers, delimiter=",")
            writeFile.writeheader()
            for line in file_list:
                if line["Item"] == item["Item"]:
                    new_value = str(item["Quantity"] + int(line["Inventory"]))
                    writeFile.writerow( {"No.": line["No."], "Item": line["Item"], "Small Size Price": line["Small Size Price"], "Medium Size Price": line["Medium Size Price"], "Large Size Price": line["Large Size Price"], "Inventory": new_value} )
                else:
                    writeFile.writerow( {"No.": line["No."], "Item": line["Item"], "Small Size Price": line["Small Size Price"], "Medium Size Price": line["Medium Size Price"], "Large Size Price": line["Large Size Price"], "Inventory": line["Inventory"]} )

    elif item["File"] == 5:
        with open(path.join(absolute_path, "menu_drinks.csv"), "r", newline="") as rf:
            csv_reader = csv.DictReader(rf, delimiter=",")
            file_list = list(csv_reader)
        with open(path.join(absolute_path, "menu_drinks.csv"), "w", newline="") as wf:
            headers = ['No.', 'Item', 'Price', 'Inventory']
            writeFile = csv.DictWriter(wf, fieldnames=headers, delimiter=",")
            writeFile.writeheader()
            for line in file_list:
                if line["Item"] == item["Item"]:
                    new_value = str(item["Quantity"] + int(line["Inventory"]))
                    writeFile.writerow( {"No.": line["No."], "Item": line["Item"], "Price": line["Price"], "Inventory": new_value} )
                else:
                    writeFile.writerow( {"No.": line["No."], "Item": line["Item"], "Price": line["Price"], "Inventory": line["Inventory"]} )


def view_order():
    total_bill = 0

    for line in user_orderlist:
        total_bill += line["Price"] * line["Quantity"]

    print("\n", "\"Order List\"".center(40))
    print("No.".ljust(5) ,"Item".ljust(30), "Price".ljust(5), "Quantity".ljust(5))
    for line in user_orderlist:
        print(str(line["No."]).ljust(5) , line["Item"].ljust(30), str(line["Price"]).ljust(5), str(line["Quantity"]).center(5))
    print("Total Bill:", str(total_bill) + " Rs")

    return total_bill


def remove_item():
    while True:
        if len(user_orderlist) > 0:
            view_order()
            try:
                item = input("If u want to remove any item just write its number \"OR\" to add item(Add/add) \"OR\" to confirm order(Exit/exit): ")
                if item == "":
                    raise ValueError
            except ValueError:
                print("Wrong input, you cannot enter an empty string.\n")
            else:
                item = item.strip()
                for line in user_orderlist:
                    if item == line["No."]:
                        index = user_orderlist.index(line)
                        popped_item = user_orderlist.pop(index)
                        add_to_inventory(popped_item)
                        print("The \"{}\" item has been removed from your order list.\n".format(popped_item["Item"]))
                        for each_dict in range(len(user_orderlist)):
                            user_orderlist[each_dict]["No."] = str(each_dict+1)
                        break
                else:
                    if item == "Exit" or item == "exit":
                        break
                    elif item == "Add" or item == "add":
                        menu()
                        continue
                    else:
                        print("Such item number was not found in your order list.\n")
        else:
            print("The order list is empty.")
            break


def LogIn():
    while True:
        print("\n", " \"Log In\" ".center(20))
        gmail = input("Gmail: ")
        password = input("Password: ")
        username = ""

        with open(path.join(absolute_path, "users.csv"), "r") as rf:
            reader = csv.DictReader(rf, delimiter=",")
            for line in reader:
                if (line["Gmail"] == gmail) and (line["Password"] == password):
                    username = line["Username"]
                    print("\nDear {}, Login Successful!\n".format(username))
                    return username
            else:
                print("Login Failed, Incorrect gmail or password.")
                while True:
                    try:
                        choice = input("Do u want to Sign Up (Yes/No): ")
                        if choice == "":
                            raise IndexError
                    except IndexError:
                        print("Wrong Input.\n")
                        continue
                    else:
                        if (choice == "Yes") or (choice == "yes"):
                            SignUp()
                            break
                        elif (choice == "No") or (choice == "no"):
                            break
                        else:
                            print("Wrong Input.\n")


def SignUp():
    print("\n", " \"Sign Up\" ".center(25))
    
    while True:
        try:
            username = input("Input Username: ")
            if username == "":
                raise IndexError
        except IndexError:
            print("Invalid Input, Try Again.\n")
        else:
            if username[0] == " ":
                print("Username cannot have a space as its first character, Try Again.")
            else:
                username = username.strip()
                with open("users.csv", "r") as rf:
                    csv_reader = csv.DictReader(rf, delimiter=",")
                    for line in csv_reader:
                        if line["Username"] == username:
                            print("\nThe username {}, is already taken.\n".format(username))
                            break
                        continue
                    else:
                        break

    while True:
        password = input("Input Password: ")
        if len(password) < 8:
            print("The lenght of the password should be atleast 8.\n")
            continue
        elif len(password) > 20:
            print("The lenght of the password cannot exceed 20.\n")
            continue
        for char in password:
            if char == " ":
                print("You cannot put spaces in your password.\n")
                break
            continue
        else:
            break

    while True:
        try:
            gmail = input("Input the preceding text of @gmail.com : ")
            if gmail == "":
                raise IndexError
        except IndexError:
            print("Wrong Input, You cannot input an empty string.\n")
            continue
        else:
            for char in gmail:
                if char == " ":
                    print("You cannot input spaces in your gmail.\n")
                    break
                elif char == "@":
                    print("You cannot use \"@\" this symbol.\n")
                    break
                continue
            else:                
                new_gmail = gmail + "@gmail.com"
                with open(path.join(absolute_path, "users.csv"), "r") as rf:
                    csv_reader = csv.DictReader(rf, delimiter=",")
                    for line in csv_reader:
                        if line["Gmail"] == new_gmail:
                            print("Sorry, this gmail is already taken please try again.\n")
                            break
                        continue
                    else:
                        break


    with open(path.join(absolute_path, "users.csv"), "a", newline="") as af:
        headers = ["Username", "Password", "Gmail"]
        appender = csv.DictWriter(af, fieldnames=headers, delimiter=",")
        appender.writerow(
            {"Username": username, "Password": password, "Gmail": new_gmail})
        print("Your account has been succesfuly created.\n")


menu_check = False


def main():
    global menu_check
    menu_check = False
    while True:
        print("\"Food On Fire Restaurant App\"".center(50))
        user_state = input("\nDo u want to Login or create a new account? Log In(L/l) or Sign Up(S/s) : ")
        user_state = user_state.strip()
        if user_state == "L" or user_state == "l":
            login_ftn = LogIn()
            break
        elif user_state == "S" or user_state == "s":
            signup_ftn = SignUp()
            continue
        else:
            print("Invalid Input, Try Again.\n")

    while True:
        print(F"Dear {login_ftn}, What type of order do u want to do?")
        order_type = input("Table Reservation OR Home Delivery (Table/Home): ")
        order_type = order_type.strip()
        if order_type == "Table" or order_type == "table":
            table_ftn = table_reservation()
            if table_ftn > 0:
                menu_check = True
                menu()
                break
            else:
                print("Sorry all the tables are reserved, You should try again after some time.")
                break
        elif order_type == "Home" or order_type == "home":
            menu_check = True
            menu()
            break
        else:
            print("Wrong Input, Please Try Again.\n")
            continue


main()


if menu_check:
    remove_item()


if len(user_orderlist) > 0:
    total = view_order()
    print("\"Your order has been placed.\"")