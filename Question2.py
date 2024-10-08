import random #This imports a module named random, whcih is being used to give random numbers to my code.

#I Brendan Dileo, certify's that this work is my own effort and that I have not allowed anybody else to copy from it.

amount = random.randint(0,20) + round( random.randint(0,100)/100, 2 ) #The random module is assigned to the 'random' variable which represents the amount the user will owe. The amount owe'd will be a integer value from 0 to 20, and rounded to two decimal places.

def change_calculator(): #This is my function for calculating change.
    amount_owed = amount #The amount that is owed is assigned to the module from line 1 and line 5.
    print(" You owe $", amount_owed) #This shows the user how much the module randomly generated, therefore how much the user will owe.

    money_given = float(input(" Enter how much youll be paying with: ")) #This asks the user for the amount of money they will be using to pay with.

    change = money_given - amount_owed #This shows the amount in change the user will get by subtracting the money given by the amount owed.

    if change == 0:
        print(" You get no change! ") #If the user gets no change, the program shows them that they owe no change and have given an exact payment.

    elif change > 0: #If the user does need to receive change, we continue to the calculations below.
        change = money_given - amount_owed

        dollars = int(change) #This is a calculation to show the total number of dollars the user is owe'd.
        change = change - dollars

        quarters = int(change // 0.25) #This is a calculation to show the total number of quarters the user is owe'd.
        change = change - quarters * 0.25

        dimes = int(change // 0.10) #This is a calculation to show the total number of dimes the user is owe'd.
        change = change - dimes * 0.10

        nickels = (round(change / 0.05)) #This is a calculation to show the total number of nickels the user is owe'd, but also rounds to the nearest nickel, because pennies are no longer used.

        if nickels == 2: #This makes sure the user is given 1 dime, instead of two nickels providing the least amount of change.
            dimes = dimes + 1
            nickels = 0

        if dimes == 2 and nickels == 1: #This makes sure the user is given 1 quarter, instead of two dimes, and one nickel providing the least amount of change.
            quarters = quarters + 1
            dimes = 0
            nickels = 0

        if quarters == 4: #This makes sure the user is given 1 dollar, instead of four quarters, providing the least amount of change.
            dollars = dollars + 1
            quarters = 0

        print(" Your change is ", dollars, " in dollars, ", quarters, " in quarters, ", dimes, " in dimes, ", nickels, " in nickels. ") #This shows the user how much they will be getting in change, after all calculations.

    else:
        print(" Payment error! You owe more than you have given!") #If the user tries to pay with less than what they owe, they will be told that theyre payment is insufficent.

change_calculator() #Here I have called upon my fucntion, so that it will run.
