# CALCULATOR 3

print("CALCULATOR")

while (True):
    n1 = float(input("Enter a value for number 1 : "))
    n2 = float(input("Enter a value for number 2 : "))

    while(True):
        print("Select an operation")
        print("1. ADDITION")
        print("2. SUBTRACTION")
        print("3. MULTIPLICATION")
        print("4. DIVISION")
        print("5. FLOOR DIVISION")
        print("6. EXPONENTIAL")
        print("7. MODULUS")
        print("8. EXIT")

        choice = int(input("Select an operation : "))
        print("Selected operation : ",choice)

        if choice == 1:
            a = n1 + n2
            print("ADDITION : ",a)

        elif choice == 2:
            s = n1 - n2
            print("SUBTRACTION : ",s)

        elif choice == 3:
            m = n1*n2
            print("MULTIPLICATION : ",m)

        elif choice == 4:
            d = n1/n2
            print("DIVISION : ",d)

        elif choice == 5:
            fd = n1//n2
            print("FLOOR DIVISION : ",fd)

        elif choice == 6:
            e = n1 ** n2
            print("EXPONENTIAL : ",e)

        elif choice == 7:
            mo = n1 % n2
            print("MODULUS : ",mo)

        elif choice == 8:
            print("EXIT")
            break

    else:
        print("Enter a valid operation")
        break









        


