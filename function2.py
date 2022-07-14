name = input("Enter Your Name:")
age = int(input("Enter Your Age:"))
year = 2022
def getage():
    return year - age

print("Hello," + name + ". You were born in the year", getage())
