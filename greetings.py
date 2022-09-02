import datetime


def greeting():
    name = input('Hey There!,Kindly Enter Your Name : ')
    a = datetime.datetime.now()
    if a.hour < 12:
        print(f"Good morning! {name}, It's Now", a.time(), 'AM')
    elif 12 <= a.hour < 16:
        print(f"Good Afternoon! {name}, It's Now :", a.time(), 'PM')
    elif 17 <= a.hour < 21:
        print(f"Good Evening! {name}, It's Now :", a.time(), 'PM')


greeting()