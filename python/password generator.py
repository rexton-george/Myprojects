import string
import random

ch = list(string.ascii_letters + string.digits + "@$#%^&*()!")

def pass_gen():
    pass_len = int(input("Enter password length :"))
    random.shuffle(ch)
    pw = []

    for i in range(pass_len):
        pw.append(random.choice(ch))
    random.shuffle(pw)
    print("Your password is:",pw)


op = str(input("Do you want to generate a password (Yes/No) :"))
if(op == "Yes"):
    pass_gen()
elif(op == "No"):
    print("Ok Thank you")