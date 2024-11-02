
pin = 1234
balance = 50000
avail_balance = balance

print("          * Insert a Card *\n")
while 1:
    Enterd_PIN = int(input("Please Enter your Secrete Number : "))
    if ( pin == Enterd_PIN):

        print('''
        
                           * Wel-come to xyz bank *
        
        
         1. balance Enquiry                                  2. Withdrowal

         3. diposite                                         4. change pin
         
         5. exit. ''')

        list1 = [ 1 , 2 ,3 ,4 ,5]

        choice = int(input("   Choice  : "))
        if choice in list1:

            match choice:
                case 1:
                    print("  availabele balance : ", avail_balance)
                
                case 2:
                    print("      * withdrowal *\n")
                    wit = int(input("Enter amount : "))
                    if wit <= avail_balance:
                        print("Rs.",wit," withdrowaled \n")
                        avail_balance = avail_balance - wit
                        print("Available balance : ",avail_balance)
                        
                    else:
                        print("  not enogh balance.")
                        break

                case 3:
                    print("      * Diposite *\n")
                    dip = int(input("Enter amount : "))
                    avail_balance = avail_balance + dip
                    print("Available balance : ", avail_balance)

                case 4:
                    print("      * Generating new PIN *  ")

                    pin = int(input("Enter new PIN : "))
                    print("PIN has beed changed successfully...") 
                    continue

                case 5:
                    print("Thank you")
                    break                   



        else :
            print(" oops!,  please select right opetion")  
            break     


    else:
        print("  oops! ,Invalid pin try again.")
        continue

