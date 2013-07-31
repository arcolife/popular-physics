from invenio.invenio_connector import *
from invenio.search_engine import  perform_request_search
#from invenio.dbquery import run_sql as rs

cds = InvenioConnector("http://cds.cern.ch/")
#cds = InvenioConnector("http://pcuds54.cern.ch/")

kwarg = raw_input("enter a search query: ")
size = int(raw_input('Specify no. of records: '))

print '''\nNote: Collections are like "Published Articles" or "Preprint" or "Articles & Preprints" or "Theses" or "Reports" or "Progress Reports" or "CERN Notes" or "Committee Documents" or "Multimedia & Outreach" and so on....\n'''
collection = raw_input("Enter Collection name: ")


    
'''To get a sample record from ID'''
#x = cds.get_record('1555733')

'''To search inside local instance - pcuds54'''
id_records = perform_request_search(p=kwarg,c=collection)

'''To search inside CDS'''
results = cds.search(p=kwarg,rg=size,ln='en',c=collection)
count=len(results)

'''write results into a file'''
file = open("output","w")
if len(collection)==0:
    collection = 'All'

file.write("Record ID's found for this search, in local instance on pcuds54 = "+str(id_records)+"\n\n")
file.write("-----------------------------------------------------------------------------------------\n\n")
file.write("Showing "+str(count)+" result(s) found in CDS, for the collection(s) of type '"+collection+"', for search string: '"+kwarg+"'\n")

for i in xrange(len(results)):
    file.write("\n\n\t\t================================================================================\n\t\t\t\t\t\t-------- "+str(i+1)+" --------\n\t\t================================================================================\n")
    for j in results[i]:
        file.write("\n"+str(j)+"\n"+str(results[i][j]))

file.close()

print "\n\n....please check the results piped into ./10_def_op \n"
