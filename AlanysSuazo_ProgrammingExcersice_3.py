# Alanys Suazo-Gracia
# Assignment: Programming Exersice 3

# The purpose of this program is to show the user's monthly expenses. Based on user input, the program should:
#  create a list/dictionary where eah expense is labeled, after which the program will analyse and show
#  what is the highest, lowest, and total expenses.

# used to get and return total expenses
def get_total(expences):
    return sum(expences.values())

# used to get and return the highest expense
def get_highest(expenses):
    highest_value = max(expenses.values())
    for name, amount in expenses.items():
        if amount == highest_value:
            return name, amount

#used to get and return the lowest expense
def get_lowest(expenses):
    lowest_value = min(expenses.values())
    for name, amount in expenses.items():
        if amount == lowest_value:
            return name, amount

# collects user input to create an expenses dictionary
def main():
    # user subscriptions
    expenses = {}

    # making a while loop to ask user to add to the dictionary
    while True:
        name = input("Enter the name of you subscription. Once you're finished, type 'done'. ")
        if name.lower() == 'done':
            break
        try:
            amount = float(input(f"Enter the cost for {name}: "))
            expenses[name] =  amount
        except ValueError:
            print('Please input an actual number')

    #printing the results
    total = get_total(expenses)
    high_name, high_value = get_highest(expenses)
    low_name, low_value = get_lowest(expenses)

    print(f'Total monthly expenses: ${total:.2f}')
    print(f'Highest expense: {high_name}(${high_value:.2f})')
    print(f'Lowest expense: {low_name} (${low_value:.2f})')

#running program
if __name__ == "__main__":
    main()