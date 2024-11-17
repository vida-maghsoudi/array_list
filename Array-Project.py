import time

class ArrayList:
    def __init__(self):
        self.array = []

    def add_without_index(self, elements):
        for i in range(elements):
            value = int(input("Enter some value: "))
            while True:
                if value in self.array:
                    print("The value you entered exists Try again")
                else:
                    self.array.append(value)
                    print("Updated array: ", self.array)
                    break
                value = int(input("Enter some value: "))
        return self.array

    def add_with_index(self, elements):
        """ Add value to array with specified index. """
        while len(self.array) < elements:
            value = int(input("Enter some value: "))
            while True:
                if value in self.array:
                    print("The value you entered exists And it will be removed.")
                    print(f"The index of removed value: ", self.array.index(value))
                    self.array.remove(value)
                    print("Updated array: ", self.array)
                else:
                    index = int(input("Enter index: "))
                    if 0 <= index < elements:
                        self.array.insert(index, value)
                        print("Updated array: ", self.array)
                        break
                    else:
                        print("Index out of range!")
                value = int(input("Enter some value: "))
        return self.array

    def remove_element(self, index):
        """ Remove element from array with specified index. """
        print("Element you removed: ", self.array[index])
        self.array.pop(index)
        return self.array

    def search_element(self, index):
        """ Search element with specified index. """
        print("Searching ...")
        time.sleep(2)
        return self.array[index]

    def search_index(self, element):
        """ You enter an element and if it exists in the array, the index of that element will be displayed. """
        print("Searching ...")
        time.sleep(2)
        return self.array.index(element)

    def reverse_array(self):
        self.array.reverse()
        print("Reversing ...")
        time.sleep(2)
        return self.array
# END CLASS
print("*** Welcome to the array creation and editing program ***")
tets = ArrayList()
while True:
    print("Choose an option:")
    print("\t1) Create a new array without specified index.")
    print("\t2) Create a new array with specified index.")
    print("\t3) Remove an element from the array with specified index.")
    print("\t4) Search an element from the array with specified index.")
    print("\t5) Search the index of an element.")
    print("\t6) Reverse the array.")
    print("\t7) Show the array.")
    print("\t8) Exit.")
    entery = int(input("Your choice: 8"))

    if entery == 1:
        elements = int(input("Enter the number of elements in the array: "))
        print("Array: ", tets.add_without_index(elements))
        print("-" * 40)
    elif entery == 2:
        elements = int(input("Enter the number of elements in the array: "))
        print("Array: ", tets.add_with_index(elements))
        print("-" * 40)
    elif entery == 3:
        if len(tets.array) == 0:
            print("Your array is empty! Please first create a new array.")
            print("-" * 40)
        else:
            index = int(input("Enter index of the element you want to remove: "))
            if not 0 <= index < len(tets.array):
                print("Index out of range! Try again!")
                print("-" * 40)
            else:
                print("Updated array: ", tets.remove_element(index))
                print("-" * 40)
    elif entery == 4:
        if len(tets.array) == 0:
            print("Your array is empty! Please first create a new array.")
            print("-" * 40)
        else:
            index = int(input("Enter the index to search: "))
            if not 0 <= index < len(tets.array):
                print("Index out of range! Try again!")
                print("-" * 40)
            else:
                print("The element you searched for: ", tets.search_element(index))
                print("-" * 40)
    elif entery == 5:
        if len(tets.array) == 0:
            print("Your array is empty! Please first create a new array.")
            print("-" * 40)
        else:
            element = int(input("Enter the element to search: "))
            if element not in tets.array:
                print("The element you entered does not exist! Try again!")
                print("-" * 40)
            else:
                print("The index of the element you entered is: ", tets.search_index(element))
                print("-" * 40)
    elif entery == 6:
        if len(tets.array) == 0:
            print("Your array is empty! Please first create a new array.")
            print("-" * 40)
        else:
            print("Reversed array: ", tets.reverse_array())
            print("-" * 40)
    elif entery == 7:
        if len(tets.array) == 0:
            print("Your array is empty! Please first create a new array.")
            print("-" * 40)
        else:
            print("Array: ", tets.array)
            print("-" * 40)
    elif entery == 8:
        print("Exiting the program...")
        time.sleep(2)
        print("Goodbye!")
        break
    else:
        print("Invalid input!")
        print("-" * 40)