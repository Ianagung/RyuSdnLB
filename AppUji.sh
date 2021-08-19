#!/bin/bash
#defining a variable
Kalimat="Pengujian Load Balancing dimulai - Uji Tanpa Beban Algoritma Random"
echo $Kalimat |& tree LoadTest01-RR01.txt
# for loop
for i in {0..1..1}
  do 
    # Load python toggle start
    python3 AppToggleUjiStart.py
    # Run siege
    siege http://192.168.146.10:85 -c 2 -t 1m |& tree -a LoadTest01-RR01.txt
    #output=$(siege http://www.len.co.id -c 2 -t 1m)
    # Output siege append to file
    #$output >> LoadTest01.txt
    # Output siege to terminal echo
    echo "selesai"
    # Load python toggle stop
    python3 AppToggleUjiStop.py    
 done
# End loop

