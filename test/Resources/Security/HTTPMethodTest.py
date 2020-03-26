import requests

verbs = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'TRACE', 'TEST']

for verb in verbs:
    req = requests.request(verb, 'http://automationpractice.com')
    print(verb, req.status_code, req.reason)
    if verb == 'TRACE' and 'TRACE / HTTP/1.1' in req.text:
        print("Possible Cross Site Tracing vulnerability found")



