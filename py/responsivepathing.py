import os

def here(filename):
    return(os.path.normpath(os.path.dirname(os.path.abspath(__file__)) + "/" + filename))

def print():
    return(os.path.dirname(os.path.abspath(__file__)))
