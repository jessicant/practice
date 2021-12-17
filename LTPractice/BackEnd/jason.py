#global array
listItems = []

def main():
    #print out commands
    displayCommands()

    while True:
        #print out current list of TODOS
        printTodos()
        print("add, remove, or exit: ")

        #get and check input for parameters
        ipt = input()
        if ipt.lower() == "exit": break 
        if " " not in ipt:
            print("no parameters")
            print()
            continue
        
        #run the program
        command = ipt.split(" ", 1)[0].lower()
        parameters = ipt.split(" ", 1)[1]
        if command == "add":
            add(parameters)
        elif command == "remove":
            remove(parameters)
        else:
            print(command,"is not a valid command")
        print()


def displayCommands():
    print("Commands: ")
    print("add + TODO")
    print("remove + index")
    print("exit")
    print()

def printTodos():
    print("Current List of TODOs: ")
    if not listItems:
        print("Empty")
    else:
        for index, val in enumerate(listItems):
            print(index, val)

def add(parameter):
    listItems.append(parameter)

def remove(parameter):
    try:
        parameter = int(parameter)
        if parameter >= len(listItems): print("item does not exist")
        else: listItems.pop(parameter)
    except ValueError:
        print("parameter is not a number")
        

if __name__ == "__main__":
    main()


