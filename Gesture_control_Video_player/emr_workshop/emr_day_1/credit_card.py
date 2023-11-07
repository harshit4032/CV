# def mycardnumber (num):
def card_num (num):
    if len(num)==16:
        num = num[12:17]
        star = '*'*12
        print(star+num)
    else :
        print('Invalid Creadit card number')
num = input("Enter the Credit Card Number : ")
card_num(num)


    