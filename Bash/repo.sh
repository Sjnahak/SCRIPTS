#!/bin/bash
set -ef
username=
password=
name=
for i in $(cat /home/ec2-user/reponame.txt); do
var=`curl -s -u $username:$password "https://api.bitbucket.org/2.0/workspaces/team/search/code?search_query=lineage_watermark.md+repo:$i" | jq -r '.values[].path_matches[].match'`
if [[ $var == "true" ]]
then
    #echo "$i" >> /home/ec2-user/file1.txt
    echo "Watermark file found"
else
    echo "$i" >> /home/ec2-user/file2.txt
fi
done

if [[ -f "/home/ec2-user/file2.txt" && -s "/home/ec2-user/file2.txt" ]]; then
    export repo_count=`cat /home/ec2-user/file2.txt | wc -l`
    echo "${repo_count} Repo(s) without watermark file exists in Lineage Bitbucket."
    cat /home/ec2-user/file2.txt
    curl -X POST -H --silent --data-urlencode "payload={\"text\": \"Scanned Lineage Github for Watermark file, below is the status:\", \"attachments\": [{\"color\": \"danger\", \"thumb_url\": \"https://emojis.slackmojis.com/emojis/images/1534948460/4529/red_card.png?1534948460\", \"text\": \"Identified ${repo_count} repositories without file: Lineage_watermark.md  \n $(cat main_result) \"}]}" ${slackinfo}
else
    echo "All repo(s) have watermark file"
curl -X POST -H --silent --data-urlencode "payload={\"text\": \"Scanned Lineage Github for Watermark file, below is the status:\", \"attachments\": [{\"color\": \"good\", \"thumb_url\": \"http://www.yourvalleynews.co.uk/wp-content/uploads/2016/02/claassifieds_icon.png\", \"text\": \"All repositories have Watermark file :thumbsup:\"}]}" ${slackinfo}
fi







#!/bin/bash

cat repo.txt |  sed 'N;s/\n/ /' | grep False > pub_repos
if [ -s pub_repos ]
then
export public=1
echo public repo exists
cat pub_repos
curl -X POST -H --silent --data-urlencode "payload={\"text\": \"Scanned Lineage Bitbucket to ensure all repo(s) are private, below is the status:\", \"attachments\": [{\"color\": \"danger\", \"thumb_url\": \"https://emojis.slackmojis.com/emojis/images/1534948460/4529/red_card.png?1534948460\", \"text\": \"Below GitHub repo(s) are public:\n $(cat pub_repos) \"}]}" ${slackinfo}
else
export public=0
echo all are safe
curl -X POST -H --silent --data-urlencode "payload={\"text\": \"Scanned Lineage Bitbucket to ensure all repo(s) are private, below is the status:\", \"attachments\": [{\"color\": \"good\", \"text\": \"All repos are Private!!  :thumbsup: \"}]}" ${slackinfo}
fi
