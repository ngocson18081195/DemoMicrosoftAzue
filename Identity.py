import httplib, urllib, base64 ,json, time


headers = {
    	'Content-Type': 'application/json',
    	'Ocp-Apim-Subscription-Key': '',
}

params = urllib.urlencode({	
})
lis = []
def Iden(data,groupId,key):
   #for i in data:
	#print(data)
    #for i in data:
	body= {
		"personGroupId": groupId,
     		"faceIds": [str(data)],
     		"maxNumOfCandidatesReturned": 1,
		"confidenceThreshold": 0.5		
	}
	headers['Ocp-Apim-Subscription-Key'] = key
	
	try:
          conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
    	  conn.request("POST", "/face/v1.0/identify?%s" % params, str(body), headers)
       	  response = conn.getresponse()
    	  data = response.read()
	  parsed = json.loads(data)
	  #lis.append(parsed)
	  #print("@@@@@@@@@@@@@@@22",parsed)
	  #print(lis)
	 
	  #return 
	  
    	  conn.close()
	  return  json.loads(data)
	except Exception as e:
    	  print("[Errno {0}] {1}".format(e.errno, e.strerror))
