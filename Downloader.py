import requests
import os
from utils import mkdir

class Downloader:

    def __init__(self, urls):
        self.__data = {}
        for k in ["author", "footnote","publication", "resource"]:
            if k not in urls:
                raise Exception("Missing required url key '%s'" % k)

            self.load_data(k, urls[k])

    def load_data(self, key, url):
        self.__data[key] = requests.get(url).content

    def save_files(self, folder):
        mkdir(folder)
        
        for k in ["author", "footnote","publication", "resource"]:
            open(os.path.join(folder, "%s.csv" % k), "wb").write(self.__data[k])

