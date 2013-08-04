from invenio.invenio_connector import *
from invenio.search_engine import perform_request_search
import sys
import signal
import json

# Starting record
jump = 2301

# Number of articles to consider
# for evaluating keywords
rg = 100

# Authors dictionary
ad = dict()

# Json output file
file = open("../data/txt.authors.json", "w")
# Keywords file
keywords = open("keywords/taxonomy_HEP.txt.step12")

#################################################
# Signal handler for SIG_INT
#################################################
def signal_handler(signal, frame):
	# global to make the variable visible to main
	global run
	run = False
	print "\n\nScheduling exit"
	run = False
	

#################################################
# Output records (auth->coauth) in a JSON file.
# This function parses just a single record
#################################################
def json_out(x):
	# Go through the list of all the authors
	try:	
		for a in x['100__']:
	
			# Coauthors list
			cl = list()	
			# Keyword dictionary		
			kd = dict()
			# Global list
			l = list()
			try:
				author = a["a"][0]
			except:
				continue		
			# If an author is already in the dictionary
			# there no need to consider him again. Just
			# update article counter
			if(author in ad):
				# Update article counter
				ad[author][2]+=1
				continue
			
			ad[author] = l
			l.append(cl)
			l.append(kd)
			l.append(1)
			# Retrieve list of coauthors			
			try:		
				for (count,coauthors) in enumerate(x['700__']):
					cl.append(coauthors["a"][0])
			except Exception,e:
				pass

			# Retrieve keywords
			dict_ka = dict()
	
			# Rank the articles retrieved with respect to
			# the number of citations
			r = cds.search(	ln='en',
							p=author,
							f='author',
							rm='citations',
							rg=1,
							cc='Articles & Preprints',
							c='Articles',
							action_search='Search')

			# Loop over articles
			for (count,record) in enumerate(r):
				keywords.seek(0)
				for keyword in keywords:
					try:
						keyword_stripped = keyword.rstrip("\n")
						if keyword.rstrip("\n") in record["520__"][0]["a"][0].split(" "):
							if keyword_stripped in dict_ka:
								dict_ka[keyword_stripped]+=1
							else:
								dict_ka[keyword_stripped]=1
					except Exception,e:
						pass

			# Order the occurrences	(most frequent to less frequent)
			ordered_ka = reversed(sorted(dict_ka.items(), key=lambda x: x[1]))
		
			# Build the dictionary of keyword->occurrences
			for i in ordered_ka:
				kd[i[0]]=str(i[1])
	except:
		pass		
#################################################
# Main
#################################################

signal.signal(signal.SIGINT, signal_handler)
cds = InvenioConnector("http://pcuds54.cern.ch/")
	
rec_num = 100
BIG_NUM = 1000000

while jump < BIG_NUM:
	try:	
		if run == False:
			break
	except:
		pass
	print "Retrieving from " + str(jump)	
	records = cds.search(	ln='en',
							ot=['001__','100__','700__'],
							rg=rec_num,
							jrec=jump,
							f='author',
							cc='Articles & Preprints',
							c='Articles',
							action_search='Search')
	
	for (count,record) in enumerate(records):
		json_out(record)

	jump+=rec_num

print "jump is " + str(jump) + "\n"
print "Writing JSON...\n"
file.write(json.dumps(ad))
file.close()
sys.exit(0)

#################################################
# Output records in plain format (both on a 
# single column and on multiple columns
#################################################
def plain_out(x,f,f1):
	try:    
		for author in x['100__']:
			f.write(author["a"][0] + ":")
			f1.write(author["a"][0] + "\n")
			for (count,coauthors) in enumerate(x['700__']):
				f.write(coauthors["a"][0] + ":")
				f1.write(coauthors["a"][0] + "\n")
	except:         
		pass
	
	f.write("\n")


