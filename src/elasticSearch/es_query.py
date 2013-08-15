############### keep calm and hack #####################

import simplejson as sj
from pprint import pprint
import urllib
import operator

#instance = "http://localhost:9200/record/"
#instance = "http://pcuds54.cern.ch:9200/record/inspire/"
instance = "http://pcuds54.cern.ch:9200/record/"

try:
    data = sj.load(urllib.urlopen(instance+"_search?fields=authors,standardized_keywords,free_keywords&size="+
                                  int(raw_input('Enter return size: '))+
                                  "&pretty=true"))
except:
    print "\nCheck the address passed OR check if ES instance is up and healthy !"
    quit()

class DictDiffer(object):
    '''To check differences between 2 dictionaries passed. 
    Note: 2nd Object is compared to 1st one
    http://stackoverflow.com/a/1165552
    '''
    def __init__(self, current_dict, past_dict):
        self.current_dict, self.past_dict = current_dict, past_dict
        self.set_current, self.set_past = set(current_dict.keys()), set(past_dict.keys())
        self.intersect = self.set_current.intersection(self.set_past)
    def added(self):
        return self.set_current - self.intersect 
    def removed(self):
        return self.set_past - self.intersect 
    def changed(self):
        return set(o for o in self.intersect if self.past_dict[o] != self.current_dict[o])
    def unchanged(self):
        return set(o for o in self.intersect if self.past_dict[o] == self.current_dict[o])

data_hits = data['hits']['hits']
hits_count = len(data_hits)
auth_kward={}

for i in xrange(hits_count):
    curr_auth_list = hits[i]['authors']               

    try:
        '''to check if author is already present in auth_kward'''
        for auth in curr_auth_list:

            past_kwards = auth_kward[auth]
            curr_kwards = hits[i]['standardized_keywords']

            curr_dict = {auth:curr_kwards}
            past_dict = {auth:past_kwards}
            
            '''
            d = DictDiffer(curr_dict,past_dict)
            new = d.added()
            old = d.unchanged()
            change = d.changed()
            '''

            if len(new) > 0:
                for new_auth in new:
                    auth_kward[new_auth]                    
            '''
            if len(current_author_list)!= 0:
            if current_author_list :
            dict_auth_kwards
            '''
            keyword_freq_for_authors(hits, current_author)
    except:
        pass

def keyword_freq_for_authors(hits,current):
    '''Finds the keyward counts for the JSON results (loaded into a list of Python Dictionaries) '''
    for n in xrange(count):
        for source in hits[i]['fields']:
            for kward in source['standardized_keywords']:                

                for i in xrange(hits_count, data_set):
                    data_set[i]['_source'][key]
    
    
find_keys(data_hits)

temp = sorted(tempD.iteritems(), key=operator.itemgetter(1))

if(raw_input("want to print key presence count for whole data set? (y/n): ")=='y'):
    for i in temp:
        print i

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





import json

print "Hello! In regard to source browser following major keys will be present as csv heads"
print "['loc',\
 'name',\
 'language',\
 'file_name',\
 'sloc',\
 'extname',\
 'version',\
 'content_type',\
 'timestamp',\
 'release',\
 'ctags',\
 'arch',\
 'size']"

print

json_data=open(raw_input('enter file (type: .json) to be converted to csv format: '))

#kindly ignore variable names

data13=json.load(json_data)

json_data.close()

l=[]

for i in xrange(len(data13['hits']['hits'])):
    try:
        l.append(data13['hits']['hits'][i]['_source']['timestamp']+","+data13['hits']['hits'][i]['_source']['name']+","+str(len(data13['hits']['hits'][i]['_source']['ctags']))+","+str(data33['hits']['hits'][i]['_source']['sloc'])+","+str(data13['hits']['hits'][i]['_source']['loc'])+","+str(data13['hits']['hits'][i]['_source']['size'])+","+data13['hits']['hits'][i]['_source']['version']+","+data13['hits']['hits'][i]['_source']['release']+","+data13['hits']['hits'][i]['_source']['arch']+","+data13['hits']['hits'][i]['_source']['extname']+","+data13['hits']['hits'][i]['_source']['content_type']+","+data13['hits']['hits'][i]['_source']['file_name']+","+data13['hits']['hits'][i]['_source']['language'])
    except:
        pass

file = open(raw_input("enter file to save data to: "),'w')

for i in l:
    file.write(i+"\n")

print "csv is ready. Please check the output file.. "

file.close()



'''
=============
In browser >> 
=============

# http://localhost:9200/record/_search?q="Ellis, John R."&fields=authors,co-authors,standardized_keywords,title&pretty=true&size=100
...gives something like : 
{
  "took" : 12,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "failed" : 0
  },
  "hits" : {
    "total" : 98,
    "max_score" : 5.0329213,
    "hits" : [ {
      "_index" : "record",
      "_type" : "inspire",
      "_id" : "96760",
      "_score" : 2.0403414,
      "fields" : {
        "authors" : [ "Ellis, John R." ],
        "title" : "High-Energy Scattering and the Nature of the Hadronic Phase Transition",
        "co-authors" : [ "Savit, Robert" ],
        "standardized_keywords" : [ "FIELD THEORY: CRITICAL PHENOMENA", "HADRON HADRON: INTERACTION", "INTERACTION: HADRON HADRON", "RENORMALIZATION", "POMERON", "DIFFRACTION", "HIGH ENERGY BEHAVIOR: FROISSART BOUND", "SCALING", "REGGE POLES: MULTI-REGGE", "THERMODYNAMICS", "MODEL: FLUID ANALOGY" ]
      }
    },
    {},{},{}, .... {}   ] } }

......So there is no '_source' key in this result. Hence we use data['hits']['hits'][i]['fields'] since selected fields were returned !

--------------------------------------------------------------
==============================================================

# http://localhost:9200/record/_search?q='John'&pretty=true 
...gives something like : 

{
  "took" : 706,
  "timed_out" : false,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "failed" : 0
  },
  "hits" : {
    "total" : 1886,
    "max_score" : 2.0082457,
    "hits" : [ {
      "_index" : "record",
      "_type" : "inspire",
      "_id" : "49902",
      "_score" : 2.0082457, "_source" : {"free_keywords": [], "standardized_keywords": [], "citations": [], "recid": 51674, "title": "Cosmic Radiation", "references": [], "abstract": "", "authors": ["Linsley, John"], "creation_date": "1967", "co-authors": []}
    }, 

    {},{},{}, .... {}   ] } }


.......So there is no particular field, but there are all keys present in this result. Hence we use data['hits']['hits'][i]['_source'] since all fields were returned !

'''
