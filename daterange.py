import sys, time, os, json, datetime

for root, dirs, files in os.walk('data'):
    path = root.split(os.sep)
    for fn in files:
        print(root, fn)
