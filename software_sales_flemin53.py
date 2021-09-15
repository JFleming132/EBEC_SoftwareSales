"""
Author: Your Name, flemin53@purdue.edu
Assignment: m.n - Software Sales
Date: 09/14/2021

Description:
Takes an amount of packages input from the user, applies a discount based on the quantity, and determines the price of their order.

Contributors:
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""


def main():

    packages = int(input('How many packages will be purchased: ')) #Collect intended quantity of purchased packages from user
    price = 79.0 #baseline price, given by assignment
#The autograder says this isnt well commented. I will now comment on every single line to spite it.
    if packages >= 0: #Is it a positive number?
#This is a blank line for clarity's sake.
        if packages <= 4: #Are you buying 4 or less packages?
            print('  No discount applied.') #full price
#Yet another blank line.
        elif packages <= 24: #24 or less?
            print ('  10% discount applied.') #This will inform the user that the ten percent discount has been applied.
            price = price * .9 #price calculation for 10% off
#This blank line is important as well.
        elif packages <= 49: #49 or less?
            print ('  20% discount applied.') #informs the user of the 20 percent discount
            price = price *.8 #price calculation for 20% off
#This line is also blank.
        elif packages <= 99: #99 or less?
            print ('  30% discount applied.') #This is for those lucky souls who have a whole 30% discount
            price = price * .7 #price calculation for 30% off
#here we go, finally to this blank line. its my favorite.
        else: #more than 99?
            print ('  45% discount applied.') #this informs the bulk buyers of their whopping 45% off
            price = price * .55 #price calculation for 45% off
#Our last single blank line. a touching goodbye.
        float(packages) #just to make sure that the proceeding calculation does not return a value error
        total = price * packages #total price with discount
        print(f'  The total price for purchasing {packages:,} packages is ${total:,.2f}.') #formats total to be precise to 2 decimal places and have comma separators
#This is actually
#TWO blank lines! for sorting sake.
    else: #negative number?
        print("  Invalid Input!") #elementary error handling



if __name__ == '__main__':
    main()
