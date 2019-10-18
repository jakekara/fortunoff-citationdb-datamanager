from utils import json2df, csv2df

class CitationTable:
    
    """
        A class to import and export folders containing CitationDB
        data in CSV or JSON format and convert from one format to
        the other.
    """
    
    def __init__(self, fname):

        if (fname.lower().endswith(".json")):
            self.load_json(fname)
        elif (fname.lower().endswith(".csv")):
            self.load_csv(fname)
        else:
            raise Exception("Invalid file extension. Must be 'json' or 'csv'")
        self.__fname = fname;
            
    def set_data(self, data):
        self.__data = data
    
    def get_data(self):
        return self.__data.copy()
    
    def load_json(self, fname):
        self.set_data(json2df(fname))
        
    def load_csv(self, fname):
        self.set_data(csv2df(fname))
        
    def as_dict(self):
        return self.get_data().as_dict(orient="index")
        
    def json(self):
        try:
            return self.get_data().to_json(orient="index")
        except Exception as e:
            raise Exception("Error converting file '%s' to JSON: %s" % (self.__fname, e))
    
    def csv(self):
        try:
            return self.get_data().to_csv(index_label="id")
        except Exception as e:
            raise Exception("Error converting file '%s' to CSV: %s" % (self.__fname, e))
    
    def to_csv_file(self, fname):
        open(fname,"w").write(self.csv())
        
    def to_json_file(self, fname):
        open(fname,"w").write(self.json())