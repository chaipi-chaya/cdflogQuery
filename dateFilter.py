import sys,time,os,json,datetime,operator

#SELECT * FROM cddata WHERE Date > 2019-01-01 and Date < 2019-01-02
txtdata = []
for root,dirs, files in os.walk('data'):
    #print(root,dirs,files)
    path = root.split(os.sep)
    for fn in files:
        fp = root+os.sep+fn
        f = open(fp, 'r')
        for line in f:
            data = json.loads(line)
            payload = data['payload']
            payload = json.loads(payload)
            k = payload['received'].split('T')[0]
            date = k.split('-')
            
            if (date[0] == '2019') and (date[1] == '01') and ((date[2] == '01') or (date[2] == '02')):
                txtdata.append(json.dumps(data))
                    
                    
# sorted_dc = sorted(dateCount.items(),key=operator.itemgetter(1),reverse=True)

file = open("datawithin2019-01-01-2019-01-02.txt", "w") 
file.write('') 
file.close() 

file = open("datawithin2019-01-01-2019-01-02.txt", "w") 
for i in txtdata:
    file.write(str(i) + '\n' ) 
file.close() 
                    
                    
            
            
