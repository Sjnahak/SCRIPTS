#!/usr/bin/python
import requests
import json

BUILDS_NAME = ['qa-app1-api', 'qa-app2-api']
REPO_NAME = ['app1api-dev', 'app2api-dev']
username=''
password=''

for r,b in zip(REPO_NAME, BUILDS_NAME):
        #myResp = requests.get(base_url+'api/search/aql', auth=('username', 'password'),  data=data)
        next_page_url = 'https://comapnyname.jfrog.io/artifactory/api/search/prop?devartifact=snapshot&build.name=%s&repos=%s' % (b, r)
        myResp = requests.get(next_page_url, auth=(username, password))
        json_resp = myResp.json()["results"]
        
        for result in json_resp[:-3]:
            nw = result["uri"]
            print(nw)
        #list_of_dict_uris = json_resp.get("results", [])
        #uri_list = [result.get("uri", "").strip() for result in
        #            list_of_dict_uris[:-1]]