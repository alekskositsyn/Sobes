import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QFileDialog
from server_db import ServerStorage
import design


# GUI - Функция реализующая заполнение таблицы Goods.
def create_goods_model(database):
    # Список записей из базы
    hist_list = database.goods_list()
    # Объект модели данных:
    model = QStandardItemModel()
    model.setHorizontalHeaderLabels(
        ['id', 'Имя', 'Категория'])
    for row in hist_list:
        good_id, good_name, good_cat = row
        good_id = QStandardItem(good_id)
        good_id.setEnabled(False)
        good_name = QStandardItem(str(good_name))
        good_name.setEnabled(False)
        good_cat = QStandardItem(str(good_cat))
        good_cat.setEnabled(False)
        model.appendRow([good_id, good_name, good_cat])
    return model


class MainWindow(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.path_db_Button.clicked.connect(self.browse_folder)

    def browse_folder(self):
        dialog = QFileDialog(self)
        path = dialog.getOpenFileName()
        path = path[0].replace('/', '\\')
        self.db_path.insert(path)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.browse_folder()
    path = window.db_path.text()
    database = ServerStorage(path)
    window.tableView.setModel(create_goods_model(database))
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
