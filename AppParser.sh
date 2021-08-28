#!/bin/bash
#defining a variable

#parser Apache AB Log

echo "Parser Data Uji03"
echo "Algoritma Round Robin"
# grep -w "Complete requests" Uji03-RR01.txt |& tee -a Uji03-RR-Complete-requests.txt
# sleep 
# grep -w "Complete requests" Uji03-RR02.txt |& tee -a Uji03-RR-Complete-requests.txt
# sleep 1
# grep -w "Complete requests" Uji03-RR03.txt |& tee -a Uji03-RR-Complete-requests.txt
# sleep 1
# grep -w "Complete requests" Uji03-RR04.txt |& tee -a Uji03-RR-Complete-requests.txt
# sleep 1
# grep -w "Complete requests" Uji03-RR05.txt |& tee -a Uji03-RR-Complete-requests.txt
# sleep 1

# grep -w "Failed requests" Uji03-RR01.txt |& tee -a Uji03-RR-Failed-requests.txt
# sleep 
# grep -w "Failed requests" Uji03-RR02.txt |& tee -a Uji03-RR-Failed-requests.txt
# sleep 1
# grep -w "Failed requests" Uji03-RR03.txt |& tee -a Uji03-RR-Failed-requests.txt
# sleep 1
# grep -w "Failed requests" Uji03-RR04.txt |& tee -a Uji03-RR-Failed-requests.txt
# sleep 1
# grep -w "Failed requests" Uji03-RR05.txt |& tee -a Uji03-RR-Failed-requests.txt
# sleep 1

# grep -w "(mean," Uji03-RR01.txt |& tee -a Uji03-RR-Timeper-requests.txt
# sleep 
# grep -w "(mean," Uji03-RR02.txt |& tee -a Uji03-RR-Timeper-requests.txt
# sleep 1
# grep -w "(mean," Uji03-RR03.txt |& tee -a Uji03-RR-Timeper-requests.txt
# sleep 1
# grep -w "(mean," Uji03-RR04.txt |& tee -a Uji03-RR-Timeper-requests.txt
# sleep 1
# grep -w "(mean," Uji03-RR05.txt |& tee -a Uji03-RR-Timeper-requests.txt
# sleep 1

# grep -w "Transfer rate:" Uji03-RR01.txt |& tee -a Uji03-RR-Transfer-rate.txt
# sleep 
# grep -w "Transfer rate:" Uji03-RR02.txt |& tee -a Uji03-RR-Transfer-rate.txt
# sleep 1
# grep -w "Transfer rate:" Uji03-RR03.txt |& tee -a Uji03-RR-Transfer-rate.txt
# sleep 1
# grep -w "Transfer rate:" Uji03-RR04.txt |& tee -a Uji03-RR-Transfer-rate.txt
# sleep 1
# grep -w "Transfer rate:" Uji03-RR05.txt |& tee -a Uji03-RR-Transfer-rate.txt
# sleep 1

grep -w "Requests per second:" Uji03-RR01.txt |& tee Uji03-RR-ReqPerSec.txt
sleep 
grep -w "Requests per second:" Uji03-RR02.txt |& tee -a Uji03-RR-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji03-RR03.txt |& tee -a Uji03-RR-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji03-RR04.txt |& tee -a Uji03-RR-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji03-RR05.txt |& tee -a Uji03-RR-ReqPerSec.txt
sleep 1
echo "Algoritma Random"
# grep -w "Complete requests" Uji03-Rd01.txt |& tee -a Uji03-Rd-Complete-requests.txt
# sleep 
# grep -w "Complete requests" Uji03-Rd02.txt |& tee -a Uji03-Rd-Complete-requests.txt
# sleep 1
# grep -w "Complete requests" Uji03-Rd03.txt |& tee -a Uji03-Rd-Complete-requests.txt
# sleep 1
# grep -w "Complete requests" Uji03-Rd04.txt |& tee -a Uji03-Rd-Complete-requests.txt
# sleep 1
# grep -w "Complete requests" Uji03-Rd05.txt |& tee -a Uji03-Rd-Complete-requests.txt
# sleep 1

