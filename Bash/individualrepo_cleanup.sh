#!/bin/bash
jfrog_user=
jfrog_pass=
repo=companyname

for i in {25..98} ; do
#  curl -X DELETE -u $jfrog_user:$jfrog_pass $i
curl -X DELETE -u $jfrog_user:$jfrog_pass https://companyname.jfrog.io/artifactory/$repo/api-$i-1.0.0-SNAPSHOT-mule-application.jar
curl -X DELETE -u $jfrog_user:$jfrog_pass https://companyname.jfrog.io/artifactory/api/trash/clean/$repo/api-$i-1.0.0-SNAPSHOT-mule-application.jar
done