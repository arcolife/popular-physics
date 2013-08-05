import simplejson as sj
from pprint import pprint
import urllib
import operator

#data = sj.load(urllib.urlopen("http://localhost:9200/record/_search"))
data = sj.load(urllib.urlopen("http://pcuds54.cern.ch:9200/record/inspire/_search"))

print

# <key finder>                                                                                                                                                          
tempD={}
for i in xrange(len(data['hits']['hits'])):
    for j in data['hits']['hits'][i]['_source'].keys():
        if j in tempD.keys():
            tempD[j]+=1
        else:
            tempD[j]=1

temp = sorted(tempD.iteritems(), key=operator.itemgetter(1))

if(raw_input("want to print key presence count for whole data set? (y/n): ")=='y'):
    for i in temp:
        print i
    print
elif(raw_input("want to just print all keys?(y/n): ")=='y'):
    keys=tempD.keys()
    keys.sort()
    print "\n\tKEYS: "
    for i in keys:
        print "\t\t",i
else:
    print "No. of keys present in source code tags dictionary: ",len(tempD.keys())
print

# </keys finder>   
