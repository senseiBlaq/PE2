# Exercise 3
#Ask user's weight in pounds and convert to KG
name = input ('Hi there, whats your name? ')
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

#Exercise 5
# check character limit of a name in

name = input("Please enter your name : ")

if len(name) < 3:
    print ("name must be at least 3 characterrs long")
elif len(name) > 50:
    print ("name can be a maximum of 50 characters")
else:
    print ("name looks good")
print("End of program")

#Exercise 5
#Weight converter
weight = int (input ('Enter your weight:'))
unit = input ('(L)bs or (K)g:')

if unit.casefold() == "l":
    weight /= 2.205
    print (f'You are {round(weight)} kilograms')
elif unit.casefold() == "k":
    weight *= 2.20462
    print (f'You are {round(weight)} pounds')
else:
    print ("invalid input")
print ("End of program")

#Exercise 5
key = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1

    if guess == key:
        print('You\'ve won !!')
        break
else:
    print('Sorry you\'ve failed !!')

#Car Game
user_input = ''
end_game ='quit'
check_started = False

while True:
    user_input = input('>').lower()
    if user_input == "help":
        print('start - to start the car\nstop - to stop the car\nquit - to exit')
    elif user_input == 'start':
        if not check_started:
            check_started = True
            print('Car is started and ready to go!')
        else:
            print('Car is already running!')
    elif user_input == 'stop':
        if check_started:
            check_started = False
            print('Car stop.')
        else:
            print('Car is already off!')
    elif user_input == 'quit':
        break
    else:
        print('I don\'t understand that... ')

print('End of progam!!')

#add items in a cart
kart = [20,10,100, 29.99,19.99]
total_cost = 0
for items in kart :
    total_cost += items
print (f'£{total_cost}')
print('End of progam!!')

#Draw alphabet
numbers = [2, 2, 2, 2, 5]

for element in numbers:
    print ('x' * element)
print('\n')
#solution 2
for element in numbers:
    output = ''
    for x in range(element):
        output += 'x'
    print(output)

#find amnd remove duplicate methods in a list
numbers = [2, 2, 4, 6, 3, 4, 6, 1]

for item in numbers:
    dup_num = numbers.count(item)
    if dup_num > 1:
        dup_num_pos = numbers.index(item)
        numbers.pop(dup_num_pos)
print (numbers)
print('End of program !')
soln 2
numbers = [2, 2, 4, 6, 3, 4, 6, 1]
num_clean = []

for number in numbers:
    if number not in num_clean:
        num_clean.append(number)

print(num_clean)

print('End of program')

#phone numbers to words
phone_number = input('Phone: ')
number_spellings = {
    '0': 'zero ',
    '1': 'one ',
    '2': 'two ',
    '3': 'three ',
    '4': 'four ',
    '5': 'five ',
    '6': 'six ',
    '7': 'seven ',
    '8': 'eight ',
    '9': 'nine ',
    '10': 'ten '
}
phon_num_spl =''

for digit in phone_number:
    phon_num_spl += number_spellings.get(digit)
print(phon_num_spl)

print('End of program')

#symbols tp emojis
msg = input('>')
emoji_dict = {
    ':-)': '😊',
    '<3': '❤️',
    ';-)': '😉',
    ':thumbsup:': '👍',
    ':star:': '⭐',
    ':coffee:': '☕',
    ':hearteyes:': '😍',
    ':sad:': '😢',
    ':smile:': '😄',
    ':fire:': '🔥',
    ':rocket:': '🚀',
    ':pencil:': '✏️',
    ':book:': '📖',
    ':computer:': '💻',
    ':phone:': '📱',
    ':sun:': '☀️',
    ':moon:': '🌙',
}

new_msg = ''
msg_lst= msg.split(' ')
for word in msg_lst:
    new_msg += emoji_dict.get(word,word) + ' '
print(new_msg)

print('End of program')

#Basic CLass structure
import random


class Dice:
    def __init__ (self):
        pass

    def roll (self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice1 = Dice()
print(dice1.roll())
print('End of progam')
