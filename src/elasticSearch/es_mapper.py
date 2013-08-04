import json
import pexpect

file = open('../../data/esReady_no_abstr.json','r')
data = json.load(file)
demo =  '{ "author": "Brady, M.Michael" , "free_keywords": [], "co-authors": ["Dedrick, Kent G."], "creation_date": "1962-09", "citations": 0, "references": 0, "papers": 1}'

print '\nDATA \n', data[data.keys()[0]]
c=1
curl_query = "curl -XPUT 'http://localhost:9200/record/author/"+str(c)+"' -d '"+demo+"'"

#for key in data.keys():
    

#print curl_query
result = pexpect.run(curl_query)
print "\nRESPONSE: \n",result,"\n"
file.close()


'''
# Shell command #

curl -XPUT 'http://localhost:9200/record/author/1' -d '{ "author": "Brady, M.Michael" , "free_keywords": [], "co-authors": ["Dedrick, Kent G."], "creation_date": "1962-09", "citations": 0, "references": 0, "papers": 1}'

'''
