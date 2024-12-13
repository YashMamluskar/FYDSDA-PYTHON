print("\n========= Welcome to Loan EMI Calculator =========")
print()

while(True): # Infinite loop for main menu
    try: 
        # Displaying bank options to the user
        print("Select the Bank for your loan:")
        print("1. HDFC Bank of India")
        print("2. SBI Bank of India")
        print("3. Exit Calculator") 

        # Taking user input for bank selection
        choice = int(input("Enter the number corresponding to your Bank: "))

        if choice == 1: # HDFC Bank selected
            print("\n\n🏦 HDFC BANK OF INDIA")
            while(True): # Infinite loop for loan type selection
                try: 
                    # Displaying loan types available at HDFC Bank
                    print("\nSelect the Type of Loan")
                    print("1. Personal Loan EMI Calculator")
                    print("2. Car Loan EMI Calculator")
                    print("3. Home Loan EMI Calculator") 
                    print("4. Exit to Bank Selection")

                    # Taking user input for loan type selection
                    choice=int(input("Enter the number corresponding to your loan type: "))

                    if choice == 1: # Personal Loan selected
                        print("\n📋 Personal Loan EMI Calculator\n")
                        while(True): # Loop until valid loan amount is entered
                            try: 
                                amount = int(input("Enter the loan amount (₹50,000 - ₹40,00,000) : ")) 
                                if (50000 <= amount <= 4000000):
                                    print()
                                    break
                                else:
                                    print("⚠️ Please enter a valid amount within the range.\n")
                                    continue
                            except ValueError:
                                print("❌ Invalid input! Please enter an integer value.\n")
                            
                        while(True): # Loop until valid loan tenure is entered
                            try: 
                                no_of_year = int(input("Enter loan tenure (1 - 5) : "))
                                if (1 <= no_of_year <= 5):
                                    print()
                                    break
                                else:
                                    print("⚠️ Please enter a valid tenure within the range.\n")
                                    continue
                            except ValueError:
                                print("❌ Invalid input! Please enter an integer value.\n") 
                        n = no_of_year * 12 # Convert years to months
                                
                        while(True): # Loop until valid interest rate is entered
                            try: 
                                rate_of_interest = float(input("Enter Rate of Interest (10.5% - 21%) : "))
                                if (10.5 <= rate_of_interest <= 21):
                                    print()
                                    break
                                else:
                                    print("⚠️ Please enter a valid interest rate within the range.\n")
                                    continue
                            except ValueError:
                                print("❌ Invalid input! Please enter a numeric value.\n")
                        r = rate_of_interest/(100 * 12) # Convert annual rate to monthly rate

                        EMI = (amount * r *(1 + r)**n) / ((1 + r)**n - 1)
                        total_payment = EMI * n   # Total amount to be paid over loan period
                        total_interest = total_payment - amount
                        print(f"Your Monthly EMI will be ₹{round(EMI)} per month")
                        print("=================================================================\n")
                        print(f"Total Payment: ₹{round(total_payment)}")
                        print("=================================================================\n")
                        print(f"Total Interest: ₹{round(total_interest)}")
                        print("=================================================================\n")
                       
                        # Asking user if they want to explore more loans
                        continue_choice = input("Do you want to explore more loans in HDFC? (yes/no): ").strip().lower() 
                        if continue_choice == 'no':
                            print(f"\nExiting HDFC Bank Loan Options...\n")
                            print("=================================================================\n")
                            break


                    elif choice == 2: # Car Loan selected
                        print("\n🚗 Car Loan EMI Calculator\n")
                        print("Select the type of car:")
                        print("1. New Car")
                        print("2. Pre-Owned Car") 

                        while(True): # Loop for car type selection
                            try: 
                                # Taking user input for car type
                                choice = int(input("Enter your choice: "))

                                if choice == 1: # New Car Loan
                                    print("\n🚘 New Car Loan\n")
                                    print() 
                                    while(True):
                                        try: 
                                            amount = int(input("Enter the loan amount (₹1,00,000 - ₹19,00,000) : "))
                                            if (100000 <= amount <=1900000):
                                                print()
                                                break
                                            else:
                                                print("⚠️ Please enter a valid amount within the range.\n")
                                                continue
                                        except ValueError:
                                            print("❌ Invalid input! Please enter an integer value.\n")
                                    
                                    while(True):
                                        try: 
                                            no_of_year = int(input("Enter loan tenure (1 - 8) : "))
                                            if (1 <= no_of_year <= 8):
                                                print()
                                                break
                                            else:
                                                print("⚠️ Please enter a valid tenure within the range.\n")
                                                continue
                                        except ValueError:
                                            print("❌ Invalid input! Please enter an integer value.\n")
                                    n = no_of_year * 12 # Convert years to months
                                    
                                    while(True):
                                        try: 
                                            rate_of_interest = float(input("Enter Rate of Interest (7% - 20%) : "))
                                            if (7 <= rate_of_interest <= 20):
                                                print()
                                                break
                                            else:
                                                print("⚠️ Please enter a valid interest rate within the range.\n")
                                                continue
                                        except ValueError: 
                                            print("❌ Invalid input! Please enter a numeric value.\n")
                                    r = rate_of_interest/(100 * 12) # Convert annual rate to monthly rate

                                    EMI = (amount * r *(1 + r)**n) / ((1 + r)**n - 1)
                                    total_payment = EMI * n
                                    total_interest = total_payment - amount
                                    print(f"Your Monthly EMI will be ₹{round(EMI)} per month")
                                    print("=================================================================\n")
                                    print(f"Total Payment: ₹{round(total_payment)}")
                                    print("=================================================================\n")
                                    print(f"Total Interest: ₹{round(total_interest)}")
                                    print("=================================================================\n")
                                    
                                    # Ask if user wants to explore more loans
                                    continue_choice = input("Do you want to explore more loans in HDFC? (yes/no): ").strip().lower()
                                    if continue_choice == 'no':
                                        print(f"\nExiting HDFC Bank Loan Options...\n")
                                        print("=================================================================\n")
                                        break

                                elif choice == 2: # Pre-Owned Car Loan
                                    print("\n🚙 Pre-Owned Car Loan")
                                    print()
                                    while(True):
                                        try: 
                                            amount = int(input("Enter the loan amount (₹50,000 - ₹50,00,000) : "))
                                            if (50000 <= amount <= 5000000):
                                                print()
                                                break
                                            else:
                                                print("⚠️ Please enter a valid amount within the range.\n")
                                                continue
                                        except ValueError:
                                            print("❌ Invalid input! Please enter an integer value.\n")

                                    while(True):
                                        try: 
                                            no_of_year = int(input("Enter loan tenure (1 - 5) : "))
                                            if (1 <= no_of_year <= 5):
                                                print()
                                                break
                                            else:
                                                print("⚠️ Please enter a valid tenure within the range.\n")
                                                continue
                                        except ValueError: 
                                            print("❌ Invalid input! Please enter an integer value.\n")
                                    n = no_of_year * 12 # Convert years to months
                                    
                                    while(True):
                                        try: 
                                            rate_of_interest = float(input("Enter Rate of Interest (13.50% - 17.50%) : "))
                                            if (13.5 <= rate_of_interest <= 17.5):
                                                print()
                                                break
                                            else:
                                                print("⚠️ Please enter a valid interest rate within the range.\n")
                                                continue
                                        except ValueError:
                                            print("❌ Invalid input! Please enter a numeric value.\n")
                                    r = rate_of_interest/(100 * 12) # Convert annual rate to monthly rate

                                    EMI = (amount * r *(1 + r)**n) / ((1 + r)**n - 1)
                                    total_payment = EMI * n
                                    total_interest = total_payment - amount
                                    print(f"Your Monthly EMI will be ₹{round(EMI)} per month")
                                    print("=================================================================\n")
                                    print(f"Total Payment: ₹{round(total_payment)}")
                                    print("=================================================================\n")
                                    print(f"Total Interest: ₹{round(total_interest)}")
                                    print("=================================================================\n")
                                    
                                    # Asking user if they want to explore more loans
                                    continue_choice = input("Do you want to explore more loans in HDFC? (yes/no): ").strip().lower()
                                    if continue_choice == 'no':
                                        print(f"\nExiting HDFC Bank Loan Options...\n")
                                        print("=================================================================\n")
                                        break
                                
                                else:
                                    print("⚠️ Please enter either 1 or 2.\n")
                                    continue

                            except ValueError:
                                print("❌ Invalid input! Please enter 1 or 2.\n")


                    elif choice == 3: # Home Loan selected
                        print("\n🏠 Home Loan EMI Calculator\n")
                        while(True):
                            try: 
                                amount = int(input("Enter the loan amount (₹1,00,000 - ₹10,00,00,000) : "))
                                if (100000 <= amount <= 100000000):
                                    print()
                                    break
                                else:
                                    print("⚠️ Please enter a valid amount within the range.\n")
                                    continue
                            except ValueError:
                                print("❌ Invalid input! Please enter an integer value.\n")
                            
                        while(True):
                            try: 
                                no_of_year = int(input("Enter loan tenure (1 - 30) : "))
                                if (1 <= no_of_year <= 30):
                                    print()
                                    break
                                else:
                                    print("⚠️ Please enter a valid tenure within the range.\n")
                                    continue
                            except ValueError:
                                print("❌ Invalid input! Please enter an integer value.\n")
                        n = no_of_year * 12 # Convert years to months
                        
                        while(True):
                            try: 
                                rate_of_interest = float(input("Enter Rate of Interest (0.5% - 15%) : "))
                                if (0.5 <= rate_of_interest <= 15):
                                    print()
                                    break
                                else:
                                    print("⚠️ Please enter a valid interest rate within the range.\n")
                                    continue
                            except ValueError:
                                print("❌ Invalid input! Please enter a numeric value.\n")
                        r = rate_of_interest/(100 * 12) # Convert annual rate to monthly rate

                        EMI = (amount * r *(1 + r)**n) / ((1 + r)**n - 1)
                        total_payment = EMI * n
                        total_interest = total_payment - amount
                        print(f"Your Monthly EMI will be ₹{round(EMI)} per month")
                        print("=================================================================\n")
                        print(f"Total Payment: ₹{round(total_payment)}")
                        print("=================================================================\n")
                        print(f"Total Interest: ₹{round(total_interest)}")
                        print("=================================================================\n")
                        
                        # Asking user if they want to explore more loans
                        continue_choice = input("Do you want to explore more loans in HDFC? (yes/no): ").strip().lower()
                        if continue_choice == 'no':
                            print(f"\nExiting HDFC Bank Loan Options...\n")
                            print("=================================================================\n")
                            break
                        
                    elif choice == 4: # Exit loan options
                        print(f"\n Exiting HDFC Bank Loan Options...")
                        print("=================================================================\n")
                        break

                    else:
                        print("⚠️ Invalid choice! Please enter a number between 1 and 4.\n")
                        print("=================================================================\n")      
                    continue
                    
                except ValueError:
                    print("❌ Invalid input! Please enter a valid number.\n")


        elif choice == 2: # SBI Bank selected
            print("\n\n🏦 SBI BANK OF INDIA")

            while(True): # Infinite loop for loan type selection
                try: 
                    # Display loan options for SBI Bank
                    print("\nSelect the Type of Loan")
                    print("1. Personal Loan EMI Calculator")
                    print("2. Car Loan EMI Calculator")
                    print("3. Home Loan EMI Calculator")
                    print("4. Exit to Bank Selection")

                    # Get user's choice for loan type
                    choice=int(input("Enter number of Type of loan you want : "))

                    if choice == 1: # Personal Loan selected
                        print("\n📋 Personal Loan EMI Calculator\n")
                        while(True):
                            try: 
                                amount = int(input("Enter the loan amount (₹10,000 - ₹30,00,000) : "))
                                if (10000 <= amount <= 3000000):
                                    print()
                                    break
                                else:
                                    print("⚠️ Please enter a valid amount within the range.\n")
                                    continue
                            except ValueError:
                                print("❌ Invalid input! Please enter an integer value.\n")

                        while(True):
                            try: 
                                no_of_year = int(input("Enter loan tenure (1 - 5) : "))
                                if (1 <= no_of_year <= 5):
                                    print()
                                    break
                                else:
                                    print("⚠️ Please enter a valid tenure within the range.\n")
                                    continue
                            except ValueError:
                                print("❌ Invalid input! Please enter an integer value.\n")
                        n = no_of_year * 12 # Convert years to months
                                
                        while(True):
                            try: 
                                rate_of_interest = float(input("Enter Rate of Interest (1% - 30%) : "))
                                if (1 <= rate_of_interest <= 30):
                                    print()
                                    break
                                else:
                                    print("⚠️ Please enter a valid interest rate within the range.\n")
                                    continue
                            except ValueError:
                                print("❌ Invalid input! Please enter a numeric value.\n")
                        r = rate_of_interest/(100 * 12) # Convert annual rate to monthly rate
                                    
                        EMI = (amount * r *(1 + r)**n) / ((1 + r)**n - 1)
                        total_payment = EMI * n    # Total amount to be paid over loan period
                        total_interest = total_payment - amount
                        print(f"Your Monthly EMI will be ₹{round(EMI)} per month")
                        print("=================================================================\n")
                        print(f"Total Payment: ₹{round(total_payment)}")
                        print("=================================================================\n")
                        print(f"Total Interest: ₹{round(total_interest)}")
                        print("=================================================================\n")
                        
                        # Ask user if they want to explore more loans
                        continue_choice = input("Do you want to explore more loans in SBI? (yes/no): ").strip().lower()
                        if continue_choice == 'no':
                            print(f"\nExiting SBI Bank Loan Options...\n")
                            print("=================================================================\n")
                            break

                    elif choice == 2: # Car Loan selected
                        print("\n🚗 Car Loan EMI Calculator\n")
                        while(True):
                            try: 
                                amount = int(input("Enter the loan amount (₹1,00,000 - ₹30,00,000) : "))
                                if (100000 <= amount <= 3000000):
                                    print()
                                    break
                                else:
                                    print("⚠️ Please enter a valid amount within the range.\n")
                                    continue
                            except ValueError:
                                print("❌ Invalid input! Please enter an integer value.\n")
                                
                        while(True):
                            try: 
                                no_of_year = int(input("Enter loan tenure (1 - 7) : "))
                                if (1 <= no_of_year <= 7):
                                    print()
                                    break
                                else:
                                    print("⚠️ Please enter a valid tenure within the range.\n")
                                    continue
                            except ValueError:
                                print("❌ Invalid input! Please enter an integer value.\n")
                        n = no_of_year * 12 # Convert years to months
                                
                        while(True):
                            try: 
                                rate_of_interest = float(input("Enter Rate of Interest (1% - 30%) : "))
                                if (1 <= rate_of_interest <= 30):
                                    print()
                                    break
                                else:
                                    print("⚠️ Please enter a valid interest rate within the range.\n")
                                    continue
                            except ValueError:
                                print("❌ Invalid input! Please enter a numeric value.\n")
                        r = rate_of_interest/(100 * 12) # Convert annual rate to monthly rate

                        EMI = (amount * r *(1 + r)**n) / ((1 + r)**n - 1)
                        total_payment = EMI * n
                        total_interest = total_payment - amount
                        print(f"Your Monthly EMI will be ₹{round(EMI)} per month")
                        print("=================================================================\n")
                        print(f"Total Payment: ₹{round(total_payment)}")
                        print("=================================================================\n")
                        print(f"Total Interest: ₹{round(total_interest)}")
                        print("=================================================================\n")
                        
                        # Ask user if they want to explore more loans
                        continue_choice = input("Do you want to explore more loans in SBI? (yes/no): ").strip().lower()
                        if continue_choice == 'no':
                            print(f"\nExiting SBI Bank Loan Options...\n")
                            print("=================================================================\n")
                            break

                    elif choice == 3: # Home Loan selected
                        print("\n🏠 Home Loan EMI Calculator\n")
                        while(True):
                            try: 
                                amount = int(input("Enter the loan amount (₹5,00,000 - ₹2,00,00,000) : "))
                                if (500000 <= amount <= 20000000):
                                    print()
                                    break
                                else:
                                    print("⚠️ Please enter a valid amount within the range.\n")
                                    continue
                            except ValueError:
                                print("❌ Invalid input! Please enter an integer value.\n")
                            
                        while(True):
                            try: 
                                no_of_year = int(input("Enter loan tenure (1 - 30) : "))
                                if (1 <= no_of_year <= 30):
                                    print()
                                    break
                                else:
                                    print("⚠️ Please enter a valid tenure within the range.\n")
                                    continue
                            except ValueError:
                                print("❌ Invalid input! Please enter an integer value.\n")
                        n = no_of_year * 12 # Convert years to months
                        
                        while(True):
                            try: 
                                rate_of_interest = float(input("Enter Rate of Interest (4% - 16%) : "))
                                if (4 <= rate_of_interest <= 16):
                                    print()
                                    break
                                else:
                                    print("⚠️ Please enter a valid interest rate within the range.\n")
                                    continue
                            except ValueError:
                                print("❌ Invalid input! Please enter a numeric value.\n")
                        r = rate_of_interest/(100 * 12) # Convert annual rate to monthly rate

                        EMI = (amount * r *(1 + r)**n) / ((1 + r)**n - 1)
                        total_payment = EMI * n
                        total_interest = total_payment - amount
                        print(f"Your Monthly EMI will be ₹{round(EMI)} per month")
                        print("=================================================================\n")
                        print(f"Total Payment: ₹{round(total_payment)}")
                        print("=================================================================\n")
                        print(f"Total Interest: ₹{round(total_interest)}")
                        print("=================================================================\n")
                        
                        # Ask user if they want to explore more loans
                        continue_choice = input("Do you want to explore more loans in SBI? (yes/no): ").strip().lower()
                        if continue_choice == 'no':
                            print(f"\nExiting SBI Bank Loan Options...\n")
                            print("=================================================================\n")
                            break
                
                    elif choice == 4: # Exit loan options
                        print(f"\n Exiting SBI Bank Loan Options...")
                        print("=================================================================\n")      
                        break

                    else:
                        print("⚠️ Invalid choice! Please enter a number between 1 and 4.\n")
                        print("=================================================================\n")      
                    continue

                except ValueError:
                    print("❌ Invalid input! Please enter a valid number.\n")

        elif choice == 3: # To exit calculator
            print("\n🔚 Exiting the Loan EMI Calculator...")
            print("=================================================================\n")      
            break

        else:
            print("⚠️ Invalid choice! Please enter a number between 1 and 3.\n")

    except ValueError:
        print("❌ Invalid input! Please enter a valid number.\n")