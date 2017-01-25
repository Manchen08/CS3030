#!/bin/bash - 
#===============================================================================
#
#          FILE: multiTables.sh
# 
#         USAGE: ./multiTables.sh 
# 
#   DESCRIPTION: 
# 
#         NOTES: ---
#        AUTHOR: Jon Wheeler (), jonathanwheeler1@weber.edu
#       CREATED: 01/24/2017 18:46
#      REVISION:  ---
#===============================================================================

#set -o nounset                              # Treat unset variables as an error

for (( i=1; i<=12; i++ ))
do
	for (( j=1; j<=12; j++ ))
	do
		echo -ne "$(( i * j))\t "

	done
	echo "" 

done

