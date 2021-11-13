import json
import requests
requests.packages.urllib3.disable_warnings()
api_url="https://10.10.20.48/restconf/data/ietf-interfaces:interfaces"
headers={"Accept":"application/yang-data+json",
        "Content-type":"application/yang-data+json"}

basicAuth=("developer","C1sco12345")

try:
    resp = requests.get(api_url,auth=basicAuth, headers=headers, verify=False)
    resp_json= resp.json()
    print(resp)
    print(f'Response formato json: {resp_json}')
    print(json.dumps(resp_json,indent=4))
   
except Exception as e:
    print("Error:",e.__cause__)


