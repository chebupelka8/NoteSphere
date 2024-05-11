from qtharmony.widgets import PushButton, DropDownMenu, DigitalEntry, Entry, RadioButton, CheckBox
from qtharmony.windows import MainWindow
from qtharmony.constructor import Initialization

from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout

import sys


Initialization.init(sys.argv)


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.mainLayout = QVBoxLayout()
        self.firstLayout = QHBoxLayout()
        self.secondLayout = QHBoxLayout()
        self.thirdLayout = QHBoxLayout()

        for i in (self.firstLayout, self.secondLayout, self.thirdLayout):
            self.mainLayout.addLayout(i)

        self.firstLayout.addWidget(PushButton("Button"))
        self.firstLayout.addWidget(DropDownMenu([str(i) * 10 for i in range(10)]))

        self.secondLayout.addWidget(DigitalEntry())
        self.secondLayout.addWidget(Entry())

        self.thirdLayout.addWidget(RadioButton("LOOOOOOOOOOOL!"))
        self.thirdLayout.addWidget(CheckBox("HAHAHAH?"))

        self.setLayout(self.mainLayout)


if __name__ == "__main__":
    window = MainWindow(Window())
    window.run()

    Initialization.exec()
