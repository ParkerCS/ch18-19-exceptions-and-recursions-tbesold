'''
- Personal investment
Create a single recursive function (or more if you wish), which can answer the first three questions below.  For each question, make an appropriate call to the function. (5pts each)
'''

#1.  You have $10000 on a high interest credit card with an APR of 20.0% (calculated MONTHLY, so MPR is APR/12).  Assuming you make no payments for 6 months, what is your new balance?  Solve recursively.


def cash(money, months):
    money +=  .2 / 12 * money
    if months == 6:
        print("you have", money, "dollars")
    else:
        cash(money, months + 1)


cash(10000, 1)


#2.  You have $5000 on a high interest credit card with an APR of 20.0% (calculated MONTHLY).  You make the minimum payment of $100 per month for 36 months.  What is your new balance?  Solve recursively.
#make a function to calculate a factorial


def cash2(money, months):
    money += .2 / 12 * money
    money -= 100
    if months == 36:
        #print(money_paid)
        #print(money)
        print("you have", money, "dollars")
    else:
        cash2(money, months + 1)

cash2(5000, 1)





#3.  You have $10000 on a high interest credit card with an APR of 20.0% (calculated MONTHLY).  If you make the minimum payment of $100 per month, how many months will it take to pay it off?  Solve recursively.

'''
can't pay off

def credit(money, money_paid, months):
    money += .02 * money
    money_paid += 100
    if money - money_paid <= 0:
        print(months)
    else:
        credit(money, money_paid, months + 1)

credit(10000, 0, 1)
'''


#4  Pyramid of Cubes - (10pts) If you stack boxes in a pyramid, the top row would have 1 box, the second row would have two, the third row would have 3 and so on.  Make a recursive function which calculates the TOTAL NUMBER OF BOXES for a pyramid of boxes n high.  For instance, a pyramid that is 3 high would have a total of 6 boxes.  A pyramid 4 high would have 10.

n = int(input("enter a number: "))

def pyr(n, boxes):
    boxes += n
    if n == 0:
        print("there are", boxes, "boxes")
    else:
        pyr(n - 1, boxes)


pyr(n, 0)