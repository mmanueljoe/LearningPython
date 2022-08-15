import random


def draw():
    numbers = []
    for x in range(0, 5):
        if len(numbers) < 5:
            numbers.append(random.randint(1, 91))  # this adds the values generated in the int range to the list numbers
    return numbers
    # random.randint(1, 6)


# print(draw())

code = input('Enter Code : ')
if code == '*959#':
    print('(1) Monday Special\n(2) Draw Results')
    option = input('Enter Choice : ')
    if option == '1':  # if option equals 1 then display menu otherwise display Invalid Input
        print('(1) Direct-1\n(2) Two Sure \n(3) Direct-3')
        option = input('Enter Choice : ')
        if option == '1':
            entry = int(input('Enter A Number(1-90) : '))
            if entry in range(1, 91):
                print('You have selected ', entry)
                amount = float(input('Enter the Amount You Wish To Stake(1-200) : '))
                print('Your amount is %.2f' % amount)
                draw = draw()
                if entry in draw:
                    print('You Won ! ', entry, ' is in ', draw)
                else:
                    print('You lost! ', entry, ' is not in ', draw)
            else:
                print('Invalid Input! Enter A Number in the Range 1-90')
    else:
        print('Invalid Input')
else:
    print('Unknown Application')

# You are to check if the number entered by the user is in the drawn numbers.
value = lambda a, b: a + b
print(value(1, 3))

numList = [30, 2, -15, 17, 9, 100]

greater_than_10 = list(filter(lambda n: n > 10, numList))
print(greater_than_10)

