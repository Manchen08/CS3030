#!/bin/bash

fol=$1
st=$2

for myFile in $fol/$st*
do
	if [[ -d $myFile ]]
	then
		echo $myFile "(dir)"
	else
		echo $myFile
	fi
done
exit 0
