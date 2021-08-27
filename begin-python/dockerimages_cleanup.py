#!/usr/bin/python
def clean_docker():
    import requests

    base_url = 'https://companyname.jfrog.io/artifactory/'

    headers = {
        'content-type': 'text/plain',
    }
    username = ''
	password = ''
    #Returns Docker Images for all repo
    #data = 'items.find({"name":{"$eq":"manifest.json"},"stat.downloaded":{"$before":"4w"}})'
	
    #Returns Dockerimages for Specific repo and for the required build number
	#Range can taken as user input and passed instead of hard cording
    for x in range(63, 65):
        data = 'items.find({"repo" : "companyname-api-name-dev"},{"name":{"$eq":"manifest.json"}},{"artifact.module.build.name":{"$eq":"%s"}},{"artifact.module.build.number":{"$eq":"%s"}})' % (x)
		#data = 'items.find({"repo" : "reponame"},{"name":{"$eq":"manifest.json"}},{"artifact.module.build.name":{"$eq":"demoname"}},{"artifact.module.build.number":{"$eq":"9"}})'

        myResp = requests.post(base_url+'api/search/aql', auth=('username', 'password'), headers=headers, data=data)
        #for result in myResp.json()["results"]: when eval gives key error
        for result in eval(myResp.text)["results"]:
            artifact_url = base_url+ result['repo'] + '/' + result['path']
			print(artifact_url)
			requests.delete(artifact_url, auth=('username', 'password'))
			build_url = base_url+'api/build/buildname?buildNumbers=%s' % (x)
			print(build_url)
			requests.delete(build_url, auth=('username', 'password'))
			

if __name__ == '__main__':
    clean_docker()