#[RACTICAL 6
'''
empt_dict = {}
print("DICCTIONARY FUNCTIONS")
print("1.To add element")
print("2.To get all keys")
print("3.To get all values")
print("4.To get all items")
print("5.To get value of a key")
print("6.To remove value of a key")
print("7.To replace value of a key")
print("8.To remove last element")
print("9.To copy dictionary")
print("10.To clear dictionary")
print("11.To view dictionary")
print("12.Exit\n")

while True:
    try:
        choice = int(input("Enter number of choice : "))

        if choice == 1:
            key = input("Enter the key: ")
            val = input("Enter the value: ")
            empt_dict.update({key:val})
            print("Dictionary : ",empt_dict)

        elif choice == 2:
            print("All keys in dictionary : ",list(empt_dict.keys()))

        elif choice == 3:
            print("values : ",list(empt_dict.values()))

        elif choice == 4:
            print("Items : ",list(empt_dict.items()))

        elif choice == 5:
            key = input("Enter the key : ")
            value = empt_dict.get(key,"key not found")
            print(f"value of {key} is : {value}.")

        elif choice == 6:
            key = input("Enter the key : ")
            if key in empt_dict:
                empt_dict.pop(key)
                print("Dictionary after poping : ",empt_dict)
            else:
                print(f"key {key} not found!")

        elif choice == 7:
            key = input("Enter the key : ")
            if key in empt_dict:
                new_val = input("Enter the new value : ")
                empt_dict.update({key:new_val})
                print("Updated dictionary : ",empt_dict)
            else:
                print(f"key {key} not found!")

        elif choice == 8:
            print("Dictionary after removing last element : ",empt_dict.popitem())

        elif choice == 9:
            copy_dict = empt_dict.copy()
            print("copy of dictionary : ",copy_dict)

        elif choice == 10:
            empt_dict.clear()
            print("Dictionary is cleared : ",empt_dict)

        elif choice == 11:
            print("Dictionary : ",empt_dict)

        elif choice == 12:
            print("=" * 30)
            break
        else:
            print("Invalid number! Please enter a valid number.\n")

    except ValueError:
        print("Please enter a valid number choice")
'''
#========================================================================================================================

'''
n = 5
for i in range(1,n+1):
    for j in range(n - i):
        print(" ",end=" ")
    for k in range(1,2*i):
        print("*",end=" ")
    print()
n = 5
for i in range(n,0,-1):
    for j in range(n - i):
        print(" ",end=" ")
    for k in range(0,2*i-1):
        print("*",end=" ")
    print()
'''

r = open("ML.docx","rt")





                




            

        
