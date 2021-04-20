def comparison_float():
    number = input("Введите число: ")
    try:
        two_numbers = number.split('.')
        if two_numbers[0] == two_numbers[1]:
            print("True")
        else:
            print('False')
    except IndexError:
        print("Целое")


comparison_float()
