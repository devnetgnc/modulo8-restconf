import json
import requests
requests.packages.urllib3.disable_warnings()
api_url="https://10.10.20.48/restconf/data/ietf-interfaces:interfaces/interface=Loopback2"
headers={"Accept":"application/yang-data+json",
        "Content-type":"application/yang-data+json"}

basicAuth=("developer","C1sco12345")

yangConfig=  {
    "ietf-interfaces:interface": {
    "name": "Loopback2",
    "description": "My Second RESTCONF loopback",
    "type": "iana-if-type:softwareLoopback",
    "enabled": True,
    "ietf-ip:ipv4": {
        "address": [
                    {
                    "ip": "10.2.1.1",
                    "netmask": "255.255.255.0"
                    }
                    ]
    },
        "ietf-ip:ipv6": {}
    }
    }




try:
    resp = requests.put(api_url,auth=basicAuth, headers=headers,data= json.dumps(yangConfig), verify=False)
    if resp.status_code >= 200 and resp.status_code <=299:
        print("STATUS OK: {}".format(resp.status_code))
    else:
        print('Error. Status code: {} \n Error message: {}'.format(resp.status_code,resp.json)) 

 
except Exception as e:
    print("Error:",e.__cause__)


