#! bin/bash

read username
currentuser="$(whoami")
if [ $username == $currentuser ]; then
echo "you are the current logged in user"
else
echo "you are not logged in"
fi

