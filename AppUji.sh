#!/bin/bash
#defining a variable
Kalimat="Pengujian Load Balancing dimulai - Uji Tanpa Beban Algoritma Random"
echo $Kalimat
$Kalimat >> LoadTest01.txt
# for loop
for i in {0..1..1}
  do 
    # Load python toggle start
    #python3 AppToggleUjiStart.py
    # Run siege
    output=$(siege http://192.168.146.10:82 -c 2 -t 1m)
    #output=$(siege http://www.len.co.id -c 2 -t 1m)
    # Output siege append to file
    $output >> LoadTest01.txt
    # Output siege to terminal echo
    echo $output
 done
# End loop
# Load python toggle stop
#python3 AppToggleUjiStop.py
