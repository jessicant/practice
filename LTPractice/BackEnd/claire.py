class TodoList:

    class __TodoItem:
        """Modelling a single item in a to-do list."""
        description: str
        priority: int
        month: int
        day: int
        year: int

        def __init__(self, description: str, priority: int, month: int, day: int, year: int):
            """Initializes details on the item in the to-do list."""
            self.description = description
            self.priority = priority
            self.month = month
            self.day = day
            self.year = year

        def __lt__(self, other):
            """Used to define priority for TodoItems. First sort by date, then priority, then description.
            TodoItems with more priority are considered less than TodoItems with less priority."""
            if self.year == other.year:
                if self.month == other.month:
                    if self.day == other.day:
                        if self.priority == other.priority:
                            return self.description < other.description
                        return self.priority > other.priority
                    return self.day < other.day
                return self.month < other.month
            return self.year < other.year

        def __gt__(self, other):
            return __lt__(other, self)

        def __eq__(self, other):
            return self.year == other.year & self.month == other.month & self.day == other.day \
                   & self.priority == other.priority & self.description == other.description

        def __str__(self):
            """Makes printing TodoItem easier."""
            return self.description + ": due " + str(self.month) + "/" + str(self.day) + "/" + str(self.year) \
                   + ", " + self.__priority()

        def __priority(self):
            """Convert from priority number to priority string"""
            return "low priority" if self.priority == 1 else "medium priority" if self.priority == 2 \
                                                        else "high priority" if self.priority == 3 else "priority n/a"

    __tdList: list
    def __init__(self):
        """Initializes an empty TodoList object."""
        self.__tdList = []

    def add(self, description: str, priority: int, month: int, day: int, year: int):
        """Adds a TodoItem to do TodoList"""
        self.__tdList.append(self.__TodoItem(description, priority, month, day, year))
        self.__tdList.sort()

    def remove(self, index: int):
        """Removes item at a specific index"""
        self.__tdList.pop(index)

    def length(self):
        return len(self.__tdList)

    def __str__(self):
        """Makes it easier to print out TodoList"""

        result = ""
        for i in range(len(self.__tdList)):
            result += str(i + 1) + " - " + self.__tdList[i].__str__() + "\n"

        return result.strip()

todo = TodoList()

userInput = ""
while userInput != "3":

    print(todo, "\n")
    userInput = input("What would you like to do with the Todo List? (1 - add, 2 - remove, 3 - exit) ")

    if userInput == "1":
        desc = input("Please give a brief description of the task you would like to add: ")

        month = input("Please give the month it is due: ")
        while not (month.isdigit() and int(month) >= 1 and int(month) <= 12):
            month = input("Invalid input. Please give a number between 1 and 12: ")
        month = int(month)

        day = input("Please give the day it is due: ")
        while not (day.isdigit() and int(day) >= 1 and int(day) <= 31):
            day = input("Invalid input. Please give a number between 1 and 31: ")
        day = int(day)

        year = input("Please give the year it is due: ")
        while not (year.isdigit() and int(year) >= 2021):
            year = input("Invalid input. Please give a number that is 2021 or greater: ")
        year = int(year)

        prior = input("Please give a number representing priority. 1 - low "
                      "priority, 2 - medium priority, 3 - high priority, 0 - n/a: ");
        while not (prior.isdigit() and int(prior) >= 0 and int(prior) <= 3):
            prior = input("Invalid input. Please give an integer between 0 and 3: ")
        prior = int(prior)

        print()
        todo.add(desc, prior, month, day, year)

    elif userInput == "2":
        if todo.length() != 0:
            index = input("Please give the index of the task you would like to remove: ")
            while not (index.isdigit() and int(index) >= 1 and int(index) <= todo.length()):
                index = input("Invalid input: Please enter a valid index: ")

            index = int(index) - 1
            todo.remove(index)
        else:
            print("There is nothing to remove.")

    elif userInput == "3":
        break
    else:
        print("Invalid input. Please try again.")