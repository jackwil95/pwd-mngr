def websites():
    newEntry = ''
    while newEntry != 'quit':
        entryList = []
        newEntry = input("What website would you like to store? Else, quit: ")
        entryList.append(newEntry)
    return entryList


print(websites())

# newEntry = ''
# while new
