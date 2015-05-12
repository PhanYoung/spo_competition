# -*- coding: utf-8 -*-

def log(err):
    print err
    
def read_lines(filePath):
    with open(filePath) as f:
        for l in f:
            yield l.strip()