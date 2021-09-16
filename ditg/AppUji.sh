#!/bin/bash
#defining a variable
Kalimat="Pengujian Load Balancing dimulai - Uji4 Dengan Beban Fuzzy"
echo $Kalimat |& tee Uji04-FZ01.txt
# for loop
for i in {0..29..1}
  do 
    
    #sleep 5
    echo "Testing number $i " |& tee -a Uji04-FZ01.txt

    # Load python toggle start
    python3 AppToggleUjiStart.py
    echo "Tes request 100" |& tee -a Uji04-FZ01.txt
    # Run ab
    ab -n 100 -c 10 http://192.168.146.100:1000/ |& tee -a Uji04-FZ01.txt
    # Load python toggle stop
    python3 AppToggleUjiStop.py
    sleep 1

    echo "selesai" |& tee -a Uji04-FZ01.txt
    sleep 1    
 done
# End loop

echo $Kalimat |& tee Uji04-FZ02.txt
# for loop
for i in {0..29..1}
  do 
    
    #sleep 5
    echo "Testing number $i " |& tee -a Uji04-FZ02.txt

    # Load python toggle start
    python3 AppToggleUjiStart.py
    echo "Tes request 200" |& tee -a Uji04-FZ02.txt
    # Run ab
    ab -n 200 -c 10 http://192.168.146.100:1000/ |& tee -a Uji04-FZ02.txt
    # Load python toggle stop
    python3 AppToggleUjiStop.py
    sleep 1

    echo "selesai" |& tee -a Uji04-FZ02.txt
    sleep 1    
 done
# End loop

echo $Kalimat |& tee Uji04-FZ03.txt
# for loop
for i in {0..29..1}
  do 
    
    #sleep 5
    echo "Testing number $i " |& tee -a Uji04-FZ03.txt

   # Load python toggle start
    python3 AppToggleUjiStart.py
    echo "Tes request 300" |& tee -a Uji04-FZ03.txt
    # Run ab
    ab -n 300 -c 10 http://192.168.146.100:1000/ |& tee -a Uji04-FZ03.txt
    # Load python toggle stop
    python3 AppToggleUjiStop.py
    sleep 1

    echo "selesai" |& tee -a Uji04-FZ03.txt
    sleep 1    
 done
# End loop

echo $Kalimat |& tee Uji04-FZ04.txt
# for loop
for i in {0..29..1}
  do 
    
    #sleep 5
    echo "Testing number $i " |& tee -a Uji04-FZ04.txt

    # Load python toggle start
    python3 AppToggleUjiStart.py
    echo "Tes request 400" |& tee -a Uji04-FZ04.txt
    # Run ab
    ab -n 400 -c 10 http://192.168.146.100:1000/ |& tee -a Uji04-FZ04.txt
    # Load python toggle stop
    python3 AppToggleUjiStop.py
    sleep 1

    echo "selesai" |& tee -a Uji04-FZ04.txt
    sleep 1    
 done
# End loop

echo $Kalimat |& tee Uji04-FZ05.txt
# for loop
for i in {0..29..1}
  do 
    
    #sleep 5
    echo "Testing number $i " |& tee -a Uji04-FZ05.txt
    # Load python toggle start
    python3 AppToggleUjiStart.py
    echo "Tes request 500" |& tee -a Uji04-FZ05.txt
    # Run ab
    ab -n 500 -c 10 http://192.168.146.100:1000/ |& tee -a Uji04-FZ05.txt
    # Load python toggle stop
    python3 AppToggleUjiStop.py
    sleep 1

    echo "selesai" |& tee -a Uji04-FZ05.txt
    sleep 1    
 done
# End loop