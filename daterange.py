import sys, time, os, json, datetime

for root, dirs, files in os.walk('data'):
    path = root.split(os.sep)
    for fn in files:
        fp = root + os.sep + fn
        f = open(fp, 'r')
        for line in f:
            data = json.load(line)
            
