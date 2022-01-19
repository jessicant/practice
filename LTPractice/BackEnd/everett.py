listDict = {}

def main():
  intro()
  checkCont = True
  while(checkCont):
    inputKey = checkToDo()
    if (inputKey == "a"):
      appendItem()
    elif (inputKey == "r"):
      removeItem()
    else:
      checkCont = exitList()

def intro():
  print("Welcome to your very own checklist! Here, you will get to list out all of the things" +
   "that you have to accomplish today! Let's get started!")

def checkToDo():
  print("What would you like to do today? Add a task, remove a task, or exit list creator?")
  checkInput = True
  inputKey = ""
  while(checkInput):
    inputKey = input("Input 'a' to add a task, 'r' to remove a task, and 'e' to exit from list creator")
    inputKey = inputKey.lower()
    if(inputKey=="a" or inputKey == "r" or inputKey == "e"):
      checkInput = False
      print("proper input detected")
    else:
      print("Try again. Input 'a' to add a task, 'r' to remove a task, and 'e' to exit from list creator")
  return inputKey

def appendItem():
  item = input("What task would you like to append to your list?")
  keys = listDict.keys()
  keyForItem = 0
  lookingForKey = True
  while(lookingForKey):
    if str(keyForItem) in keys:
      keyForItem+=1
    else:
      lookingForKey = False
  listDict[str(keyForItem)] = item
  print("Here is your current list")
  print(listDict.items())

def removeItem():
  print("Current List: ")
  print(listDict.items())
  item = input("What task number would you like to remove from your list?")
  while(item not in listDict.keys()):
    item = input("Faulty Input. What task number would you like to remove from your list?")
  listDict.pop(item)
  print("Item removed")

def exitList():
  inputKey = input("Would you like to exit this program? y for yes. anything else for no")
  inputKey = inputKey.lower()
  if (inputKey == "y"):
    print("Program terminated")
    return False

if __name__ == "__main__":
  main()
