#!/bin/bash
START_DATE=1514745000000
CURRENT_TIME=`date +%s%3N`
BUILDS_NAME="buildname"
REPO_NAME="reponame"
jfrog_user=username
jfrog_pass=password

for ARTIFACT in $REPO_NAME ;do
old_artifact=`curl -s -X GET -u $jfrog_user:$jfrog_pass "https://test.jfrog.io/artifactory/api/search/creation?from=$START_DATE&to=$CURRENT_TIME&repos=$ARTIFACT" | jq -r '.results[]?.uri'| head -n -5`
   # REMOVING /api/stoarge from the url
   # IF Artifact is null else
   if [ -z "$old_artifact" ]
   then
      echo "******NO OLD ARTIFACT FOUND FOR CORRESPONDING API $ARTIFACT NOTHING TO DELETE MOVING TO NEXT CALL******"
   else
      echo "******OLD BUILD ARTIFACT FOUND FOR CORRESPONDING API $ARTIFACT PROCEEDING WITH THE DELETE LOOP******"
      for ARTIFACT_PATH2 in $old_artifact ; do
        corresponding_buildnum=`curl -s -u $jfrog_user:$jfrog_pass $ARTIFACT_PATH2?properties=build.number  | jq -r '.properties[]?[]'`
        echo "$corresponding_buildnum"
        #echo "FETCHINH THE PATH FOR ARTIFACT TO DELETE $ARTIFACT_PATH2"
        PATH_TO_ARTIFACT2=`curl -s -X GET -u $jfrog_user:$jfrog_pass $ARTIFACT_PATH2 | jq -r '.downloadUri' `
        echo "DELETING CORRESPONDING ARTIFACT $PATH_TO_ARTIFACT2"
        #deleting the corresponding artifact at last
        #curl -X DELETE -u $jfrog_user:$jfrog_pass $PATH_TO_FILE
        #curl -X DELETE -u $jfrog_user:$jfrog_pass "https://test.jfrog.io/artifactory/api/build/$RESULT?buildNumbers=$corresponding_buildnum"
      done
   fi
done
