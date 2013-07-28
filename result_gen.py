from invenio.invenio_connector import *
from invenio.search_engine import  perform_request_search

cds = InvenioConnector("http://cds.cern.ch")
kwarg = raw_input("enter a search query: ")

'''To search inside local instance - pcuds54'''
rec_id_arr = perform_request_search(p=kwarg,c=[""])

'''To search inside CDS'''
results = cds.search(kwarg)

'''write results into a file'''
file = open("10_def_op","w")

file.write("Record ID's found for this search, in local instance on pcuds54 = "+str(rec_id_arr)+"\n\n")
file.write("-----------------------------------------------------------------------------------------\n\n")
file.write("First 10 results from CDS, for search string: '"+kwarg+"'\n")

for i in xrange(len(results)):
    file.write("\n\n\t\t================================================================================\n\t\t\t\t\t\t-------- "+str(i+1)+" --------\n\t\t================================================================================\n")
    for j in results[i]:
        file.write("\n"+str(j)+"\n"+str(results[i][j]))

file.close()

print "\n\n....please check the results piped into ./10_def_op \n"
