import plotly.figure_factory as ff
import statistics
import csv
import pandas as pd
import random

def randomMean(counter):
  dataset1 = []
  df = pd.read_csv("newdata.csv")
  data = df["average"].tolist()
  for i in range(0,counter):
    randomindex1 = random.randint(0,len(data)-1)
    value1 = data[randomindex1]
    dataset1.append(value1)
  
  mean1 = statistics.mean(dataset1)
  return mean1

def showfig(meanList):
  df1 = meanList
  fig1 = ff.create_distplot([df1],["temp"],show_hist=False)
  fig1.show()

def setup():
  meanList = []
  for i in range(0,1000):
    setofmeans = randomMean(100)
    meanList.append(setofmeans)
  
  showfig(meanList)

setup()