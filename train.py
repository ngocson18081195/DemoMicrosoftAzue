import httplib, urllib, base64
import os,time
import CreatePer,Addper

def change(path):
 	print(path)
	son = os.listdir(path)[0]
	print(son)
	s = CreatePer.create(son)
	print(s)
	for root, dirs, files in os.walk(path,1):
		#for i in files:
		#	a = path+"/"+son+"/"+i
		Addper.add(s,files,son)

	headers = {
    		'Ocp-Apim-Subscription-Key': '18a4901b9c644cb9b2a743e1b12aaff4',
	}

	params = urllib.urlencode({
	})
	body = ''
	try:
    		conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
    		conn.request("POST", "/face/v1.0/persongroups/123/train?%s" % params, body, headers)
    		response = conn.getresponse()
    		data = response.read()
    		print(data)
    		conn.close()
	except Exception as e:
		print("Loi Train")
    		#print("[Errno {0}] {1}".format(e.errno, e.strerror))	
				
			
        		
				
