#!/bin/bash
#defining a variable

#parser Apache AB Log

echo "Parser Data Uji04"
echo "Algoritma Round Robin"
# grep -w "Complete requests" Uji04-RR01.txt |& tee -a Uji04-RR-Complete-requests.txt
# sleep 
# grep -w "Complete requests" Uji04-RR02.txt |& tee -a Uji04-RR-Complete-requests.txt
# sleep 1
# grep -w "Complete requests" Uji04-RR03.txt |& tee -a Uji04-RR-Complete-requests.txt
# sleep 1
# grep -w "Complete requests" Uji04-RR04.txt |& tee -a Uji04-RR-Complete-requests.txt
# sleep 1
# grep -w "Complete requests" Uji04-RR05.txt |& tee -a Uji04-RR-Complete-requests.txt
# sleep 1

# grep -w "Failed requests" Uji04-RR01.txt |& tee -a Uji04-RR-Failed-requests.txt
# sleep 
# grep -w "Failed requests" Uji04-RR02.txt |& tee -a Uji04-RR-Failed-requests.txt
# sleep 1
# grep -w "Failed requests" Uji04-RR03.txt |& tee -a Uji04-RR-Failed-requests.txt
# sleep 1
# grep -w "Failed requests" Uji04-RR04.txt |& tee -a Uji04-RR-Failed-requests.txt
# sleep 1
# grep -w "Failed requests" Uji04-RR05.txt |& tee -a Uji04-RR-Failed-requests.txt
# sleep 1

# grep -w "(mean," Uji04-RR01.txt |& tee -a Uji04-RR-Timeper-requests.txt
# sleep 
# grep -w "(mean," Uji04-RR02.txt |& tee -a Uji04-RR-Timeper-requests.txt
# sleep 1
# grep -w "(mean," Uji04-RR03.txt |& tee -a Uji04-RR-Timeper-requests.txt
# sleep 1
# grep -w "(mean," Uji04-RR04.txt |& tee -a Uji04-RR-Timeper-requests.txt
# sleep 1
# grep -w "(mean," Uji04-RR05.txt |& tee -a Uji04-RR-Timeper-requests.txt
# sleep 1

# grep -w "Transfer rate:" Uji04-RR01.txt |& tee -a Uji04-RR-Transfer-rate.txt
# sleep 
# grep -w "Transfer rate:" Uji04-RR02.txt |& tee -a Uji04-RR-Transfer-rate.txt
# sleep 1
# grep -w "Transfer rate:" Uji04-RR03.txt |& tee -a Uji04-RR-Transfer-rate.txt
# sleep 1
# grep -w "Transfer rate:" Uji04-RR04.txt |& tee -a Uji04-RR-Transfer-rate.txt
# sleep 1
# grep -w "Transfer rate:" Uji04-RR05.txt |& tee -a Uji04-RR-Transfer-rate.txt
# sleep 1

grep -w "Requests per second:" Uji04-RR01.txt |& tee Uji04-RR-ReqPerSec.txt
sleep 
grep -w "Requests per second:" Uji04-RR02.txt |& tee -a Uji04-RR-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji04-RR03.txt |& tee -a Uji04-RR-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji04-RR04.txt |& tee -a Uji04-RR-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji04-RR05.txt |& tee -a Uji04-RR-ReqPerSec.txt
sleep 1
echo "Algoritma Random"
# grep -w "Complete requests" Uji04-Rd01.txt |& tee -a Uji04-Rd-Complete-requests.txt
# sleep 
# grep -w "Complete requests" Uji04-Rd02.txt |& tee -a Uji04-Rd-Complete-requests.txt
# sleep 1
# grep -w "Complete requests" Uji04-Rd03.txt |& tee -a Uji04-Rd-Complete-requests.txt
# sleep 1
# grep -w "Complete requests" Uji04-Rd04.txt |& tee -a Uji04-Rd-Complete-requests.txt
# sleep 1
# grep -w "Complete requests" Uji04-Rd05.txt |& tee -a Uji04-Rd-Complete-requests.txt
# sleep 1

# grep -w "Failed requests" Uji04-Rd01.txt |& tee -a Uji04-Rd-Failed-requests.txt
# sleep 
# grep -w "Failed requests" Uji04-Rd02.txt |& tee -a Uji04-Rd-Failed-requests.txt
# sleep 1
# grep -w "Failed requests" Uji04-Rd03.txt |& tee -a Uji04-Rd-Failed-requests.txt
# sleep 1
# grep -w "Failed requests" Uji04-Rd04.txt |& tee -a Uji04-Rd-Failed-requests.txt
# sleep 1
# grep -w "Failed requests" Uji04-Rd05.txt |& tee -a Uji04-Rd-Failed-requests.txt
# sleep 1

