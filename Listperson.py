import httplib, urllib, base64,json ,requests
def list():
	headers = {
    # Request headers
    		'Ocp-Apim-Subscription-Key': '18a4901b9c644cb9b2a743e1b12aaff4',
	}

	params = urllib.urlencode({
	    # Request parameters
    		'start': '0',
    		'top': '1000',
	})
	body = ''

	try:
    		conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
    		conn.request("GET", "/face/v1.0/persongroups/123/persons?%s" % params, body, headers)
    		response = conn.getresponse()
    		data = response.read()
    		parsed = json.loads(data)
    		#print (json.dumps(parsed, sort_keys=True, indent=2))
    		conn.close()
		return parsed
	except Exception as e:
    		print("[Errno {0}] {1}".format(e.errno, e.strerror))
