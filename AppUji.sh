#!/bin/bash
#defining a variable
Kalimat="Pengujian Load Balancing dimulai - Uji3 Tanpa Beban Algoritma Random"
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
    ab -n 100 -c 5 http://192.168.146.100:1000/ |& tee -a Uji03-Rd01.txt
    # Load python toggle stop
    python3 AppToggleUjiStop.py
    sleep 1

    echo "selesai" |& tee -a Uji03-Rd01.txt
    sleep 1    
 done
# End loop

echo $Kalimat |& tee Uji03-Rd02.txt
# for loop
for i in {0..29..1}
  do 
    
    #sleep 5
    echo "Testing number $i " |& tee -a Uji03-Rd02.txt

    # Load python toggle start
    python3 AppToggleUjiStart.py
    echo "Tes request 200" |& tee -a Uji03-Rd02.txt
    # Run ab
    ab -n 200 -c 5 http://192.168.146.100:1000/ |& tee -a Uji03-Rd02.txt
    # Load python toggle stop
    python3 AppToggleUjiStop.py
    sleep 1

    echo "selesai" |& tee -a Uji03-Rd02.txt
    sleep 1    
 done
# End loop

echo $Kalimat |& tee Uji03-Rd03.txt
# for loop
for i in {0..29..1}
  do 
    
    #sleep 5
    echo "Testing number $i " |& tee -a Uji03-Rd03.txt

   # Load python toggle start
    python3 AppToggleUjiStart.py
    echo "Tes request 300" |& tee -a Uji03-Rd03.txt
    # Run ab
    ab -n 300 -c 5 http://192.168.146.100:1000/ |& tee -a Uji03-Rd03.txt
    # Load python toggle stop
    python3 AppToggleUjiStop.py
    sleep 1

    echo "selesai" |& tee -a Uji03-Rd03.txt
    sleep 1    
 done
# End loop

echo $Kalimat |& tee Uji03-Rd04.txt
# for loop
for i in {0..29..1}
  do 
    
    #sleep 5
    echo "Testing number $i " |& tee -a Uji03-Rd04.txt

    # Load python toggle start
    python3 AppToggleUjiStart.py
    echo "Tes request 400" |& tee -a Uji03-Rd04.txt
    # Run ab
    ab -n 400 -c 5 http://192.168.146.100:1000/ |& tee -a Uji03-Rd04.txt
    # Load python toggle stop
    python3 AppToggleUjiStop.py
    sleep 1

    echo "selesai" |& tee -a Uji03-Rd04.txt
    sleep 1    
 done
# End loop

echo $Kalimat |& tee Uji03-Rd05.txt
# for loop
for i in {0..29..1}
  do 
    
    #sleep 5
    echo "Testing number $i " |& tee -a Uji03-Rd05.txt
    # Load python toggle start
    python3 AppToggleUjiStart.py
    echo "Tes request 500" |& tee -a Uji03-Rd05.txt
    # Run ab
    ab -n 500 -c 5 http://192.168.146.100:1000/ |& tee -a Uji03-Rd05.txt
    # Load python toggle stop
    python3 AppToggleUjiStop.py
    sleep 1

    echo "selesai" |& tee -a Uji03-Rd05.txt
    sleep 1    
 done
# End loop