import jwt
import hashlib
import os
import requests
import uuid
from urllib.parse import urlencode, unquote

# access_key = os.environ['kIahnghxejJDQxgD4axE7tT57O8VbmNu3VnQgyuo']
# secret_key = os.environ['xiYku0xqJ31AF9mpcN93a7sF3JsmbyoHGKXm7tct']
# server_url = os.environ['UPBIT_OPEN_API_SERVER_URL']

# payload = {
#     'access_key': access_key,
#     'nonce': str(uuid.uuid4()),
# }

# jwt_token = jwt.encode(payload, secret_key)
# authorization = 'Bearer {}'.format(jwt_token)
# headers = {
#   'Authorization': authorization,
# }

# res = requests.get(server_url + '/v1/accounts', params=params, headers=headers)
# res.json()


import jwt   # PyJWT 
import uuid

payload = {
    'access_key': 'kIahnghxejJDQxgD4axE7tT57O8VbmNu3VnQgyuo',
    'nonce': str(uuid.uuid4()),
}

jwt_token = jwt.encode(payload, 'xiYku0xqJ31AF9mpcN93a7sF3JsmbyoHGKXm7tct')
authorization_token = 'Bearer {}'.format(jwt_token)

print(authorization_token)



# res = requests.get("https://api.upbit.com" + '/v1/accounts', params=params, headers=headers)
# res.json()


res = requests.get("https://api.upbit.com/v1/market/all")
print(res)
res.json()
print(res.json())

