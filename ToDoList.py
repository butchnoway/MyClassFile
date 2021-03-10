# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What): 
# RRoot,1.1.2030,Created started script
# BDavis, 3/9/2021, Modified Script
# ------------------------------------------------------------------------ #

#Display Greeting and o/v of what program does 
print("\t\t\t\t\tWELCOME TO YOUR TO-DO LIST!\n")
print("+"*80)
print("+"*80)
print("+"*80)
print("\n")

# -- Data -- #
# declare variables and constants
objFile = None   # An object that represents a file
strFile = "ToDoList.txt"
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = "" # A Capture the user option selection
strMenu = """
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
"""  # A menu of user options


# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
objFile = open(strFile, "w")

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print(strMenu)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        for row in lstTable:
            print(row)
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        strID = input("Enter an ID: ") 
        strName = input("Enter a Name: ")
        strEmail = input("Enter an Email: \n")
        dicRow = {"id":strID, "name":strName, "email":strEmail}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove an item from the list/Table based on its name
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        print("Your inventory is currently: \n")
        print(lstTable)
        rowDelete = int(input("which row would you like deleted?: "))
        #would be an excellent chance for try/except
        try:
            if rowDelete > 0 :
                lstTable.remove(lstTable[rowDelete - 1])
            else:
                print("ID is not in results list" )        
        except: 
            print("An error occursed because", rowDelete, "is less than 0")
        print("Your invetory is now: ")
        print(lstTable)
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        objFile.write(str(lstTable) + "\n")
        print("File updated")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        objFile = open(strFile, "r")
        for row in objFile:
            lstRow = row.split(",")
            print(lstRow)
            print(lstRow[0] + '|' + lstRow[1] + '|' + lstRow[2].strip())
        print("Your results have been saved!")
        objFile.close()
        break  # and Exit the program
