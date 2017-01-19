#!/bin/bash - 
#===============================================================================
#
#          FILE: funcs.sh
# 
#         USAGE: ./funcs.sh 
# 
#   DESCRIPTION: 
# 
#         NOTES: ---
#        AUTHOR: Jon Wheeler (), jonathanwheeler1@weber.edu
#       CREATED: 01/19/2017 18:56
#      REVISION:  ---
#===============================================================================

#set -o nounset                              # Treat unset variables as an error

Hello="Weber"
# () are not required
function help1
{
	echo "Inside help 1 $Hello"
}

# () are required
help2()
{
	# For local variables use local
	local Hello="Waldo"
	echo "help2 $Hello $1"
}

# To call a function, it must be defined above the call
help1
echo "Now calling another function"
help2(World)
exit 0