# grep -w "Failed requests" Uji03-Rd01.txt |& tee -a Uji03-Rd-Failed-requests.txt
# sleep 
# grep -w "Failed requests" Uji03-Rd02.txt |& tee -a Uji03-Rd-Failed-requests.txt
# sleep 1
# grep -w "Failed requests" Uji03-Rd03.txt |& tee -a Uji03-Rd-Failed-requests.txt
# sleep 1
# grep -w "Failed requests" Uji03-Rd04.txt |& tee -a Uji03-Rd-Failed-requests.txt
# sleep 1
# grep -w "Failed requests" Uji03-Rd05.txt |& tee -a Uji03-Rd-Failed-requests.txt
# sleep 1

# grep -w "(mean," Uji03-Rd01.txt |& tee -a Uji03-Rd-Timeper-requests.txt
# sleep 
# grep -w "(mean," Uji03-Rd02.txt |& tee -a Uji03-Rd-Timeper-requests.txt
# sleep 1
# grep -w "(mean," Uji03-Rd03.txt |& tee -a Uji03-Rd-Timeper-requests.txt
# sleep 1
# grep -w "(mean," Uji03-Rd04.txt |& tee -a Uji03-Rd-Timeper-requests.txt
# sleep 1
# grep -w "(mean," Uji03-Rd05.txt |& tee -a Uji03-Rd-Timeper-requests.txt
# sleep 1

# grep -w "Transfer rate:" Uji03-Rd01.txt |& tee -a Uji03-Rd-Transfer-rate.txt
# sleep 
# grep -w "Transfer rate:" Uji03-Rd02.txt |& tee -a Uji03-Rd-Transfer-rate.txt
# sleep 1
# grep -w "Transfer rate:" Uji03-Rd03.txt |& tee -a Uji03-Rd-Transfer-rate.txt
# sleep 1
# grep -w "Transfer rate:" Uji03-Rd04.txt |& tee -a Uji03-Rd-Transfer-rate.txt
# sleep 1
# grep -w "Transfer rate:" Uji03-Rd05.txt |& tee -a Uji03-Rd-Transfer-rate.txt
# sleep 1

grep -w "Requests per second:" Uji03-Rd01.txt |& tee Uji03-Rd-ReqPerSec.txt
sleep 
grep -w "Requests per second:" Uji03-Rd02.txt |& tee -a Uji03-Rd-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji03-Rd03.txt |& tee -a Uji03-Rd-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji03-Rd04.txt |& tee -a Uji03-Rd-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji03-Rd05.txt |& tee -a Uji03-Rd-ReqPerSec.txt
sleep 1
echo "Algoritma Min Respon Time"
# grep -w "Complete requests" Uji03-RT01.txt |& tee -a Uji03-RT-Complete-requests.txt
# sleep 
# grep -w "Complete requests" Uji03-RT02.txt |& tee -a Uji03-RT-Complete-requests.txt
# sleep 1
# grep -w "Complete requests" Uji03-RT03.txt |& tee -a Uji03-RT-Complete-requests.txt
# sleep 1
# grep -w "Complete requests" Uji03-RT04.txt |& tee -a Uji03-RT-Complete-requests.txt
# sleep 1
# grep -w "Complete requests" Uji03-RT05.txt |& tee -a Uji03-RT-Complete-requests.txt
# sleep 1

# grep -w "Failed requests" Uji03-RT01.txt |& tee -a Uji03-RT-Failed-requests.txt
# sleep 
# grep -w "Failed requests" Uji03-RT02.txt |& tee -a Uji03-RT-Failed-requests.txt
# sleep 1
# grep -w "Failed requests" Uji03-RT03.txt |& tee -a Uji03-RT-Failed-requests.txt
# sleep 1
# grep -w "Failed requests" Uji03-RT04.txt |& tee -a Uji03-RT-Failed-requests.txt
# sleep 1
# grep -w "Failed requests" Uji03-RT05.txt |& tee -a Uji03-RT-Failed-requests.txt
# sleep 1

# grep -w "(mean," Uji03-RT01.txt |& tee -a Uji03-RT-Timeper-requests.txt
# sleep 
# grep -w "(mean," Uji03-RT02.txt |& tee -a Uji03-RT-Timeper-requests.txt
# sleep 1
# grep -w "(mean," Uji03-RT03.txt |& tee -a Uji03-RT-Timeper-requests.txt
# sleep 1
# grep -w "(mean," Uji03-RT04.txt |& tee -a Uji03-RT-Timeper-requests.txt
# sleep 1
# grep -w "(mean," Uji03-RT05.txt |& tee -a Uji03-RT-Timeper-requests.txt
# sleep 1

