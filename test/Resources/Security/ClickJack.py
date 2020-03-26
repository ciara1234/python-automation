import requests
from ghost import Ghost
import logging
import os

URL = 'http://automationpractice.com'
req = requests.get(URL)
try:
    xframe = req.headers['x-frame-options']
    print('X-FRAME-OPTIONS:', xframe, 'present, clickjacking not likely possible')
except:
    print('X-FRAME-OPTIONS missing')

print('Attempting clickjacking...')

html = '''
<html>
<body>
<div>Click to get rich now:</div>
<iframe src="''' + URL + '''" height='600px' width='800px'></iframe>
</body>
</html>'''

html_filename = 'clickjack.html'
f = open(html_filename, 'w+')
f.write(html)
f.close()

log_filename = 'test.log'
fh = logging.FileHandler(log_filename)
ghost = Ghost(log_level=logging.INFO, log_handler=fh)
page, resources = ghost.open(html_filename)
l = open(log_filename, 'r')

if 'forbidden by X-Frame-Options.' in l.read():
    print('Clickjacking mitigated via X-FRAME-OPTIONS')
else:
    href = ghost.evaluate('document.location.href')[0]
    if html_filename not in href:
        print('Frame busting detected')
    else:
        print('Frame busting not detected, page is likely vulnerable to clickjacking')
l.close()

logging.getLogger('ghost').handlers[0].close()
os.unlink(log_filename)
os.unlink(html_filename)
