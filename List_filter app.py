#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def list_filter(list=[]):
    pass


# In[ ]:


while True:
    list_size = (input("Enter number of items in list...\n"))
    if int(list_size) == 0:
        print("List must contain Numbers")
    else:
        print("Constructing List...")
        full_list = list(range(int(list_size) + 1))
        print("List contains: ", full_list)
    try:
        val = int(list_size)
        print("List size is: ", val)
        break;
    except ValueError:
        print("This is not a Number.\nPlease enter a valid Number")


# In[ ]:


numbers_to_filter = input("Enter type of number to select...\n 'E' for Even Number and 'O' for Odd Number \n").capitalize()
if numbers_to_filter == "E":
    print("Sorting Even Numbers...")
    print("The Even numbers in the list are: ")
    for x in full_list:
        if x % 2 == 0:            
            print(x)
elif numbers_to_filter == "O":
    print("Sorting Odd Numbers...")
    print("The Odd numbers in the list are: ")
    for x in full_list:
        if x % 2 == 1:          
            print(x)
else:
    print("Invalid Option")
    print("Enter 'E' or 'O'")
    
list_filter(full_list)


# In[ ]:





# In[ ]:




