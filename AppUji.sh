#!/bin/bash
#defining a variable
Kalimat="Pengujian Load Balancing dimulai - Uji Beban Algoritma Fuzzy"
echo $Kalimat |& tee Uji03-Rd01.txt
# for loop
for i in {0..29..1}
  do 
    
    #sleep 5
    echo "Testing number $i " |& tee -a Uji03-Rd01.txt

    # Load python toggle start
    python3 AppToggleUjiStart.py
    echo "Tes request 100" |& tee -a Uji03-Rd01.txt
    # Run ab
    ab -n 100 -c 10 http://192.168.146.100:1000/ |& tee -a Uji03-Rd01.txt
    # Load python toggle stop
    python3 AppToggleUjiStop.py
    sleep 1

    echo "selesai" |& tee -a Uji03-Rd01.txt
    sleep 1    
 done
# End loop

for i in {0..29..1}
  do 
    
    #sleep 5
    echo "Testing number $i " |& tee -a Uji03-Rd01.txt

    # Load python toggle start
    python3 AppToggleUjiStart.py
    echo "Tes request 1000" |& tee -a Uji03-Rd01.txt
    # Run ab
    ab -n 1000 -c 10 http://192.168.146.100:1000/ |& tee -a Uji03-Rd01.txt
    # Load python toggle stop
    python3 AppToggleUjiStop.py
    sleep 1

    echo "selesai" |& tee -a Uji03-Rd01.txt
    sleep 1    
 done
# End loop

for i in {0..29..1}
  do 
    
    #sleep 5
    echo "Testing number $i " |& tee -a Uji03-Rd01.txt

   # Load python toggle start
    python3 AppToggleUjiStart.py
    echo "Tes request 2000" |& tee -a Uji03-Rd01.txt
    # Run ab
    ab -n 2000 -c 10 http://192.168.146.100:1000/ |& tee -a Uji03-Rd01.txt
    # Load python toggle stop
    python3 AppToggleUjiStop.py
    sleep 1

    echo "selesai" |& tee -a Uji03-Rd01.txt
    sleep 1    
 done
# End loop

for i in {0..29..1}
  do 
    
    #sleep 5
    echo "Testing number $i " |& tee -a Uji03-Rd01.txt

    # Load python toggle start
    python3 AppToggleUjiStart.py
    echo "Tes request 3000" |& tee -a Uji03-Rd01.txt
    # Run ab
    ab -n 3000 -c 10 http://192.168.146.100:1000/ |& tee -a Uji03-Rd01.txt
    # Load python toggle stop
    python3 AppToggleUjiStop.py
    sleep 1

    echo "selesai" |& tee -a Uji03-Rd01.txt
    sleep 1    
 done
# End loop

for i in {0..29..1}
  do 
    
    #sleep 5
    echo "Testing number $i " |& tee -a Uji03-Rd01.txt
    # Load python toggle start
    python3 AppToggleUjiStart.py
    echo "Tes request 4000" |& tee -a Uji03-Rd01.txt
    # Run ab
    ab -n 4000 -c 10 http://192.168.146.100:1000/ |& tee -a Uji03-Rd01.txt
    # Load python toggle stop
    python3 AppToggleUjiStop.py
    sleep 1

    echo "selesai" |& tee -a Uji03-Rd01.txt
    sleep 1    
 done
# End loop