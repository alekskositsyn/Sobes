import re


def read_file(path):
    with open(path, 'r+', encoding='UTF-8') as r:
        pattern = 'example1'
        pattern2 = '\s\w+\s'
        must_changed = 'example2'
        changed_to = ' changed '
        for line in r:
            r.write(re.sub(must_changed, changed_to, line))
            if re.match(pattern, line):
                print(line)
            if re.findall(pattern, line):
                print(line)
            if re.findall(pattern2, line):
                print(line)


def write_file():
    try:
        with open("new_file.txt", 'r', encoding='UTF-8') as r:
            print("File is exist")

    except FileNotFoundError:
        with open("new_file.txt", 'w', encoding='UTF-8') as w:
            keys = ['example', 'example', 'example', 'example', 'example']
            values = [1, 2, 3, 4, 5, 9]
            list = [el + str(v) for el in keys for v in values]
            for i in list:
                w.write(f'{str(i)} \n')
        read_file(w.name)


write_file()
