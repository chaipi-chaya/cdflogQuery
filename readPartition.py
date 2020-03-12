import sys,time,os,json,datetime,operator

# SELECT temp_5, temp_8 FROM print_reading WHERE pitime > 2018-05-06 16:00:00 AND pitime < 2018-05-06 18:00:00;
# SELECT AVG(temp_8) FROM print_reading WHERE pitime > 2018-05-05 16:00:00 AND pitime < 2018-05-07 16:00:00;

temp_5data = []
temp_8data = []
temp_8avgdata = []

datetemp1 = datetime.datetime(2018, 5, 6, 16, 00)
datetemp2 = datetime.datetime(2018, 5, 6, 18, 00)
dateavg1 = datetime.datetime(2018, 5, 5, 16, 00)
dateavg2 = datetime.datetime(2018, 5, 7, 16, 00)

starttime = time.time()

for root,dirs, files in os.walk('datalog'):
    # print(root,dirs,files)
    path = root.split(os.sep)
    for fn in files:
        fp = root+os.sep+fn
        f = open(fp, 'r')
        for line in f:
            data = json.loads(line)
            pitime = data['pitime']
            pitimedate = pitime.split('T')[0]
            pitimetime = pitime.split('T')[1].split('.')[0]
            date_str = pitimedate + ' ' + pitimetime
            date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
            if (date > datetemp1) and (date < datetemp2):
                if 'temp_5' in data:
                    temp_5data.append(data['temp_5'])
                if 'temp_8' in data:
                    temp_8data.append(data['temp_8'])
            if (date > dateavg1) and (date < dateavg2):
                if 'temp_8' in data:
                    temp_8avgdata.append(data['temp_8'])
                    
print(time.time()-starttime)

temp_5data = []
temp_8data = []
temp_8avgdata = []

starttime = time.time()

for root,dirs, files in os.walk('partitionPitime'):
    # print(root,dirs,files)
    path = root.split(os.sep)
    for fn in files:
        pitimedate = fn.split('.')[0]
        date = datetime.datetime.strptime(pitimedate, '%Y_%m_%d')
        fp = root+os.sep+fn
        if (date.date() >= datetemp1.date()) and (date.date() <= datetemp2.date()):
            f = open(fp, 'r')
            for line in f:
                data = json.loads(line)
                pitime = data['pitime']
                pitimedate = pitime.split('T')[0]
                pitimetime = pitime.split('T')[1].split('.')[0]
                date_str = pitimedate + ' ' + pitimetime
                indate = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
                if (indate > datetemp1) and (indate < datetemp2):
                    if 'temp_5' in data:
                        temp_5data.append(data['temp_5'])
                    if 'temp_8' in data:
                        temp_8data.append(data['temp_8'])
        if (date.date() >= dateavg1.date()) and (date.date() <= dateavg2.date()):
            f = open(fp, 'r')
            for line in f:
                data = json.loads(line)
                pitime = data['pitime']
                pitimedate = pitime.split('T')[0]
                pitimetime = pitime.split('T')[1].split('.')[0]
                date_str = pitimedate + ' ' + pitimetime
                indate = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
                if (indate > dateavg1) and (indate < dateavg2):
                    if 'temp_8' in data:
                        temp_8avgdata.append(data['temp_8'])
                        
print(time.time()-starttime)