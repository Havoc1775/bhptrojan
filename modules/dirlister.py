import os

def run (**args):
    print ("[*] In drlistermodule.")
    files = os.listdir(".")
    return str(files)