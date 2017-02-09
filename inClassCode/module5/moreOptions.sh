#!/bin/bash - 
#===============================================================================
#
#          FILE: moreOptions.sh
# 
#         USAGE: ./moreOptions.sh 
# 
#   DESCRIPTION: 
# 
#         NOTES: ---
#        AUTHOR: Jon Wheeler (), jonathanwheeler1@weber.edu
#       CREATED: 02/02/2017 19:17
#      REVISION:  ---
#===============================================================================

#set -o nounset                              # Treat unset variables as an error

help()
{
	echo "Usage: $0 -f firstName -l lastName -t favoriteTeam"
	exit 1
}

while getopts ":f:l:t:" opt
do
	case $opt in
		f) first=$OPTARG
			;;
		l) last=$OPTARG
			;;
		t) team=$OPTARG
			;;
		/?)
			help
			;;
	esac
done

if [[ -z $team ]]
then
	echo "Last name is required"
	help
fi

echo "[$first] [$last] [$team]"
exit 0

