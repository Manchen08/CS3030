#!/bin/bash - 
#===============================================================================
#
#          FILE: helloFun.sh
# 
#         USAGE: ./helloFun.sh 
# 
#   DESCRIPTION: 
# 
#         NOTES: ---
#        AUTHOR: Jon Wheeler (), jonathanwheeler1@weber.edu
#       CREATED: 01/17/2017 20:16
#      REVISION:  ---
#===============================================================================

#set -o nounset                              # Treat unset variables as an error

#Help Function
help(){
	echo "Help function"
}

#call funcation 
echo "before function"
help
echo "after function"

exit 0

