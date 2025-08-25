# Alanys Suazo-Gracia
# Assignment: Programming Exercise 1

# The Purpose of this assignment/exercise is to write an application that sells movie tickets.
# Criteria for the assignment: must have at least 2 functions, an input, an output, an accumulator,
#   an if statement, and a loop

# making variables for the tickets_available and buyer_count
tickets_available = 20
buyer_count = 0

# the functions for the prompt asking the user how many tickets they want to purchase
def ticket_prompt():
    try:
        requested = int(input("4 tickets MAX. How many would you like?"))
        if 1 <= requested <= 4:
            return requested
        elif requested < 1:
            print('I dont know why you want null tickets but ok...')
            return 0
        elif requested > 4:
            print('Buddy, I said 4 MAX!')
            return 0
    except ValueError:
        print('what are you even typing?')
        return 0

# function for calculating the purchase, the buyer count, the tickets available
def calculations(requested, tickets_available):
    if requested <= tickets_available:
        tickets_available -= requested
        print(f'You got {requested} ticket(s).')
        return tickets_available, True
    else:
        print(f'Darn! There arent enought tickets for you to buy {requested}. Only {tickets_available} remaining.')
        return tickets_available, False

# the function for looping the program until all tickets are sold
def loopdeloop():
    global tickets_available, buyer_count
    while tickets_available > 0:
        requested = ticket_prompt()
        if requested == 0:
            continue
        tickets_available, success = calculations(requested, tickets_available)
        if success:
            buyer_count += 1
    print(f"All tickets sold! Total Buyers: {buyer_count}")

# running with it!
loopdeloop()