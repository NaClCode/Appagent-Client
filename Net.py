import requests
import os,json,Error

jsonpath = f'{os.path.dirname(__file__)}\Config.json'

def net(neturl:str,payload:dict,headers:dict,method:dict)->dir:
    with open(jsonpath) as url:
        url = json.load(url).get('Server')
    reurl = f'{url.get("url")}/{neturl}'
    try:
        response = requests.request(method, reurl, headers=headers, data=payload)
        return {'code':response.status_code,'body':response.text,'head':response.headers}
    except:
        Error.neterror()