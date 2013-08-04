import json
import pexpect

file = open('../../data/esReady_no_abstr.json','r')

#demo =  '{ "authors": "Brady, M.Michael" , "free_keywords": [], "co-authors": ["Dedrick, Kent G."], "creation_date": "1962-09", "citations": 0, "references": 0, "papers": 1}'

#print '\nDATA \n', data[data.keys()[0]]
c=1
for i in file:
    query = "curl -XPUT 'http://localhost:9200/record/inspire/"+str(c)+"' -d '"+i.split("\n")[0]+"'"
    print "\nQUERY: ",query
    result = pexpect.run(query)
    print "\nRESPONSE: \n",result,"\n"
    print "\n===============================\n"
    c+=1

#print curl_query

file.close()


'''
# Shell command #

curl -XPUT 'http://localhost:9200/record/author/1' -d '{ "authors": "Brady, M.Michael" , "free_keywords": [], "co-authors": ["Dedrick, Kent G."], "creation_date": "1962-09", "citations": 0, "references": 0, "papers": 1}'

'''
