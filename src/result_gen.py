##################### 
# SEARCH PARAMETERS #
#####################
'''
ln=language ;; ln='' ;; ln = ['','']
rg=size ;; rg=100
cc=collection ;; cc = 'Articles & Preprints' ;; cc = ['','']
c=sub_collection ; c='Articles' ;; c =['','']
p=search_param ;; p='boson' ;; p=['','']
ot=metadata_keys ;; '100__' ;; ot=['001__','100__','700__']
f=fields ;; f='author'
action_search=action_type ;; action_search='Search'
action=action_type;; action='Search'
'''

from invenio.invenio_connector import *
from invenio.search_engine import  perform_request_search
#from invenio.dbquery import run_sql as rs

#cds = InvenioConnector("http://cds.cern.ch/")
cds = InvenioConnector("http://pcuds54.cern.ch/")

kwarg = raw_input("enter a search query: ")

try:
    size = int(raw_input('Specify no. of records: '))
except:
    size = 10

print \
''' \nNote:\tFor ~~CDS~~, Sub-collections are like:\
\n\t "Published Articles" or "Preprint" or \
\n\t or "Theses" or "Reports" or "Progress Reports" \
\n\t or "CERN Notes" or "Committee Documents" \
\n\t and so on....\
\n\t For ~~local-instance of master branch~~ main sub-collections are like:\
\n\t "Articles" or "Drafts" or "Notes" or "Preprints" or\
\n\t "Books" or "Theses" or "Reports"\
\n\t and so on...'''
collection = raw_input("Enter Collection name(s) [if multiple, separate by single whitespace]: ").split()

print \
'''\nNote:   Fields are like "author" or "title" or "abstract" \
\n\t or "year" or "fulltext" or "reference" or "keyword" and so on..'''
field = raw_input("Enter Field name: ")

print '''\nNote:   Metadata Keys are like "100__" or "700__" or "8564_" or "001__" and so on...'''
keys = raw_input("Enter metdata key(s) [if multiple, separate by single whitespace]: ").split()

'''To get a sample record from ID'''
#x = cds.get_record('1555733')

'''To search inside local instance - pcuds54'''
id_records = perform_request_search(p=kwarg,c=collection)

'''To search inside CDS'''
results = cds.search(p=kwarg,ln='en',c=collection,rg=size,f=field,ot=keys)

results = cds.search(p=kward, ln='en',action_search='Search',op1='a',m1='a',p1='',f1='',c='Articles & Preprints',c='',sf='',so='d',rm='',rg=2000,sc=0,of='hb')

count=len(results) # find actual no. of results returned 

'''write results into a file'''
file = open("../data/output","w")
if len(collection)==0:
    collection = 'All'

#file.write("Record ID's found for this search, in local instance on pcuds54 = "+str(id_records)+"\n\n")
file.write("-----------------------------------------------------------------------------------------\n\n")
file.write("Showing "+str(count)+" result(s) found for the collection(s) of type '"+str(collection)+"', for search string: '"+str(kwarg)+"'\n")

for i in xrange(len(results)):
    file.write("\n\n\t\t\t\t=====================================\n\t\t\t\t\t-------- "+str(i+1)+" --------\n\t\t\t\t=====================================\n")
    for j in results[i]:
        file.write("\n"+str(j)+"\n"+str(results[i][j]))

file.close()

print "\n\n....please check the results piped into <data/output> \n"
