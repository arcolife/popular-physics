import json

file = open('../../../records.json','r')
l=[]
for i in file:
    l.append(i.split('\n')[0])

#print i
#print l[2323]
file.close()
#print len(l)
c = 0
data = {}
file = open('../../data/author_citation','w')
limit = int(raw_input("Enter response limit/count: "))

def allot(keys,author):
    if author in keys:
        return True
    else:
        return False

for i in l:
    if c < limit:
        i = json.loads(i)
#        co_auth = i['co-authors']
        auth = i['authors']
        cites = len(i['citations'])
        if len(auth)==1:
            if allot(data.keys(),auth[0])==True:
                data[auth[0]]+=cites
            else:
                data[auth[0]]=cites
        elif len(auth)>1:
            for author in auth:
                if allot(data.keys(),author)==True:
                    data[author]+=cites
                else:
                    data[author]=cites
        else:
            pass
    
    c+=1
    
arr = json.dumps(data)
file.write(arr)
file.close()

print "\n\n..output in <data/author_citation.json>\n"
'''

# Shell command #

curl -XPUT 'http://localhost:9200/record/author/1' -d '{ "author": "Brady, M.Michael" , "free_keywords": [], "co-authors": ["Dedrick, Kent G."], "creation_date": "1962-09", "citations": 0, "references": 0, "papers": 1}'

'''
