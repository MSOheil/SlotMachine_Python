import random

MAX_LINES=3
MAX_BET=100
MIN_BET=1
ROWS =3
COLS=3

symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8,
}
def get_slot_machine_spin(rows,cols,symbols):
    all_symbols =[]
    
def Deposit():
    while True:
        amount=input("What would you like to deposit? $")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("{amount} must be greater than 0.")
        else:
            print("PLease enter a number")

    return amount

def get_number_of_lines():
    while True:
        lines=input("Enter the number of line to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines=int(lines)
            if  1<=lines<=MAX_LINES:
               break
            else:
                print("Enter a valid number of lines.")
        else:
            print("PLease enter a number")

    return lines

def get_bet():
    while True:
        amount=input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET<=amount<=MAX_BET:
                break
            else:
                print(f" must be greater between. ${MAX_BET} - ${MAX_BET}")
        else:
            print("PLease enter a number")
    return amount
def main():
    balance= Deposit()
    lines= get_number_of_lines()
    bet= get_bet()
    total_bet=bet*lines
    if total_bet>balance:
        print(f"You don't have enough to bet that amount, your current balance is : ${balance}")
    else:
        break

    print(f"you are betting ${bet} on ${lines} lines. total bet is equal to ${total_bet}")

main()