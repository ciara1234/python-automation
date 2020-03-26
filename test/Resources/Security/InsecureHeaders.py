import requests

urls = open("urls.txt", "r")
for url in urls :
    url = url.strip()
    req = requests.get(url)
    print(url, 'report:')
    try :
        xssprotect = req.headers['X-XSS-Protection']
        if xssprotect != '1; mode=block' :
            print('X-XSS-Protection not set properly, XSS may be possible:', xssprotect)
    except :
        print('X-XSS-Protection not set, XSS may be possible')

    try :
        contenttype = req.headers['X-Content-Type-Options']
        if contenttype != 'nosniff' :
            print('X-Content-Type-Options not set properly:', contenttype)
    except :
        print('X-Content-Type-Options not set')

    try :
        hsts = req.headers['Strict-Transport-Security']

    except :
        print('HSTS header not set, MITM attacks may be possible')

    try :
        csp = req.headers['Content-Security-Policy']
        print('Content-Security-Policy set:', csp)
    except :
        print('Content-Security-Policy missing')
        print('----')
