import httplib, urllib, base64, json ,requests
import Listperson
#js = json.load(open('listperson.json'))

def recog(person):
	#print(person)
	parsed = Listperson.list()
	for i in parsed:
	    for j in person:
		if(j['personId'] == i['personId']):
					#print(i['name'])
			return i 	
	#for i in js:
	#	if(person == i['personId']):
	#		return i['name']	
	#		break

