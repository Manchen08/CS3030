#!/bin/bash - 
#===============================================================================
#
#          FILE: funcsParam.sh
# 
#         USAGE: ./funcsParam.sh 
# 
#   DESCRIPTION: 
# 
#         NOTES: ---
#        AUTHOR: Jon Wheeler (), jonathanwheeler1@weber.edu
#       CREATED: 01/19/2017 19:15
#      REVISION:  ---
#===============================================================================

#set -o nounset                              # Treat unset variables as an error

# $0 is the program 
# $1 is the first input paramater
echo "Param list [$0] [$1] [$2] [$3]"
# $# is the number of actual params (excluding $0)
echo "Param Number [$#]"
# $@ is an array of strings of params (excluding $0)
echo "Params [$@]"
exit 0
