import json
import pexpect

file = open('../../../records.json','r')

#demo =  '{ "authors": "Brady, M.Michael" , "free_keywords": [], "co-authors": ["Dedrick, Kent G."], "creation_date": "1962-09", "citations": 0, "references": 0, "papers": 1}'

#print '\nDATA \n', data[data.keys()[0]]
c=1
for i in file:
    query = "curl -XPUT 'http://localhost:9200/record/inspire/"+str(c)+"' -d '"+str(i.split("\n")[0])+"'"
#    print "\nQUERY: ",query
    result = pexpect.run(query)
    print "\n",c," >> RESPONSE: ",result," <<"
#    print c,">"
    c+=1

#print curl_query

file.close()


'''
# Shell command #

curl -XPUT 'http://localhost:9200/record/author/1' -d '{ "authors": "Brady, M.Michael" , "free_keywords": [], "co-authors": ["Dedrick, Kent G."], "creation_date": "1962-09", "citations": 0, "references": 0, "papers": 1}'


curl --max-time  6600 --connect-timeout 6000 http://localhost:9200/record/_search -d '
{"query":{"bool":{"must":[{"query_string":{"default_field":"_all","query":" Ellis, P J "}}],"must_not":[],"should":[]}},"from":0,"size":500,"sort":[],"facets":{}}'

'''
