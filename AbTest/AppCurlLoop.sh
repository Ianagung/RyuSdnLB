#!/bin/bash
#defining a variable
Kalimat="PBackground Traffic Curl - Loop"
echo $Kalimat
echo "infinite loops [ hit CTRL+C to stop]"
# for loop
for i in {0..36000..1}
  do 
    curl --silent http://192.168.146.100:8080/index.html > /dev/null
    sleep 1    
 done
# End loop