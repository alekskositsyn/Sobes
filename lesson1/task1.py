def multiplication_table(a, b):
    for i in range(1, b+1):
        for n in range(1, b+1):
            c = i * n
            print(f'{i} * {n} = {c}')


multiplication_table(3, 4)
