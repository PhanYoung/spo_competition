# -*- coding: utf-8 -*-
from base_tools import read_lines
from collections import defaultdict
P_List = []

infoPool = defaultdict(lambda: {})

def pool_data(infoDict, dataList):
    for i in range(len(dataList), step=2):
        infoDict[i] = infoDict

def read_infos(filePath, seperator):
    for l in read_lines(filePath):
        e = l.split(seperator)
        

class PosInfo(object):
    def __init__(self):
        #self.orderP = 0  #1,pre   2,mid   3,post
        self.distToS = 0
        self.distToO = 0



def P_pos(sentense, S, O):
    try:
        posS = sentense.index(S)
        posO = sentense.index(O)
    except:
        Log("Can't find %s or %s in %s" % (S, O, sentense))
        
    for P in P_List:
        try:
            posP = sentense.index(P)
            pi = PosInfo()
            pi.distToS = posP - posS
            pi.distToO = posO - posS
        except:
            continue

            