# grep -w "(mean," Uji04-Rd01.txt |& tee -a Uji04-Rd-Timeper-requests.txt
# sleep 
# grep -w "(mean," Uji04-Rd02.txt |& tee -a Uji04-Rd-Timeper-requests.txt
# sleep 1
# grep -w "(mean," Uji04-Rd03.txt |& tee -a Uji04-Rd-Timeper-requests.txt
# sleep 1
# grep -w "(mean," Uji04-Rd04.txt |& tee -a Uji04-Rd-Timeper-requests.txt
# sleep 1
# grep -w "(mean," Uji04-Rd05.txt |& tee -a Uji04-Rd-Timeper-requests.txt
# sleep 1

# grep -w "Transfer rate:" Uji04-Rd01.txt |& tee -a Uji04-Rd-Transfer-rate.txt
# sleep 
# grep -w "Transfer rate:" Uji04-Rd02.txt |& tee -a Uji04-Rd-Transfer-rate.txt
# sleep 1
# grep -w "Transfer rate:" Uji04-Rd03.txt |& tee -a Uji04-Rd-Transfer-rate.txt
# sleep 1
# grep -w "Transfer rate:" Uji04-Rd04.txt |& tee -a Uji04-Rd-Transfer-rate.txt
# sleep 1
# grep -w "Transfer rate:" Uji04-Rd05.txt |& tee -a Uji04-Rd-Transfer-rate.txt
# sleep 1

grep -w "Requests per second:" Uji04-Rd01.txt |& tee Uji04-Rd-ReqPerSec.txt
sleep 
grep -w "Requests per second:" Uji04-Rd02.txt |& tee -a Uji04-Rd-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji04-Rd03.txt |& tee -a Uji04-Rd-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji04-Rd04.txt |& tee -a Uji04-Rd-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji04-Rd05.txt |& tee -a Uji04-Rd-ReqPerSec.txt
sleep 1
echo "Algoritma Min Respon Time"
# grep -w "Complete requests" Uji04-RT01.txt |& tee -a Uji04-RT-Complete-requests.txt
# sleep 
# grep -w "Complete requests" Uji04-RT02.txt |& tee -a Uji04-RT-Complete-requests.txt
# sleep 1
# grep -w "Complete requests" Uji04-RT03.txt |& tee -a Uji04-RT-Complete-requests.txt
# sleep 1
# grep -w "Complete requests" Uji04-RT04.txt |& tee -a Uji04-RT-Complete-requests.txt
# sleep 1
# grep -w "Complete requests" Uji04-RT05.txt |& tee -a Uji04-RT-Complete-requests.txt
# sleep 1

# grep -w "Failed requests" Uji04-RT01.txt |& tee -a Uji04-RT-Failed-requests.txt
# sleep 
# grep -w "Failed requests" Uji04-RT02.txt |& tee -a Uji04-RT-Failed-requests.txt
# sleep 1
# grep -w "Failed requests" Uji04-RT03.txt |& tee -a Uji04-RT-Failed-requests.txt
# sleep 1
# grep -w "Failed requests" Uji04-RT04.txt |& tee -a Uji04-RT-Failed-requests.txt
# sleep 1
# grep -w "Failed requests" Uji04-RT05.txt |& tee -a Uji04-RT-Failed-requests.txt
# sleep 1

# grep -w "(mean," Uji04-RT01.txt |& tee -a Uji04-RT-Timeper-requests.txt
# sleep 
# grep -w "(mean," Uji04-RT02.txt |& tee -a Uji04-RT-Timeper-requests.txt
# sleep 1
# grep -w "(mean," Uji04-RT03.txt |& tee -a Uji04-RT-Timeper-requests.txt
# sleep 1
# grep -w "(mean," Uji04-RT04.txt |& tee -a Uji04-RT-Timeper-requests.txt
# sleep 1
# grep -w "(mean," Uji04-RT05.txt |& tee -a Uji04-RT-Timeper-requests.txt
# sleep 1

