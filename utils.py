import pandas as pd
import os

def json2df(fname):
    try:
        return pd.read_json(fname).transpose()
    except Exception as e:
        raise Exception("Could not open JSON file '%s': %s" % (fname, e))

def csv2df(fname):
    try:
        return pd.read_csv(fname, index_col="id")
    except Exception as e:
        raise Exception("Could not open CSV file '%s': %s" % (fname, e))

def mkdir(path):
    
    """ 
    Make a directory if it doesn't exist
    """

    if not path.endswith("/"):
        path += "/"
        
    dst_dir = os.path.dirname(path)

    if os.path.exists(dst_dir):return 
        
    os.makedirs(dst_dir)
