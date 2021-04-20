import os


def search_file(file_name):
    try:
        path = os.path.abspath(file_name)
        file_name = os.path.basename(path)
        f_name_without_extension = file_name.split('.')[0]
        print(path)
        print(f_name_without_extension)
    except FileNotFoundError:
        print("Проверте правильность имени и расширения!")


search_file('test.txt')
