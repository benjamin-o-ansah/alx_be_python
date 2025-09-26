def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            itemName = input("Enter the item to add: ")
            shopping_list.append(itemName)
            print(f"{itemName} has been added to the list.")
            print("Thank you for using the Shopping List Manager!")
        elif choice == '2':
            itemName = input("Enter the item to remove: ")
            if itemName in shopping_list:
                shopping_list.remove(itemName)
                print(f"{itemName} has been removed from the list.")
            else:
                print(f"{itemName} is not in the list.")
            print("Thank you for using the Shopping List Manager!")
            
        elif choice == '3':
            print("Shopping List: \n",shopping_list)
            print("Thank you for using the Shopping List Manager!")
            
        elif choice == '4':
            print("Thank you for using the Shopping List Manager!")
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()