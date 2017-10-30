import httplib, urllib, base64, json ,requests
import numpy as np
import cv2
from tkFileDialog import askopenfilename
from PIL import Image

subscription_key = '18a4901b9c644cb9b2a743e1b12aaff4'

uri_base = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'
	
headers = {
    	'Content-Type': 'application/octet-stream',
   	'Ocp-Apim-Subscription-Key': subscription_key,
}


params = urllib.urlencode({
    	'returnFaceId': 'true',
    	'returnFaceLandmarks': 'false',
    	'returnFaceAttributes': 'age,gender',
})
body=""
def pathimage(path):
	filename = path	
	#print("###############"+ filename)
	try:
    		
		
		pppp = open(path,'rb')
   		body = pppp.read()
		
    		pppp.close()
		
    		conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
    		conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
    		response = conn.getresponse()
    		data = response.read()
		
    		parsed = json.loads(data) 		
		
    		#print (json.dumps(parsed, sort_keys=True, indent=2))
    		conn.close()
		#print(parsed)
		return parsed
		#for i in parsed:
		#	print(i['faceId'])
		#	return parsed
		
		#return parsed[0]['faceId']
	except Exception as e:  
		print('loi detect')		
		#print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################




