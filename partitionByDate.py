import sys,time,os,json,datetime,operator

# select * from cddata where date >= 2019-01-01 and date <= 2019-01-02
# append all json string to new file called output.txt

partdir = 'partitioned/'

for root,dirs, files in os.walk('datalog'):
    # print(root,dirs,files)
    path = root.split(os.sep)
    for fn in files:
        fp = root+os.sep+fn
        f = open(fp, 'r')
        for line in f:
            data = json.loads(line)
            payload = data['payload']
            payload = json.loads(payload)
            
            partfn = payload['recieved'].split('T')[0].replace('-','_')
            
            fout = open(partdir + partfn + '.txt', 'a')
            fout.write(json.dumps(payload) + '\n')
            fout.close()
            
        f.close()