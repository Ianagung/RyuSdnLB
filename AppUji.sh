#!/bin/bash
#defining a variable
Kalimat="Pengujian Load Balancing dimulai - Uji Tanpa Beban Algoritma Min Respon Time"
echo $Kalimat |& tee LoadTest01-Random01.txt
# for loop
for i in {0..4..1}
  do 
    # Load python toggle start
    python3 AppToggleUjiStart.py
    # Run siege
    ab -n 100 -c 2 http://192.168.146.10:1000/ |& tee -a LoadTest01-Random01.txt
    #siege http://192.168.146.10:85 -c 250 -t 1m |& tee -a LoadTest01-RR01.txt
    #output=$(siege http://www.len.co.id -c 2 -t 1m)
    # Output siege append to file
    #$output >> LoadTest01.txt
    # Output siege to terminal echo
    echo "selesai"
    # Load python toggle stop
    python3 AppToggleUjiStop.py
    sleep 5    
 done
# End loop

