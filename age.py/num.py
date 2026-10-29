age=int(input(" please enter your age:"))
if 18 <= age <= 25:
    print("welcome,young adult")
elif age >= 26:
    print("welcome,adult")
elif age <18:
    print("you are underage")
else:
    print("you cant log in")