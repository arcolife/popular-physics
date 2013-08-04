import json

file = open('../data/txt.authors.json','r')
data = json.load(file)
file.close()

file = open('../data/author_citation','r')
data2 = json.load(file)
file.close()

file = open('common.json','w')
common = {}

'''mergers both dictionaries'''
for auth in data2.keys():
    if auth in data.keys():
        common[auth]=[data2[auth],data[auth][0],data[auth][1],data[auth][2]]

'''dumps dictionary as a JSON object into a variable'''
arr = json.dumps(new)

file.write(arr)
file.close()

print "\n\n....output in <data/common.json>\n"
