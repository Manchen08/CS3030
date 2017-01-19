#!/bin/bash - 
#===============================================================================
#
#          FILE: cond.sh
# 
#         USAGE: ./cond.sh 
# 
#   DESCRIPTION: Practice conditional statements
# 
#         NOTES: ---
#        AUTHOR: Jon Wheeler (), jonathanwheeler1@weber.edu
#       CREATED: 01/19/2017 18:40
#      REVISION:  ---
#===============================================================================

#set -o nounset                              # Treat unset variables as an error

echo "Enter your favorite team"
#take input from user
read Team
#Team="Real Madrid"

#Add spaces after if and after [[ and before ]]
if [[ $Team == "Real Madrid" ]]
then
	echo "You know a lot of futbol"
else
	echo "You do not know a lot of futbol"
	exit 1
fi

exit 0
