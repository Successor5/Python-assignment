cardNumber = (input("enter card number: "))
print("**********************")
length = len(cardNumber)
print("length of card number:", length)
add = 0
add2 = 0
plus = 0
answer = 0
answer2 = 0
if 13 > length > 16:
    print(" credit card type: invalid")
if cardNumber[:1] == "4":
    print("credit card type: visa card")
elif cardNumber[:1] == "5":
    print("credit card type: master card")
elif cardNumber[:1] == "37":
    print(" credit card type:american express")
elif cardNumber[:1] == "6":
    print("credit card number:discover cards")
else:
    print("credit card validity type:invalid card number")
    print("card number", cardNumber)
sums1 = 0
sum2 = 0
number_list = []
for digit in cardNumber:
    number_list.append(int(digit))
    # print(digit)
for i in range(0, len(cardNumber), 2):
    product = number_list[i] * 2
    if product > 9:
        product = product - 9
    sums1 = sums1 + product
for j in range(1, len(cardNumber), 2):
    sum2 = sum2 + number_list[j]
total = sums1 + sum2
if total % 10 == 0:
    cardNumber = 'valid'
else:
    cardNumber = 'Invalid'
print(f"credit card Status: {cardNumber}")
print("**************************")
