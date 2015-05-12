# -*- coding: utf8 -*-

from traceback import format_exc

from base_tools import log
from base_tools import read_lines
            
            

def gen_name_dict_dup(fromPath, toPath, dataSegIndices, seperator='\t', limit=None):
    if limit:
        lineCnt = limit
    with open(toPath, 'a') as toFile:
        with open(fromPath, 'r') as fromFile:
            for l in fromFile:
                l = l.strip()
                e = l.split(seperator)
                if limit:
                    lineCnt -= 1
                    print "line:%s" % lineCnt
                    if not lineCnt:
                        return
                try:
                    toFile.write('\n'.join([e[i] for i in dataSegIndices]))
                    toFile.write('\n')
                except:
                    continue
                
                
def gen_name_dict(fromPath, toPath, dataSegIndices, seperator='\t', limit=None):
    if limit:
        lineCnt = limit
    wordSet = set()
    with open(fromPath, 'r') as fromFile:
        for l in fromFile:
            try:
                l = l.strip()
                e = l.split(seperator)

                if limit:
                    lineCnt -= 1
                    if not lineCnt:
                        break
                wordSet.update([e[i] for i in dataSegIndices])
                    
            except:
                print format_exc()
                continue
    print wordSet        
    with open(toPath, 'a') as toFile:
        toFile.write('\n'.join(wordSet))


def line_unique(fromPath, toPath):
    lineSet = set()
    for l in read_lines(fromPath):
        lineSet.add(l)
    with open(toPath, 'w') as t:
        t.write('\n'.join(lineSet))