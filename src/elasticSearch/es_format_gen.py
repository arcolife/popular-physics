import json

file = open('../../../records.json','r')
l=[]
for i in file:
    l.append(i.split('\n')[0])

print i
print l[2323]
file.close()
print len(l)
c = 0
data = {}
file = open('../../data/esReady_no_abstr.json','w')
limit = int(raw_input("Enter response limit/count: "))

for i in l:
    if c < limit:
        i = json.loads(i)
        try:
            if i['authors'][0] in data.keys():
		for key in data[i['authors']].keys():
                    if key=='papers':
                        data[key]+=1
                    elif key=='citations' or key=='references':
                        data[key]+=len(i[key])
                    else:
                        data[key].append(i[key])
                    
            else:
		data[i['authors'][0]]={"co-authors":i['co-authors'],"free_keywords":i['free_keywords'],"citations":len(i['citations']), "references":len(i['references']),"creation_date":i['creation_date'], "papers":1,"recid":i['recid']}
            print "c=",c
        except:
          pass
        
    c+=1
    
arr = json.dumps(data)
file.write(arr)
file.close()

print "\n\n..output in <data/esReady_no_abstr.json>\n"

'''

# Shell command #

curl -XPUT 'http://localhost:9200/record/author/1' -d '{ "author": "Brady, M.Michael" , "free_keywords": [], "co-authors": ["Dedrick, Kent G."], "creation_date": "1962-09", "citations": 0, "references": 0, "papers": 1}'

'''
