import requests
import random
import json
#P_W_7
dd = '1234567890'
def dw():
 while True:
  re="".join(random.choice(dd)for i in range(6))
  url = f'http://i.instagram.com/api/v1/users/{re}/info/'
  headers = {

'Host': 'i.instagram.com',
'Connection': 'Keep-Alive',
'User-Agent': 'Instagram 6.12.1 Android (30/11; 480dpi; 1080x2298; HONOR; ANY-LX2; HNANY-Q1; qcom; en_IQ)',
'Accept-Language': 'en-IQ, en-US',
'X-IG-Connection-Type': 'MOBILE(LTE)',
'X-IG-Capabilities': 'AQ==',
'Accept-Encoding': 'gzip',
}

  rr = requests.get(url,headers=headers).text
  if 'User not found' in rr:
   print(f' Bad ID : {re}')
   dw()
  else:
   rre=json.loads(rr)
   user = rre['user']['username']
   print(f' God ID : @{user}')
  
dw()
