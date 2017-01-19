#!/bin/bash - 
#===============================================================================
#
#          FILE: forLoop.sh
# 
#         USAGE: ./forLoop.sh 
# 
#   DESCRIPTION: Practice for loop
# 
#         NOTES: ---
#        AUTHOR: Jon Wheeler (), jonathanwheeler1@weber.edu
#       CREATED: 01/19/2017 20:00
#      REVISION:  ---
#===============================================================================

#set -o nounset                              # Treat unset variables as an error

# List files in pwd

for f in $(ls)
do
	echo "File $f"
done

# ` for program call
for n in `seq 0 2 10`
do
	echo "Number $n"
done

exit 0
