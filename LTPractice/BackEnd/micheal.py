class Todolist:
    # Initialization
    def __init__(self):
        self.currentList = []

    # Add item to list
    def add(self, item):
        # Check if item already exists in the list
        if self.currentList.count(item) > 0:
            raise Exception()
        else:
            self.currentList.append(item)

    # Remove item from list
    def remove(self, item):
        # Check if user is trying to remove from empty list
        if len(self.currentList) == 0:
            raise Exception()
        else:
            self.currentList.remove(item)

    # Print current contents of the list
    def print_list(self):
        if len(self.currentList) == 0:
            print("No items in the to-do list.")
        else:
            print("Current to-do list")
            for x in self.currentList:
                print(x)

    # Manage behavior for to do list
    def manage(self):
        n = 1
        while n == 1:
            val = input("To-do list options: add, remove, exit or print. ")

            if val.lower() == "exit":
                break;
            elif val.lower() == "add":
                additem = input("Enter what you would like to add to the to-do list. ")
                try:
                    self.add(additem)
                except:
                    print("That item is already in the list. Please add a different item.")
            elif val.lower() == "remove":
                removeitem = input("Enter what you would like to remove from the to-do list. ")
                try:
                    self.remove(removeitem)
                except:
                    print("Please add at least one item before removing.")
            elif val.lower() == "print":
                self.print_list();
            else:
                print("Please enter a valid option.")


list1 = Todolist()
list1.manage()

