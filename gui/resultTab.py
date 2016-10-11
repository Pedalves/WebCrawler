# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets


class ResultTab(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ResultTab, self).__init__(parent)

        self.mainGui = parent
        self.currentUrl = ''
        self.__createUi()

    def __createUi(self):
        self.urlLabel = QtWidgets.QLabel('Result: ')
        self.urlTable = QtWidgets.QListWidget(self)

        self.contentLabel = QtWidgets.QLabel('Content: ')
        self.contentTable = QtWidgets.QTextEdit(self)
        self.contentTable.setReadOnly(True)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.urlLabel)
        layout.addWidget(self.urlTable)
        layout.addWidget(self.contentLabel)
        layout.addWidget(self.contentTable)

        self.urlTable.itemClicked.connect(self.updateContent)

    def updateResult(self, urlInput):
        self.currentUrl = urlInput
        self.urlLabel.setText('Result:\n' + '"' + urlInput + '"')
        for site in self.mainGui.db.getSites(urlInput):
            self.urlTable.addItem(site[0])

    def updateContent(self, item):
        self.contentTable.setText(self.mainGui.db.getSiteContent(self.currentUrl, item.text())[0][0].replace('\n', ''))
