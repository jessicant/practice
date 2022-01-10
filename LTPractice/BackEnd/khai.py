# This class represents the command-line user interface that
#     manages the to-do list
class to_do_list_client:
    user_to_do_list = None
    username = None # kept as a field just in case we need to manage multiple lists
                    #     and need a good way to identify them
    
    # post: Initializes the client
    def __init__(self):
        self.user_to_do_list = to_do_list()
    
    # post: Prints the contents of the to-do list
    def print_list_contents(self):
        task_list = self.user_to_do_list.get_task_list()
        if task_list:
            print("Your current to-do list:")
            for task in task_list:
                print("\t" + task)
        else:
            print("There are currently no tasks in your to-do list.")
        
    # post: Prints instructions for using this program
    def print_instructions(self):
        print("Type 'add' to add a task to your to-do list,")
        print("Type 'remove' to remove a task from your to-do list.")
        print("Type 'clear' to clear all items from your to-do list.")
        print("Type 'exit' to quit the program.")
    
    # post: Runs the to-do list program
    #       Exits the program when user inputs 'exit'
    def run(self):
        print()
        print("Hello! Welcome to kList!");
        print("Before we begin, what is your name?")
        username = input()
        keep_running = True
        while(keep_running):
            print()
            print("You are currently signed in as " + username + ".")
            self.print_list_contents()
            print()
            self.print_instructions()
            user_choice = input()
            print()
            if user_choice == "add":
                print("What task would you like to add?")
                task = input()
                self.user_to_do_list.add_task(task)
            elif user_choice  == "remove":
                print("What task would you like to remove?")
                task = input()
                print()
                if self.user_to_do_list.remove_task(task):
                    print("Task successfully removed.");
                else:
                    print("Sorry, that task is not in your to-do list.")
            elif user_choice == "clear":
                self.user_to_do_list.clear_all_tasks()
                print("All tasks have been cleared.")
            elif user_choice == "exit":
                keep_running = False
                print("Thank you for using kList!")
        

# This class represents a to-do list
class to_do_list:
    task_list = None;
    
    # post: Initializes the to-do list
    def __init__(self):
        self.task_list = []
    
    # pre:  Must input a String task
    # post: If to-do list is not None, adds the task to the list
    def add_task(self, task):
        if self.task_list != None:
            self.task_list.append(task)
        
    # pre:  Must input a String task
    # post: If to-do list is not None and the task is in the list,
    #           adds task to the list and returns True
    #       Else, returns False
    def remove_task(self, task):
        if self.task_list != None and task in self.task_list:
            self.task_list.remove(task)
            return True
        else:
            return False
            
    # post: Removes all tasks from the to-do list
    def clear_all_tasks(self):
        self.task_list.clear()
    
    # post: Returns the to-do list
    def get_task_list(self):
        return self.task_list
        
khai_list = to_do_list_client()
khai_list.run()
    
