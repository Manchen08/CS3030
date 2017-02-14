#!/bin/bash -

#set -0 nounset
#
#done < /home/student1/repos/CS3030/inClassCode/module5/passwd
infile=$1
ts=`date +%H%M%`
outfile="user.log".$ts

while IFS=: read user pass uid gid fname homedir shell
do
	echo $user $homedir >> $outfile
done < $infile

exit 0
