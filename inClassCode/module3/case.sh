#!/bin/bash - 
#===============================================================================
#
#          FILE: case.sh
# 
#         USAGE: ./case.sh 
# 
#   DESCRIPTION: 
# 
#         NOTES: ---
#        AUTHOR: Jon Wheeler (), jonathanwheeler1@weber.edu
#       CREATED: 01/24/2017 19:29
#      REVISION:  ---
#===============================================================================

#set -o nounset                              # Treat unset variables as an error
help(){
	echo "Usage $0 <input> "
	echo "1 2 or 3"
	exit 1
}

# Require one input parameter
if [[ $# -ne 1 ]]
then
	help
fi

case $1 in
	1) echo "You Rock!"
		;;
	2) echo "Robots are awesome!"
		;;
	3) echo "Another"
		;;
	--help)
		help
		;;
	*) echo "Wrong choice"
		help
		;;
esac
exit 0

