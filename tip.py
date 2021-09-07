'''
Your goal is to find out exactly how much tip you should give after receiving a service. In this scenario, ask for the total bill. Then display the tip for 18%, 20% and 25%.

'''

def total_bill():
    amount = int(input('Enter the amount of the bill: '))

    tip_18 = amount * .18
    tip_20 = amount * .20
    tip_25 = amount * .25

    print(f'Total price with 18% tip is: {amount + tip_18}')
    print(f'Total price with 20% tip is: {amount + tip_20}')
    print(f'Total price with 25% tip is: {amount + tip_25}')

total_bill()