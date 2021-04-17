import random
import time

database = {}


class budget:

    def init():
        print("Welcome to OOO budget app\n")
        input_decision = int(
            input("What would you be doing today?\npress\n1. to login\n2. to register\n"))

        if input_decision == 1:
            return 1

        elif input_decision == 2:
            return 2
        else:
            print("Invalid entry")

    def register():
        Y = ['Y', 'y', "Yes", "yes", 'YES']
        N = ['N', 'n', 'No', 'no', 'NO']

        print("Please fill the form\n")
        Fname = input("Please enter your first name:\n")
        Lname = input("Please enter yout last name\n")
        email = input("Please enter your email\n")
        userName = input("What would you like to use as your username?\n")
        password = input("Please enter your preferred password\n")
        food_bal = 0
        clothing_bal = 0
        entertainment_bal = 0
        health_bal = 0
        Transportation_bal = 0
        Subscription_bal = 0
        database[email] = [Fname, Lname, userName,
                           email, password, food_bal, clothing_bal,
                           entertainment_bal, health_bal,
                           Transportation_bal, Subscription_bal
                           ]

        print("Saving your details...")
        time.sleep(3)
        print("Your account has been created!")
        time.sleep(2)

        askToLogin = input(
            "Would you like to login to your account?(Yes/No)\n")

        if askToLogin in Y:
            budget.login()

        elif askToLogin in N:
            budget.init()

        else:
            budget.init()

    def login():
        # login to the system
        # ask what category you would like to go to
        print("Loading...")
        time.sleep(2)
        print("Login to your account")
        loginError = 0
        isLoginSuccesful = False

        while loginError < 4:
            loginError += 1
            email = input("Please enter your email login\n")
            password = input("Please enter your preferred password\n")

            for user, userDetails in database.items():
                if (user == email) and (userDetails[4] == password):
                    isLoginSuccesful = True
                    budget.budgetOperations(userDetails)

        print("invalid user")
        time.sleep(2)
        decisions = input(
            "would you like to remember forgot password?\n 1. forgot password\n 2. back to login page\n 3. back to homepage")

        try:
            decision = int(decisions)
            if decision == 1:
                budget.forgotPassword()
            elif decision == 2:
                budget.login()
            elif decision == 3:
                budget.init()
        except:
            print("Invalid entry!")
            budget.init()

    def budgetOperations(user):
        print("Loading...")
        time.sleep(2)
        print("welcome %s %s" % (user[0], user[1]))
        time.sleep(1)
        print("What will you be doing today?")
        time.sleep(1)
        print("Press 1 to check balance")
        print("Press 2 to deposit funds")
        print("Press 3 to withdraw funds")
        print("Press 4 to move funds from one category to another")
        print("Press 5 to lodge a complaint")
        print("Press 6 to logout")
        print("Press 7 to exit")

        select = input("please select an option:\n")

        try:
            select_Operation = int(select)
            if select_Operation == 1:
                budget.category_balance(user)

            elif select_Operation == 2:
                budget.deposit(user)

            elif select_Operation == 3:
                budget.withdraw(user)

            elif select_Operation == 4:
                budget.fund_mover(user)

            elif select_Operation == 5:
                budget.complaint(user)

            elif select_Operation == 6:
                budget.Logout()

            elif select_Operation == 7:
                exit()
        except:
            print("Wrong entry!")
            budget.budgetOperations(user)

    def category_balance(user):
        # show all the balance for each category
        # Show the total
        print("Loading...")
        time.sleep(2)
        sums = 0
        # print(user[5:-1])
        print("Food balance:-             ", user[5])
        print("Clothing balance:-         ", user[6])
        print("Entertainment balance:-    ", user[7])
        print("Health balance:-           ", user[8])
        print("Transportation balance:-   ", user[9])
        print("Subscription balance:-     ", user[10])
        for sum in user[5:-1]:
            sums += sum
        print("Total balance:-", sums)
        budget.budgetOperations(user)

    def deposit(user):
        print("Loading...")
        time.sleep(2)
        print("Enter a number to which category you would like to fund")
        print("1. Food\n2. Clothing\n3. Entertainment\n4. Health\n5. Transportation\n6. Subscription")

        select = input("Enter a number:\n")
        try:
            select_Option = int(select)
            if select_Option == 1:
                amount_entry = int(
                    input("How much would you like to deposit to your food wallet?\n"))
                user[5] += amount_entry
                budget.budgetOperations(user)

            elif select_Option == 2:
                amount_entry = int(
                    input("How much would you like to deposit to your clothing wallet?\n"))
                user[6] += amount_entry
                budget.budgetOperations(user)

            elif select_Option == 3:
                amount_entry = int(
                    input("How much would you like to deposit to your entertainment wallet?\n"))
                user[7] += amount_entry
                budget.budgetOperations(user)

            elif select_Option == 4:
                amount_entry = int(
                    input("How much would you like to deposit to your health wallet?\n"))
                user[8] += amount_entry
                budget.budgetOperations(user)

            elif select_Option == 5:
                amount_entry = int(
                    input("How much would you like to deposit to your transportation wallet?\n"))
                user[9] += amount_entry
                budget.budgetOperations(user)

            elif select_Option == 6:
                amount_entry = int(
                    input("How much would you like to deposit to your subscription wallet?\n"))
                user[-1] += amount_entry
                budget.budgetOperations(user)
        except:
            print("Wrong entry!")
            budget.budgetOperations(user)

    def withdraw(user):
        print("Loading...")
        time.sleep(3)
        print("Enter a number to which category you would like to withdraw funds from")
        print("1. Food\n2. Clothing\n3. Entertainment\n4. Health\n5. Transportation\n6. Subscription")

        select = int(input("Enter a number:\n"))

        try:
            select_Option = int(select)
            if select_Option == 1:
                amount_entry = int(
                    input("How much would you like to withdraw from your food wallet?\n"))
                if amount > user[5]:
                    print("insufficient funds")
                    budget.budgetOperations(user)
                else:
                    time.sleep(3)
                    print("please take your cash")
                    user[5] -= amount_entry
                    budget.budgetOperations(user)

            elif select_Option == 2:
                amount_entry = int(
                    input("How much would you like to withdraw from your clothing wallet?\n"))
                if amount > user[6]:
                    print("insufficient funds")
                    budget.budgetOperations(user)
                else:
                    time.sleep(3)
                    print("please take your cash")
                    user[6] -= amount_entry
                    budget.budgetOperations(user)

            elif select_Option == 3:
                amount_entry = int(
                    input("How much would you like to withdraw from your entertainment wallet?\n"))
                if amount > user[7]:
                    print("insufficient funds")
                    budget.budgetOperations(user)
                else:
                    time.sleep(3)
                    print("please take your cash")
                    user[7] -= amount_entry
                    budget.budgetOperations(user)

            elif select_Option == 4:
                amount_entry = int(
                    input("How much would you like to withdraw from your health wallet?\n"))
                if amount > user[8]:
                    print("insufficient funds")
                    budget.budgetOperations(user)
                else:
                    time.sleep(3)
                    print("please take your cash")
                    user[8] -= amount_entry
                    budget.budgetOperations(user)

            elif select_Option == 5:
                amount_entry = int(
                    input("How much would you like to withdraw from your transportation wallet?\n"))
                if amount > user[9]:
                    print("insufficient funds")
                    budget.budgetOperations(user)
                else:
                    time.sleep(3)
                    print("please take your cash")
                    user[9] -= amount_entry
                    budget.budgetOperations(user)

            elif select_Option == 6:
                amount_entry = int(
                    input("How much would you like to withdraw from your subscription wallet?\n"))
                if amount > user[-1]:
                    print("insufficient funds")
                    budget.budgetOperations(user)
                else:
                    time.sleep(3)
                    print("please take your cash")
                    user[-1] -= amount_entry
                    budget.budgetOperations(user)
        except:
            print("Wrong entry!")
            budget.budgetOperations(user)

    def fund_mover(user):
        print("Loading...")
        time.sleep(2)
        a = user
        b = a

        move_from = int(input(
            "Where would you like to move funds from?\n5.Food\n6. clothing\n7. Entertainment\n8. Health\n9. Transportation\n10. Subscription\n"))
        move_to = int(input(
            "Where would you like to move funds to?\n5.Food\n6. clothing\n7. Entertainment\n8. Health\n9. Transportation\n10. Subscription\n"))
        amount = int(input("How much would you like to move?\n"))
        s = a[move_from] - amount
        b[move_from] = s
        b[move_to] = amount
        # print(b)
        budget.budgetOperations(b)

    def complaint(user):
        print("Loading...")
        time.sleep(2)
        comp_laint = input("Enter your complaint\n")
        time.sleep(1)
        print("Thank you for your feedback")
        budget.budgetOperations(user)

    def forgotPassword():
        print("Loading page...")
        time.sleep(2)
        enterUserName = input(
            "Please enter your username to confirm if user exist\n")

        for email, user in database.items():

            if (enterUserName != user[2]):
                print("User does not exist")
                print("going back to login page...")
                time.sleep(3)
                break

            else:
                print("Your email is", email)
                print("Your password is ", user[4])
                time.sleep(5)
                print("going back to login page...")
                time.sleep(1)
                budget.init()

        # init()

    def Logout():
        print("Thank you for  with us")
        time.sleep(3)
        budget.init()
        pass


while(1):
    input_decision = budget.init()

    if input_decision == 1:
        budget.login()

    elif input_decision == 2:
        budget.register()
