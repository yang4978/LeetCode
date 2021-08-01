# Read from the file file.txt and output the tenth line to stdout.

#!/bin/bash

# method 1 #
#declare -i i
#i=0
#while read line
#do
#    i=${i}+1
#    if [[ "${i}" == "10" ]]
#    then
#        echo ${line}
#    fi
#done < file.txt

# method 2 #
#sed -n '10p' file.txt

# method 3 #
#tail -n +10 file.txt | head -n 1

# method 4 #
awk 'NR==10' file.txt
