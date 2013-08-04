import json

file = open('../../records.json','r')
dump=[]
for i in file:
    dump.append(i.split('\n')[0])

print i
print dump[2323]
file.close()
print len(dump)

c = 0
data = {}
final = []
file = open('../data/demo.json','w')
ct = int(raw_input("Enter record count to parse:"))
for i in dump:
    if c < ct:
        i = json.loads(i)
        if (len(i["citations"])+len(i["references"]))>0 and len(i["citations"])!=0:
            i["creation_date"]=i["creation_date"].split("-")[0]
            try:
                author = i['authors'][0]
                print "n\nSuccess\n\n"
                if author in data.keys():

                    temp = [int(i["creation_date"]),len(i["citations"])]
                    data[author]["income"].append(cites)

                    temp = [int(i["creation_date"]),len(i["co-authors"])]
                    data["lifeExpectancy"].append(temp)

                    temp = [int(i["creation_date"]),len(i["references"])]
                    data["population"].append(temp)                    

                    print "\n\nAgain: \n",data
                else:
                    data["name"]=author
                    data["income"]=[[int(i["creation_date"]),len(i["citations"])]]
                    data["lifeExpectancy"]=[[int(i["creation_date"]),len(i["co-authors"])]]
                    data["population"]=[[int(i["creation_date"]),len(i["references"])]]
                    data["region"]= "Sub-Saharan Africa"
                    
                    print "\n\nAgain: \n",data
                final.append(data)
            except:
                pass
    
        print "c=",c
    data={}        
    c+=1

print final[0]

file.write(str(final))
file.close()

print "\n\n..output in <data/demo.json>\n"
