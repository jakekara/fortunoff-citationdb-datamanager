import os
import json
import pandas as pd
from CitationTable import CitationTable
from utils import mkdir
        
class CitationData:

    """
    A class to wrap load citation data in JSON or CSV format
    """
        
    def __init__(self, folder, ext):
        self.load_folder(folder, ext)
    
    def load_folder(self, folder, ext):
        
        mkpath = lambda fname: os.path.join(folder, fname)
        get_table = lambda fname: CitationTable(mkpath(fname))

        self.__data = {
            "author": get_table("author.%s" % ext),
            "footnote": get_table("footnote.%s" % ext),
            "publication": get_table("publication.%s" % ext),
            "resource": get_table("resource.%s" % ext)
        }

    
    def load_json_folder(self, folder):
        self.load_folder(folder, "json")   
        
    def load_csv_folder(self, folder):
        self.load_folder(folder, "csv")
        
    
    def to_file(self, folder, convert, ext):
        
        if not folder.endswith("/"):
            folder = "%s/" % folder
            
        mkdir(folder)
        
        def save_csv(k):
            dst = os.path.join(folder, "%s.%s" % (k, ext))
            converted = convert(self.__data[k])
            open(dst,"w").write(converted)
                 
        list(map(save_csv, self.get_data().keys()))

        
    def to_jsons(self, folder):
        """ Convert the data to JSON files"""
        self.to_file(folder, lambda x: x.json(), "json")
        #raise Exception("CitationData.to_jsons: Not implemented")
        
        
    def to_csvs(self, folder):
        """ Convert the data to CSV files"""
        self.to_file(folder, lambda x: x.csv(), "csv")
        
    
    def get_data(self):
        try:
            return self.__data
        except:
            raise Exception("No data! use load_csv_folder() or load_json_folder() first")
        
    def validate(self):
        raise Exception("CitationData.validate: Not implemented")