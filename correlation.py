import csv
import pandas as pd 
import plotly.express as px
import numpy as np

def getdatasource(datapath):
    Marks=[]
    Days=[]
    with open(datapath)as f:
        df=csv.DictReader(f)
        for row in df:
            Marks.append(float(row["Marks In Percentage"]))
            Days.append(float(row["Days Present"]))
    return {"x":Marks,"y":Days}


def findcorrelation(datasrc):
    correlation=np.corrcoef(datasrc["x"],datasrc["y"])
    print("correlation is :-\n---->",correlation[0,1])

def setup():
    datapath='./CoRelation/Student Marks vs Days Present.csv'
    datasrc=getdatasource(datapath)
    findcorrelation(datasrc)

setup()