# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets


class UrlAdditionTab(QtWidgets.QWidget):
    def __init__(self, startFunction, parent=None):
        super(UrlAdditionTab, self).__init__(parent)
        self._startFunction = startFunction
        self.__createUi()

    def __createUi(self):
        urlLabel = QtWidgets.QLabel("Urls: ")
        self._urlTable = QtWidgets.QListWidget(self)

        addButton = QtWidgets.QPushButton("Add")
        self._delButton = QtWidgets.QPushButton("Remove")
        self._delButton.setEnabled(False)

        buttonsLayout = QtWidgets.QHBoxLayout()
        buttonsLayout.addWidget(addButton)
        buttonsLayout.addWidget(self._delButton)

        self._startButton = QtWidgets.QPushButton("Start")
        self._startButton.setFixedWidth(50)
        self._startButton.setEnabled(False)

        urlLayout = QtWidgets.QVBoxLayout(self)
        urlLayout.addWidget(urlLabel)
        urlLayout.addWidget(self._urlTable)
        urlLayout.addLayout(buttonsLayout)
        urlLayout.addWidget(self._startButton, alignment=QtCore.Qt.AlignRight)

        addButton.clicked.connect(self.__show)
        self._delButton.clicked.connect(self.__delete)

        self._urlTable.itemClicked.connect(
            lambda: (
                self._startButton.setEnabled(True),
                self._delButton.setEnabled(True)
            )
        )

        self._startButton.clicked.connect(lambda: self._startFunction(self._urlTable.currentItem().text()))

    def __show(self):
        text, ok = QtWidgets.QInputDialog.getText(self, "Input", "Site Url: ", flags=QtCore.Qt.WindowTitleHint)

        if ok and text is not "":
            self._urlTable.addItem(text)

    def __delete(self):
        self._urlTable.takeItem(self._urlTable.currentRow())

        if self._urlTable.currentRow() == -1:
            self._delButton.setEnabled(False)
            self._startButton.setEnabled(False)
