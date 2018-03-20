#!/usr/bin/python
import datetime
import sys
import argparse

def getCount(inptime):
    count=0
    inptime=datetime.datetime.strptime(inptime,'%H:%M:%S')
    with open('input_calcp.txt','r') as f:
        for line in f:
            intime,extime=(datetime.datetime.strptime(x,'%H:%M:%S') for x in line.split())
            #print("input time is {0} and exittime is {1}".format(intime,extime))
            if inptime >= intime and inptime <= extime:
                count += 1
    return count

ap=argparse.ArgumentParser(description='Get the time during which the empolyee count is required')
ap.add_argument('-p','--persons',dest='persons')
ap.add_argument('-t','--time',dest='timestamp',required=True)
results=ap.parse_args()
pers=getCount(results.timestamp)
print("The total no. of persons present during {0} are: {1}".format(results.timestamp,pers))
