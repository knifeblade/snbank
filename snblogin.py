import os
import random

title = "\t\t\t\t\t\t\t\t\t\t\t********snb BANK******\n\t\t\t\t\t\t\t\t\t\t\t**********************"
print(title)

with open("staff.txt", "r") as f:
    info = f.readlines()
    info = [x.strip() for x in info]
    username = info[0]
    password = info[1]

login = True
while login:
    act = input("\nEnter'1' or '2'\n\t1 Staff Login\n\t2 Close App\n ")
    try:
        action = int(act)
    except ValueError:
        print("Error! Please enter '1', or '2'. ")
        break
    if action == 2:
        print("Logged out!")
        break
    log_in = True
    while log_in:
        if action == 1:
            userName = input("Username: ")
            passWord = input("Password: ")
            if userName == username and passWord == password:
                print("Successful Login! ")
                log_in = not True
            elif userName != username and passWord != password:
                print("Incorrect Username and Password!")
                print("Try again!")
                userName = input("\nUsername: ")
                passWord = input("Password: ")
                continue
        session = True
        while session:
            tempfile = open("tempsession.txt", "w+t")
            task = int(input("\n\t1 Create New Bank Account\n\t2 Check Account Details\n\t3 Logout\n "))
            if task == 1:
                name = input("Enter the account holder name: ")
                deposit = input("Enter Opening Balance: ")
                acct_type = input("Enter the type of account [C/S]: ")
                email = input("Enter the account holder email: ")
                accountnumber = "".join([str(random.randint(0, 9)) for i in range(0, 10)])
                print("New account number created: " + accountnumber)
                newdetails = open("customer.txt", "a")
                newdetails.write("\n")
                newdetails.write(name)
                newdetails.write("\n")
                newdetails.write(deposit)
                newdetails.write("\n")
                newdetails.write(acct_type)
                newdetails.write("\n")
                newdetails.write(email)
                newdetails.write("\n")
                newdetails.write(accountnumber)
                newdetails.close()
                continue
            if task == 2:
                actNo = input("Account number: ")
                display = open("customer.txt")
                customer = display.readlines()
                customer = [x.strip() for x in customer]
                if actNo == customer[5]:
                    print('Customer Name: ', customer[1])
                    print('Opening Balance: ', customer[2])
                    print('Account Type [C/S]: ', customer[3])
                    print('Account Email: ', customer[4])
                    print('Account Number: ', customer[5])
                    continue
                else:
                    print("Details not Found!")
                    continue
            if task == 3:
                session = not True
                log_in = not True
            tempfile.close()
        os.remove("tempsession.txt")


f.close()