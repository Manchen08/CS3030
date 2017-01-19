#!/bin/bash - 
#===============================================================================
#
#          FILE: task4_1.sh
# 
#         USAGE: ./task4_1.sh 
# 
#   DESCRIPTION: Take two input params and display them together as one string
#				Check for valid number of params
#				if missing params, call help function and exit 1
# 
#         NOTES: ---
#        AUTHOR: Jon Wheeler (), jonathanwheeler1@weber.edu
#       CREATED: 01/19/2017 19:20
#      REVISION:  ---
#===============================================================================

#set -o nounset                              # Treat unset variables as an error

numParams=$#

help()
{
	# REMEMBER! $1 $2 inside a function are function parameters NOT program parameters.
	echo "This program requires at least strings to run you entered $numParams"
}

printFuncParams()
{
	# REMEMBER! $1 $2 inside a function are function parameters NOT program parameters.
	echo "Passing Function params example: $2 $1"
}

if [[ $1 == "--help" ]]
then
	echo "This is our help function"
	help
	exit 0
fi

if [[ $# != 2 ]]
then
	help
	exit 1
fi

echo "These are your two string..."
echo "$1 $2"
printFuncParams $1 $2
exit 0
