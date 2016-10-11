# -*- coding: utf-8 -*-

import sqlite3
import os
import sys


class DB:
    __schemaPath = os.path.abspath(os.path.join(os.curdir, 'resources/schema.sql'))
    __temp = os.path.abspath(os.path.join(os.curdir, 'temp/webCrawler.db'))

    def __init__(self):
        try:
            self.__con = sqlite3.connect(self.__temp)
            self.__con.text_factory = str
            self.cur = self.__con.cursor()
        except sqlite3.Error:
            print("SQL Error")
            sys.exit(1)

        f = open(self.__schemaPath, 'r').read()
        self.cur.executescript(f)

        self.__con.commit()

    def __del__(self):
        self.__con.close()

    def addUrl(self, url):
        self.cur.execute('INSERT INTO url(url_input) VALUES (?)',
                         [url])
        self.__con.commit()

    def removeUrl(self, url):
        self.cur.execute('DELETE FROM url WHERE url_input=?',
                         [url])
        self.__con.commit()

    def getUrl(self):
        self.cur.execute('SELECT * FROM url')
        return self.cur.fetchall()

    def addSite(self, url, link, content, parentKey=None):
        self.cur.execute('INSERT INTO site(url_input, site_name, content, parent) VALUES (?, ?, ?, ?)',
                         [url, link, content, parentKey])
        self.__con.commit()

    def getSites(self, urlInput):
        self.cur.execute('SELECT site_name FROM site WHERE url_input=?',
                         [urlInput])
        return self.cur.fetchall()

    def getSiteContent(self, urlInput, url):
        self.cur.execute('SELECT content FROM site WHERE site_name=? AND url_input=?',
                         [url, urlInput])
        return self.cur.fetchall()

if __name__ == '__main__':
    db = DB()


