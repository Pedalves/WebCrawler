# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore
import sys, threading

from WebCrawler.db import DB
from WebCrawler.webCrawler import WebCrawler

from gui.urlsTab import UrlAdditionTab
from gui.resultTab import ResultTab


class WebCrawlerGui(QtWidgets.QTabWidget):
    updateStatusSignal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(WebCrawlerGui, self).__init__(parent)

        self.db = DB()

        self.updateStatusSignal.connect(self.onUpdateStatus)

        self.resize(400, 500)
        self.setWindowTitle("Web Crawler")

        self.result = ResultTab(self)
        self.urlTab = UrlAdditionTab(self.crawler, self)

        self.addTab(self.urlTab, "Urls")
        self.addTab(self.result, "Result")

    @QtCore.pyqtSlot(str)
    def onUpdateStatus(self, site):
        self.urlTab.progressBar.setVisible(False)
        self.webCrawler.update()
        self.result.updateResult(site)

    def updateStatus(self, site):
        self.updateStatusSignal.emit(site)

    def crawler(self, site):
        self.urlTab.progressBar.setVisible(True)
        self.urlTab.progressBar.setMaximum(0)
        self.urlTab.progressBar.setMinimum(0)
        self.urlTab.progressBar.setValue(0)

        self.webCrawler = WebCrawler(site, self.db, 3, self.updateStatus)

        thr = threading.Thread(target=self.webCrawler.searchThread)
        thr.start()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    t = WebCrawlerGui()
    t.show()
    sys.exit(app.exec_())
