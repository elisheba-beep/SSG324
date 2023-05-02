for number in range(1, 61):
    if number%3 == 0 and number%4 == 0:
        print("Multiple of 3 and 4")
    elif number%3 == 0:
        print("Multiple of 3")
    elif number%4 == 0:
        print("Multiple of 4")
    else:
        print(number)