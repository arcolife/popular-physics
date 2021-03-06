# browser link [ https://localhost/search?ln=en&p=&ot='001__,100__,700__'&rg=200&action_search=Search ]
# (optional fields) &cc=Articles+%26+Preprints&c=Articles

import json
from invenio.invenio_connector import *
from invenio.search_engine import perform_request_search
#from invenio.dbquery import run_sql as rs

#cds = InvenioConnector("http://cds.cern.ch/")
cds = InvenioConnector("http://localhost/")

#author_dict = {}
#file = open('author_list.json','w')
def display_info(x):
    '''To display a record's metadata'''
    print 'RECORD_ID --> ',x['001__'][0]
    c=1
    print '\nAuthor(s): ',
    for i in x['100__']:
        print ' (',c,')',i['a'][0]
#        author_dict[i['a'][0]]=[x['001__'][0],[],[]]
        c+=1
    try:
        c=1
        print '\nCo-author(s): \n',
        for i in x['700__']:
            print '('+str(c)+')',i['a'][0],
            c+=1
    except:
        pass
    print '\n--------------------\n'

records = cds.search(ln='en',p=raw_input('Enter search term: '),ot=['001__','100__','700__'],rg=int(raw_input("Enter result size: ")),f='author',cc='Articles & Preprints',c='Articles',action_search='Search')

for record in records:
    #print record['001']
    #print 'Author(s): ',record['100__'], records['700__'], '\tPDF full-text link: ',record['8564_']
    display_info(record)
    raw_input()
