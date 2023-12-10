# Exercise 3
#Ask user's weight in pounds and convert to KG 
name = input ('Hi there, whats your name
? ')
weight= int(input ('Nice to meet you ' + name + '. Tell me your weight in pounds and il'll convert it to kilograms. '))
weight_kg = weight / 2.205
print ('Your weight in kilogram is ', weight_kg)

#Exercise 4 
#Price of a house is $1M. If buyer has good credit, they need to put down 10%Otherwisethey need to put down 20%
price_house = 1000000
credit_score = True

if credit_score :
    down_payment = price_house * 0.10
else :
    down_payment = price * 0.20

print(f'your down paymentis{down_payment}')

print ('End of program')