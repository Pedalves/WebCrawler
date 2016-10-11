# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests


class WebCrawler:
    def __init__(self, url, db, maxPages, callback=None):
        self.max = maxPages

        self.count = []
        self.links = []
        self.linksToUpdate = []

        self.inputUrl = url

        self.__db = db

        self.callback = callback

    def searchThread(self):
        self.search(self.inputUrl)
        self.callback(self.inputUrl)

    def search(self, url, parent=None):
        try:
            request = requests.get(url)
        except:
            return
        print("Url: " + url)
        if parent is not None:
            if parent not in self.count:
                self.count.append(parent)
        soup = BeautifulSoup(request.text, 'html.parser')
        self.linksToUpdate.append([self.inputUrl, url, soup.get_text(), parent])
        if self.max >= len(self.count):
            for a in soup.findAll('a', href=True):
                link = a['href']
                if link not in self.links:
                    self.links.append(link)
                    self.search(link)

    def update(self):
        for item in self.linksToUpdate:
            self.__db.addSite(item[0], item[1], item[2], item[3])
