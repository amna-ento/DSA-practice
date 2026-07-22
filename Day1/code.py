import os

if not os.path.exists("warehouse_management_system.txt"):

    file = open("warehouse_management_system.txt", "w")

    file.write("101,Laptop\n")
    file.write("205,Mouse\n")
    file.write("150,Keyboard\n")
    file.write("310,Monitor\n")
    file.write("120,USB Drive\n")
    file.write("275,Printer\n")
    file.write("180,Webcam\n")
    file.write("140,Headphones\n")
    file.write("220,Speaker\n")
    file.write("160,Microphone\n")

    file.close()

    print("File created successfully.\n")


products = []


file = open("warehouse_management_system.txt", "r")

for line in file:
    item_id, item_name = line.strip().split(",")
    products.append([int(item_id), item_name])

file.close()


def search_item():

    target = int(input("Enter Product ID to search: "))

    found = False

    for product in products:

        if product[0] == target:
            print("\nProduct Found")
            print("ID :", product[0])
            print("Name :", product[1])
            found = True
            break

    if not found:
        print("\nProduct not found.")


def add_item():

    while True:

        item_id = int(input("Enter Product ID: "))

        duplicate = False

        for product in products:
            if product[0] == item_id:
                duplicate = True
                print("Product ID already exists. Please enter a different ID.")
                break

        if not duplicate:
            break

    item_name = input("Enter Product Name: ")

    products.append([item_id, item_name])

    
    file = open("warehouse_management_system.txt", "a")
    file.write(f"{item_id},{item_name}\n")
    file.close()

    print("\nProduct Added Successfully.")


def delete_item():

    target = int(input("Enter Product ID to delete: "))

    found = False

    for product in products:

        if product[0] == target:
            products.remove(product)
            found = True
            break

    if found:

       
        file = open("warehouse_management_system.txt", "w")

        for product in products:
            file.write(f"{product[0]},{product[1]}\n")

        file.close()

        print("\nProduct Deleted Successfully.")

    else:
        print("\nProduct ID not found.")


def merge_sort(array):

    if len(array) > 1:

        mid = len(array) // 2

        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):

            if left[i][0] < right[j][0]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


def generate_report():

    merge_sort(products)

    print("\n===== Warehouse Report =====")

    for product in products:
        print("ID:", product[0], " Product:", product[1])

    # Save sorted data back to file
    file = open("warehouse_management_system.txt", "w")

    for product in products:
        file.write(f"{product[0]},{product[1]}\n")

    file.close()


while True:

    print("\n========== Warehouse Management =========")
    print("1. Search Product")
    print("2. Add Product")
    print("3. Delete Product")
    print("4. Generate Warehouse Report")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        search_item()

    elif choice == 2:
        add_item()

    elif choice == 3:
        delete_item()

    elif choice == 4:
        generate_report()

    elif choice == 5:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice.")
