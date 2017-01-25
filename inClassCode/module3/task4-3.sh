#!/bin/bash - 
#===============================================================================
#
#          FILE: task4-3.sh
# 
#         USAGE: ./task4-3.sh 
# 
#   DESCRIPTION: 
# 
#         NOTES: ---
#        AUTHOR: Jon Wheeler (), jonathanwheeler1@weber.edu
#       CREATED: 01/24/2017 19:05
#      REVISION:  ---
#===============================================================================

#set -o nounset                              # Treat unset variables as an error

ts=`date +%Y-%m-%d_%H:%M`
suffix="BACKUP--$ts"
bk="backup"

# Test for bk directory
if [[ ! -d $bk ]]
then
	mkdir $bk
fi

for script in *.txt
do
	echo " Copy $script to $bk/$script.$suffix"
	#make the cp command
	cp $script $bk/$script.$suffix
done

exit 0

