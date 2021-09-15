"""
Author: Your Name, login@purdue.edu
Assignment: m.n - Assignment Name
Date: MM/DD/YYYY

Description:
    Describe your program here.

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

    packages = int(input('How many packages will be purchased: '))
    price = 79.0

    if packages >= 0:
        if packages <= 4:
            print('No Discount Applied.')
        elif packages <= 24:
            print ('10% discount applied.')
            price = price * .9
        elif packages <= 49:
            print ('20% discount applied.')
            price = price *.8
        elif packages <= 99:
            print ('30% discount applied')
            price = price * .7
        else:
            print ('45% discount applied')
            price = price * .55

        float(packages)
        total = price * packages
        print(f'The total price for purchasing {packages:,} packages is ${total:,.2f}.')

    else:
        print("Invalid Input!")



if __name__ == '__main__':
    main()
