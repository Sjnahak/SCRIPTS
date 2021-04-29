#!/bin/bash
jfrog_user=
jfrog_pass=
repo=companyname

for i in {25..98} ; do
#  curl -X DELETE -u $jfrog_user:$jfrog_pass $i
curl -X DELETE -u $jfrog_user:$jfrog_pass https://companyname.jfrog.io/artifactory/$repo/api-$i-1.0.0-SNAPSHOT-mule-application.jar
curl -X DELETE -u $jfrog_user:$jfrog_pass https://companyname.jfrog.io/artifactory/api/trash/clean/$repo/api-$i-1.0.0-SNAPSHOT-mule-application.jar
done

#Search a pattern and delete it
#!/bin/bash
jfrog_user=""
jfrog_pass=""
repo=reponame

for i in {371..373} ; do
patterns=`curl -s -u  $jfrog_user:$jfrog_pass https://companyname.jfrog.io/artifactory/api/search/pattern?pattern=$repo:folder/HtmlReport_apiname_$i*.zip | jq -r '.files[]?'`
echo $patterns
done
#curl -X DELETE -u $jfrog_user:$jfrog_pass https://companyname.jfrog.io/artifactory/$repo/$patterns


###########################################################################################################################################################
#!/bin/bash
CURRENT_TIME=`date +%s%3N`
echo "enter build name?"
read BUILDS_NAME
echo "Enter repo name?"
read REPO_NAME
echo "Enter tag devartifact or qaartifact name?"
read artifact_tag
echo "Enter tag snapshot or qaartifact name?"
read artifact_value
jfrog_user=""
echo "enter jfrog password"
read jfrog_pass
# FETCHING URL DETAIS FOR MATCHING PROPERTY NAME Env property repos, Fetcth Corresponding builds to delete using the usl
untagged_jar=`curl -s -u $jfrog_user:$jfrog_pass "https://comapnyname.jfrog.io/artifactory/api/search/prop?$artifact_tag=$artifact_value&repos=$REPO_NAME" | jq -r '.results[]?.uri'`
#untagged_jar=`curl -s -u $jfrog_user:$jfrog_pass "https://companyname.jfrog.io/artifactory/api/search/prop?env=dev&repos=companyname-api-dev" | jq -r '.results[]?.uri'| head -n -3`

for build in $BUILDS_NAME ; do
   if [ -z "$untagged_jar" ]
   then
      echo "#####NO Snapshot BUILD FOUND FOR $build NOTHING TO DELETE HENCE MOVING TO NEXT REPO#####"
   else
      for build_info in $untagged_jar; do
        snapshot_build=`curl -s -u $jfrog_user:$jfrog_pass $build_info?properties=build.number  | jq -r '.properties[]?[]'`
        echo "#####SNAPHOT BUILD NUMBER FOUND FOR $build HENCE PROCEEDING WITH DELETE LOOP#####"
        echo "Your build number : $snapshot_build"
        PATH_TO_ARTIFACT=`curl -s -X GET -u $jfrog_user:$jfrog_pass $build_info | jq -r '.downloadUri'`
        echo $PATH_TO_ARTIFACT
        #curl -X DELETE -u $jfrog_user:$jfrog_pass "https://comapnyname.jfrog.io/artifactory/api/build/$build?buildNumbers=$snapshot_build"
        #curl -X DELETE -u $jfrog_user:$jfrog_pass "$PATH_TO_ARTIFACT"
      done
    fi
done

#head -n -1   removes 1 line from bottom
#tail -n +2   removes 1 line lesser than the provided number from top(example if given 2 it will remove 1)