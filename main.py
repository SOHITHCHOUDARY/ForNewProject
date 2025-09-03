#-----------------Banking System--------------------#
def show_balance(balance):
    print(f"Your balance amount is 💲{balance:.2f} :")
def deposit():
    amount = float(input("Enter amount to deposit "))
    if amount < 0:
        print("That's invalid number:")
        return 0
    else:
        return  amount
def withdraw(balance):
    amount = float(input("Enter amount to withdraw "))
    if amount > balance:
        print("Amount should be under the balance to withdraw")
        return 0
    elif amount < 0:
        print("Amount should be greater than 0")
        return 0
    else:
        return amount

def main():
    is_running = True
    balance = 0
    while is_running:
        print("🤑🤑🤑🤑🤑🤑🤑🤑🤑🤑🤑🤑🤑🤑🤑🤑🤑🤑🤑🤑")
        print("Welcome to the ATM")
        print("|===========================================|")
        print("|1.Show Balance                             |")
        print("|2.Deposit                                  |")
        print("|3.Withdraw                                 |")
        print("|4.Exit                                     |")
        print("|===========================================|")

        choice = int(input("Enter your choice 1 - 4 :"))

        if choice == 1:
            show_balance(balance)
        elif choice == 2:
            balance += deposit()
        elif choice == 3:
            balance -= withdraw(balance)
        elif choice == 4:
            is_running=False
            print("Thank you for using the ATM. Goodbye!")
        else:
            print("Invalid choice. Please try again.")


    print("Thank you for using the ATM.Come back again 💲💲💲💲!")

if __name__ == '__main__':
    main()
