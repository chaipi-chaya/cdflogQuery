import sys,time,os,json,datetime,operator

# select * from cddata where date >= 2019-01-01 and date <= 2019-01-02
# append all json string to new file called output.txt

partdir = 'partitionPitime/'
buf = ''
lastpartfn = ''
n = 0
for root,dirs, files in os.walk('datalog'):
    # print(root,dirs,files)
    path = root.split(os.sep)
    for fn in files:
        fp = root+os.sep+fn
        f = open(fp, 'r')
        for line in f:
            data = json.loads(line)
            pitime = data['pitime']
            partfn = pitime.split('T')[0].replace('-','_')
            buf += json.dumps(data) + '\n'
            
            if n % 500 == 0 or partfn != lastpartfn:
                fout = open(partdir + partfn + '.txt', 'a')
                fout.write(buf)
                fout.close()
                buf = ''
                
            n += 1
            lastpitime = pitime
        fout = open(partdir + partfn + '.txt', 'a')
        fout.write(buf)
        fout.close()
        buf = ''
        
        f.close()