import httplib, urllib, base64, json

subscription_key = '18a4901b9c644cb9b2a743e1b12aaff4'

uri_base = 'westcentralus.api.cognitive.microsoft.com'

# Request headers.
headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

# Request parameters.
params = urllib.urlencode({
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile',
})
body = "{'url':'https://scontent.fsgn5-2.fna.fbcdn.net/v/t34.0-12/22782136_1611570428989537_2139285987_n.jpg?oh=92ef68e6e438c0d6b74231becaebd099&oe=59F18D79'}"
try:
    # Execute the REST API call and get the response.
    conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
    conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()

    # 'data' contains the JSON data. The following formats the JSON data for display.
    parsed = json.loads(data)
    print(parsed[0]['faceRectangle']['width'])
    #print ("Response:")
    print (json.dumps(parsed, sort_keys=True, indent=2))
    conn.close()
    
    
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
