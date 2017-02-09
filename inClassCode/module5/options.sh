#!/bin/bash - 
#===============================================================================
#
#          FILE: options.sh
# 
#         USAGE: ./options.sh 
# 
#   DESCRIPTION: 
# 
#         NOTES: ---
#        AUTHOR: Jon Wheeler (), jonathanwheeler1@weber.edu
#       CREATED: 02/02/2017 18:57
#      REVISION:  ---
#===============================================================================

#set -o nounset                              # Treat unset variables as an error
# expecting options -s <> -w <> or -c
# in any order

usage()
{
	echo "Usage ./$0 -s <> -c<> -w<>"
}
if [[ $1 == "--help" ]]
then
	usage
	exit 1;
fi

while getopts ":s:w:c:" opt
do
	case $opt in
		s) size=$OPTARG
			;;
		w) width=$OPTARG
			;;
		c) color=$OPTARG
			;;
		/?)
			usage
			;;
	esac
done

if [[ -z "$size" ]]
then

	echo "Size is required"
fi

echo "[$size] [$width] [$color]"
exit 0

