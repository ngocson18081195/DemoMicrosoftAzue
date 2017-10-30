import httplib, urllib, base64
import Addper
def create(name):
	
	body = "{'userData':'11' ,'name' : '"+name+"'}"
	headers = {
    		'Content-Type': 'application/json',
    		'Ocp-Apim-Subscription-Key': '18a4901b9c644cb9b2a743e1b12aaff4',
	}

	params = urllib.urlencode({
	})

	try:
    		conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
    		conn.request("POST", "/face/v1.0/persongroups/123/persons?%s" % params, body, headers)
    		response = conn.getresponse()
    		data = response.read()
    		conn.close()
		return data
	except Exception as e:
		print("Create Person")
    		print("[Errno {0}] {1}".format(e.errno, e.strerror))
