'''
This file makes a terminal checklist.
You can add, remove, update, and read entries from the list.
An empty checkbox is prepended to every new entry.
You can then check or uncheck the entry's checkbox.
'''

# Create our Checklist
checklist = []

# Define Functions
def create(item):
    # Create item code here
    checklist.append(item)

    return f"{item} was added to checklist: {checklist}"

def read(index):
    # Read code here
    return print (f"{checklist[index]} is at {index} position")

def update(index, item):
    # Update code here
    old_item = checklist[index]
    checklist[index] = item 

def destroy(index):
    # Destroy code here
    old_item = checklist[index]
    checklist.pop(index)
    
    return print(f"{old_item} was deleted from checklist")

def mark_completed(index):
    # Add code here that marks an item as completed
    if "*" not in checklist[index]:
        checklist[index] = f'[*] {checklist[index]}'

    return print(f"{checklist[index]} was marked completed")
    

def list_all_items():
    # List all items code here
    for item in checklist:
        if "*" not in item:
            print(item)

    return print(f'{checklist} only non-starred items returned')


def select(function_code):
    # User Selection Code here

    # Create item example
    if function_code == "C":
        input_item = input ("Input item:")
        create(input_item)
        running = True

        return running
    
    elif  function_code == "R":
        input_item = input("Enter item to add")
        read(int(input_item))
        running = True
    
    elif function_code =="U":
        input_index = input("Chose index position in list to revise ")
        input_item = input("Chose element in list to revise")
        update(int(input_index), input_item)
        running = True
        return running
    
    elif function_code == "D":
        input_index = input("Chose index position of element to delete: ")
        destroy(int(input_index))
    
    elif function_code == "M":
        input_index = input("Enter the index position of the element you want to mark completed: ")
        mark_completed(int(input_index))
        running = True

        return running

    elif function_code == "L":
        list_all_items()
        running = True

        return running

    else:
        print("Please enter a valid checklist command!")
        
        running = True

        return running

running = True



while running: 
    selection = input(
        "Press C to add to list, R to read from list, U to update list, D to delete an element from list, M to mark element completed, L to display items on list, and Q to quit:").upper()
    running = select(selection)