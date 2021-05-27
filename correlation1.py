import csv
import pandas as pd 
import plotly.express as px
import numpy as np

def getdatasource(datapath):
    Size=[]
    watchingTV=[]
    with open(datapath)as f:
        df=csv.DictReader(f)
        for row in df:
            Size.append(float(row["Size of TV"]))
            watchingTV.append(float(row["Average time spent watching TV in a week"]))
    return {"x":Size,"y":watchingTV}


def findcorrelation(datasrc):
    correlation=np.corrcoef(datasrc["x"],datasrc["y"])
    print("correlation is :-\n---->",correlation[0,1])

def setup():
    datapath='./CoRelation/Size of TV,_Average time spent watching TV in a week (hours).csv'
    datasrc=getdatasource(datapath)
    findcorrelation(datasrc)

setup()