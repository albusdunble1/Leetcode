for x in range(1,21):
    if x == 4 or x == 13:
        word = "UNLUCKY"
    elif x % 2 == 0:
        word = "even"
    elif x % 2 == 1:
        word = "odd"
    
    print(f"{x} is {word}!")
