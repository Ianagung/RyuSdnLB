#!/bin/bash
#defining a variable
Kalimat="Pengujian Load Balancing dimulai - Uji Beban Algoritma Fuzzy"
echo $Kalimat |& tee Uji02-FZ01.txt
# for loop
for i in {0..29..1}
  do 
    # Load python toggle start
    python3 AppToggleUjiStart.py
    #sleep 5
    #echo "kosongan" |& tee Uji02-0.txt
    # Run siege
    ab -n 100 -c 5 http://192.168.146.100:1000/ |& tee -a Uji02-FZ01.txt
    #siege http://192.168.146.10:85 -c 250 -t 1m |& tee -a LoadTest01-RR01.txt
    #output=$(siege http://www.len.co.id -c 2 -t 1m)
    # Output siege append to file
    #$output >> LoadTest01.txt
    # Output siege to terminal echo
    echo "selesai"
    # Load python toggle stop
    python3 AppToggleUjiStop.py
    sleep 1    
 done
# End loop

