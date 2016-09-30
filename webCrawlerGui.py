# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore
import sys

from gui.urlsTab import UrlAdditionTab


class WebCrawlerGui(QtWidgets.QTabWidget):

    def __init__(self, parent=None):
        super(WebCrawlerGui, self).__init__(parent)
        self.resize(400, 500)
        self.setWindowTitle("Web Crawler")

        self.addTab(UrlAdditionTab(self.webCrawler), "Urls")

    def webCrawler(self, site):
        print(site)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    t = WebCrawlerGui()
    t.show()
    sys.exit(app.exec_())