# grep -w "Transfer rate:" Uji04-RT01.txt |& tee -a Uji04-RT-Transfer-rate.txt
# sleep 
# grep -w "Transfer rate:" Uji04-RT02.txt |& tee -a Uji04-RT-Transfer-rate.txt
# sleep 1
# grep -w "Transfer rate:" Uji04-RT03.txt |& tee -a Uji04-RT-Transfer-rate.txt
# sleep 1
# grep -w "Transfer rate:" Uji04-RT04.txt |& tee -a Uji04-RT-Transfer-rate.txt
# sleep 1
# grep -w "Transfer rate:" Uji04-RT05.txt |& tee -a Uji04-RT-Transfer-rate.txt
# sleep 1

grep -w "Requests per second:" Uji04-RT01.txt |& tee Uji04-RT-ReqPerSec.txt
sleep 
grep -w "Requests per second:" Uji04-RT02.txt |& tee -a Uji04-RT-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji04-RT03.txt |& tee -a Uji04-RT-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji04-RT04.txt |& tee -a Uji04-RT-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji04-RT05.txt |& tee -a Uji04-RT-ReqPerSec.txt
sleep 1
echo "Algoritma Fuzy"
# grep -w "Complete requests" Uji04-FZ01.txt |& tee -a Uji04-FZ-Complete-requests.txt
# sleep 
# grep -w "Complete requests" Uji04-FZ02.txt |& tee -a Uji04-FZ-Complete-requests.txt
# sleep 1
# grep -w "Complete requests" Uji04-FZ03.txt |& tee -a Uji04-FZ-Complete-requests.txt
# sleep 1
# grep -w "Complete requests" Uji04-FZ04.txt |& tee -a Uji04-FZ-Complete-requests.txt
# sleep 1
# grep -w "Complete requests" Uji04-FZ05.txt |& tee -a Uji04-FZ-Complete-requests.txt
# sleep 1

# grep -w "Failed requests" Uji04-FZ01.txt |& tee -a Uji04-FZ-Failed-requests.txt
# sleep 
# grep -w "Failed requests" Uji04-FZ02.txt |& tee -a Uji04-FZ-Failed-requests.txt
# sleep 1
# grep -w "Failed requests" Uji04-FZ03.txt |& tee -a Uji04-FZ-Failed-requests.txt
# sleep 1
# grep -w "Failed requests" Uji04-FZ04.txt |& tee -a Uji04-FZ-Failed-requests.txt
# sleep 1
# grep -w "Failed requests" Uji04-FZ05.txt |& tee -a Uji04-FZ-Failed-requests.txt
# sleep 1

# grep -w "(mean," Uji04-FZ01.txt |& tee -a Uji04-FZ-Timeper-requests.txt
# sleep 
# grep -w "(mean," Uji04-FZ02.txt |& tee -a Uji04-FZ-Timeper-requests.txt
# sleep 1
# grep -w "(mean," Uji04-FZ03.txt |& tee -a Uji04-FZ-Timeper-requests.txt
# sleep 1
# grep -w "(mean," Uji04-FZ04.txt |& tee -a Uji04-FZ-Timeper-requests.txt
# sleep 1
# grep -w "(mean," Uji04-FZ05.txt |& tee -a Uji04-FZ-Timeper-requests.txt
# sleep 1

# grep -w "Transfer rate:" Uji04-FZ01.txt |& tee -a Uji04-FZ-Transfer-rate.txt
# sleep 
# grep -w "Transfer rate:" Uji04-FZ02.txt |& tee -a Uji04-FZ-Transfer-rate.txt
# sleep 1
# grep -w "Transfer rate:" Uji04-FZ03.txt |& tee -a Uji04-FZ-Transfer-rate.txt
# sleep 1
# grep -w "Transfer rate:" Uji04-FZ04.txt |& tee -a Uji04-FZ-Transfer-rate.txt
# sleep 1
# grep -w "Transfer rate:" Uji04-FZ05.txt |& tee -a Uji04-FZ-Transfer-rate.txt
# sleep 1

grep -w "Requests per second:" Uji04-FZ01.txt |& tee Uji04-FZ-ReqPerSec.txt
sleep 
grep -w "Requests per second:" Uji04-FZ02.txt |& tee -a Uji04-FZ-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji04-FZ03.txt |& tee -a Uji04-FZ-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji04-FZ04.txt |& tee -a Uji04-FZ-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji04-FZ05.txt |& tee -a Uji04-FZ-ReqPerSec.txt
sleep 1