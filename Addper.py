import httplib, urllib, base64,json, time,requests

from PIL import Image

headers = {
   		 # Request headers
    	'Content-Type': 'application/octet-stream',
   	'Ocp-Apim-Subscription-Key': '18a4901b9c644cb9b2a743e1b12aaff4',
}

params = urllib.urlencode({
   		 # Request parameters
})

def add(data,path,son):
	a = json.loads(data)['personId']
	print("@@@@@@@@@@@@@",a)
	print(path)
	print("&&&&&&&&&&&&",son)
	for i in path:
		#print("/home/ngocson/Pictures/Face_Cognitive/Son"+i)
		filename = "/home/ngocson/Pictures/Face_Cognitive/{0}/{1}".format(son,i)
		
		personGroupId = '123'
		try:
			 conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
			 fi = open(filename,'rb')
			 
			 body = fi.read()
			
    		         fi.close()
    	  		 conn.request("POST", "/face/v1.0/persongroups/{0}/persons/{1}/persistedFaces?{2}".format(personGroupId, a, params), body, headers)
     		 	 response = conn.getresponse()
   		 	 data = response.read()
    			 print(data)
    		 	 conn.close()
		except Exception as e:
		   	 print("error")	
    		time.sleep(5)	
		
