#Python Slot Machine Game
import random


def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐" ]
    # results = []
    # for symbol in range(3):
    #     results.append(random.choice(symbols))
    # return results
    return [random.choice(symbols) for _ in range(3)]


def print_row(row):
    print("------------------")
    print("   |  ".join(row))
    print("------------------")


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return  bet * 3
        elif row[0] == "🍉":
            return  bet * 4
        elif row[0] == "🍋":
            return  bet * 5
        elif row[0] == "🔔":
            return  bet * 20
        elif row[0] == "⭐":
            return  bet * 50
    return 0


def slot() :
    balance = 100

    print("|===========================================|")
    print("|           Welcome to Slot Machine         |")
    print("|===========================================|")
    print("|                                           |")
    print("|          Symbols : 🍒 🍉 🍋 🔔 ⭐        |")
    print("|                                           |")
    print("|===========================================|")

    while balance > 0:
        print(f"Current Balance: ${balance} ")
        bet = input("Enter your bet amount: ")

        if not bet.isdigit():
            print("Please enter the valid number")
            continue
        bet = int(bet)
        if bet <= 0 :
            print("Please enter the number in positive and not in negative")
            continue
        if bet > balance:
            print("Please the appropriate amount within your balance")
            continue
        balance -= bet

        row = spin_row()
        print("spinning ... \n")
        print_row(row)

        payout = get_payout(row,bet)

        if payout > 0 :
            print(f"You win! 🎉{payout} ")
        else:
            print("You lose! Try again.")

        balance += payout
        print(f"Your new balance is: ${balance}")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break
    print("|===========================================|")
    print(f"|Game Over! Your final balance is: ${balance}|")
    print("Thank you for playing Slot Machine! Come back again 💲💲💲")
    print("|===========================================|")
if __name__ == '__main__':
    slot()