# grep -w "Transfer rate:" Uji03-RT01.txt |& tee -a Uji03-RT-Transfer-rate.txt
# sleep 
# grep -w "Transfer rate:" Uji03-RT02.txt |& tee -a Uji03-RT-Transfer-rate.txt
# sleep 1
# grep -w "Transfer rate:" Uji03-RT03.txt |& tee -a Uji03-RT-Transfer-rate.txt
# sleep 1
# grep -w "Transfer rate:" Uji03-RT04.txt |& tee -a Uji03-RT-Transfer-rate.txt
# sleep 1
# grep -w "Transfer rate:" Uji03-RT05.txt |& tee -a Uji03-RT-Transfer-rate.txt
# sleep 1

grep -w "Requests per second:" Uji03-RT01.txt |& tee Uji03-RT-ReqPerSec.txt
sleep 
grep -w "Requests per second:" Uji03-RT02.txt |& tee -a Uji03-RT-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji03-RT03.txt |& tee -a Uji03-RT-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji03-RT04.txt |& tee -a Uji03-RT-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji03-RT05.txt |& tee -a Uji03-RT-ReqPerSec.txt
sleep 1
echo "Algoritma Fuzy"
# grep -w "Complete requests" Uji03-FZ01.txt |& tee -a Uji03-FZ-Complete-requests.txt
# sleep 
# grep -w "Complete requests" Uji03-FZ02.txt |& tee -a Uji03-FZ-Complete-requests.txt
# sleep 1
# grep -w "Complete requests" Uji03-FZ03.txt |& tee -a Uji03-FZ-Complete-requests.txt
# sleep 1
# grep -w "Complete requests" Uji03-FZ04.txt |& tee -a Uji03-FZ-Complete-requests.txt
# sleep 1
# grep -w "Complete requests" Uji03-FZ05.txt |& tee -a Uji03-FZ-Complete-requests.txt
# sleep 1

# grep -w "Failed requests" Uji03-FZ01.txt |& tee -a Uji03-FZ-Failed-requests.txt
# sleep 
# grep -w "Failed requests" Uji03-FZ02.txt |& tee -a Uji03-FZ-Failed-requests.txt
# sleep 1
# grep -w "Failed requests" Uji03-FZ03.txt |& tee -a Uji03-FZ-Failed-requests.txt
# sleep 1
# grep -w "Failed requests" Uji03-FZ04.txt |& tee -a Uji03-FZ-Failed-requests.txt
# sleep 1
# grep -w "Failed requests" Uji03-FZ05.txt |& tee -a Uji03-FZ-Failed-requests.txt
# sleep 1

# grep -w "(mean," Uji03-FZ01.txt |& tee -a Uji03-FZ-Timeper-requests.txt
# sleep 
# grep -w "(mean," Uji03-FZ02.txt |& tee -a Uji03-FZ-Timeper-requests.txt
# sleep 1
# grep -w "(mean," Uji03-FZ03.txt |& tee -a Uji03-FZ-Timeper-requests.txt
# sleep 1
# grep -w "(mean," Uji03-FZ04.txt |& tee -a Uji03-FZ-Timeper-requests.txt
# sleep 1
# grep -w "(mean," Uji03-FZ05.txt |& tee -a Uji03-FZ-Timeper-requests.txt
# sleep 1

# grep -w "Transfer rate:" Uji03-FZ01.txt |& tee -a Uji03-FZ-Transfer-rate.txt
# sleep 
# grep -w "Transfer rate:" Uji03-FZ02.txt |& tee -a Uji03-FZ-Transfer-rate.txt
# sleep 1
# grep -w "Transfer rate:" Uji03-FZ03.txt |& tee -a Uji03-FZ-Transfer-rate.txt
# sleep 1
# grep -w "Transfer rate:" Uji03-FZ04.txt |& tee -a Uji03-FZ-Transfer-rate.txt
# sleep 1
# grep -w "Transfer rate:" Uji03-FZ05.txt |& tee -a Uji03-FZ-Transfer-rate.txt
# sleep 1

grep -w "Requests per second:" Uji03-FZ01.txt |& tee Uji03-FZ-ReqPerSec.txt
sleep 
grep -w "Requests per second:" Uji03-FZ02.txt |& tee -a Uji03-FZ-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji03-FZ03.txt |& tee -a Uji03-FZ-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji03-FZ04.txt |& tee -a Uji03-FZ-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji03-FZ05.txt |& tee -a Uji03-FZ-ReqPerSec.txt
sleep 1