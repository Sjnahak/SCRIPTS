#!/usr/bin/python
import requests
import sys
##Login
username ='user'
password = 'user'
team = 'Nextgen'

full_repo_list = []

# Request 100 repositories per page (and only their slugs), and the next page URL
next_page_url = 'https://api.bitbucket.org/2.0/repositories/%s?pagelen=100&fields=next,values.slug,values.is_private' % team

# Keep fetching pages while there's a page to fetch
while next_page_url is not None:
  response = requests.get(next_page_url, auth=(username, password))
  page_json = response.json()

  # Parse repositories from the JSON
  for repo in page_json['values']:
    full_repo_list.append(repo['slug'])
    full_repo_list.append(repo['is_private'])

  # Get the next page URL, if present
  # It will include same query parameters, so no need to append them again
  next_page_url = page_json.get('next', None)
# Result length will be equal to `size` returned on any page
#print ("Result:", len(full_repo_list))

for i in range(len(full_repo_list)):
  restorepoint = sys.stdout
  sys.stdout = open("/home/ec2-user/repo.txt", 'a')
  print full_repo_list[i]
  sys.stdout.close()
  sys.stdout = restorepoint