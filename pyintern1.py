def display_list(todo_list):
    if not todo_list:
        print("Your To-Do List is empty!")
    else:
        print("Your To-Do List:")
        for index, item in enumerate(todo_list, start=1):
            print(f"{index}. {item}")

# Function to add an item to the To-Do List
def add_item(todo_list, item):
    todo_list.append(item)
    print(f"'{item}' added to your To-Do List.")

# Function to remove an item from the To-Do List
def remove_item(todo_list, index):
    if 1 <= index <= len(todo_list):
        removed_item = todo_list.pop(index - 1)
        print(f"'{removed_item}' removed from your To-Do List.")
    else:
        print("Invalid index.")

# Main function
def main():
    todo_list = []
    while True:
        print("\n1. Display To-Do List")
        print("2. Add Item to To-Do List")
        print("3. Remove Item from To-Do List")
        print("4. Exit")

        choice = input("\nEnter your choice (1/2/3/4): ")

        if choice == '1':
            display_list(todo_list)
        elif choice == '2':
            item = input("Enter the item to add: ")
            add_item(todo_list, item)
        elif choice == '3':
            index = int(input("Enter the index of the item to remove: "))
            remove_item(todo_list, index)
        elif choice == '4':
            print("Exiting program. Do it well in next time!")
            break
        else:
            print("Invalid input. Please enter a valid option.")

if __name__ == "__main__":
    main()
