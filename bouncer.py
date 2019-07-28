print("How old are you?")
age = input()

if not age:
    print("You trollin bro?")
else:
    age = int(age)



    if age >= 18 and age < 21:
        print("Wristband")
    elif age >= 21:
        print("Drink, normal entry")
    else:
        print("Too young, sorry...")
