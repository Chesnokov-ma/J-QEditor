from PyQt6.QtWidgets import QApplication
from JQEditor.main_window import MainWindow
import sys

"""
Класс для работы с обменными интегралами J.
Просмотр/редактирование/создание/масштабирование.
"""

class JQEditor:
    from .main_window import MainWindow

    def __init__(self):
        """
        Инициализация приложения
        """
        self.__app = QApplication(sys.argv)
        self.__window = MainWindow()

    def run(self):
        """
        Запуск приложения
        """
        self.__window.show()
        self.__app.exec()
