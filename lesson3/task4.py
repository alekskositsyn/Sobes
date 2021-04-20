def read_file(path):
    with open(path, 'r', encoding='UTF-8') as r:
        for line in r:
            print(line, end="")


def write_file():
    try:
        with open("new_file.txt", 'r', encoding='UTF-8') as r:
            print("File is exist")

    except FileNotFoundError:
        with open("new_file.txt", 'w', encoding='UTF-8') as w:
            keys = "abcdefg"
            values = range(10)
            list = [el for el in zip(keys, values)]
            for i in list:
                w.write(f'{str(i)}\n')
        read_file(w.name)

write_file()
