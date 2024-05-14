from qtharmony.widgets import PushButton, DropDownMenu, DigitalEntry, Entry, RadioButton, CheckBox
from qtharmony.windows import MainWindow
from qtharmony.constructor import Initialization
from qtharmony.src.core.theme import ThemeManager

from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout

import sys


Initialization.init(sys.argv)
ThemeManager.change_theme("Dark-Default")


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.mainLayout = QHBoxLayout()
        self.mainLayout.addWidget(PushButton("Button"))

        self.setLayout(self.mainLayout)


if __name__ == "__main__":
    window = MainWindow(Window())
    window.run()

    Initialization.exec()
