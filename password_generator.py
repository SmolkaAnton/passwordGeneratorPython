#Password Generator
from random import *

def main():
    strength = input("Do you want a strong password, or a weak password: ")
    strength.lower()
    if(strength=="strong"):
        print("Password is: ", password_strong())
    elif(strength=="weak"):
        print("Password is: ", password_weak())
    else:
        print("Invalid input!")

def password_strong():
    password = " "
    return password

def password_weak():
    password = ""
    weak_passwords=["123456","Password","12345678","qwerty","12345","123456789","letmein","1234567","football","iloveyou","admin",
    "welcome","monkey", "abc123", "starwars","123123","dragon","passw0rd","maste","hello","freedom","whatever",
    "qazwsx","trustno1"]
    num = randint(0,24)
    password += weak_passwords[num]
    return password

main()
