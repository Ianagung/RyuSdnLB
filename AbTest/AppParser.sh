#!/bin/bash
#defining a variable

#parser Apache AB Log

echo "Parser Data Uji05"
echo "Algoritma Round Robin"
grep -w "Complete requests" Uji05-RR01.txt |& tee -a Uji05-RR-Complete-requests.txt
sleep 
grep -w "Complete requests" Uji05-RR02.txt |& tee -a Uji05-RR-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji05-RR03.txt |& tee -a Uji05-RR-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji05-RR04.txt |& tee -a Uji05-RR-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji05-RR05.txt |& tee -a Uji05-RR-Complete-requests.txt
sleep 1

grep -w "Failed requests" Uji05-RR01.txt |& tee -a Uji05-RR-Failed-requests.txt
sleep 
grep -w "Failed requests" Uji05-RR02.txt |& tee -a Uji05-RR-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji05-RR03.txt |& tee -a Uji05-RR-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji05-RR04.txt |& tee -a Uji05-RR-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji05-RR05.txt |& tee -a Uji05-RR-Failed-requests.txt
sleep 1

grep -w "(mean," Uji05-RR01.txt |& tee -a Uji05-RR-Timeper-requests.txt
sleep 
grep -w "(mean," Uji05-RR02.txt |& tee -a Uji05-RR-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji05-RR03.txt |& tee -a Uji05-RR-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji05-RR04.txt |& tee -a Uji05-RR-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji05-RR05.txt |& tee -a Uji05-RR-Timeper-requests.txt
sleep 1

grep -w "Transfer rate:" Uji05-RR01.txt |& tee -a Uji05-RR-Transfer-rate.txt
sleep 
grep -w "Transfer rate:" Uji05-RR02.txt |& tee -a Uji05-RR-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji05-RR03.txt |& tee -a Uji05-RR-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji05-RR04.txt |& tee -a Uji05-RR-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji05-RR05.txt |& tee -a Uji05-RR-Transfer-rate.txt
sleep 1

grep -w "Requests per second:" Uji05-RR01.txt |& tee Uji05-RR-ReqPerSec.txt
sleep 
grep -w "Requests per second:" Uji05-RR02.txt |& tee -a Uji05-RR-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji05-RR03.txt |& tee -a Uji05-RR-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji05-RR04.txt |& tee -a Uji05-RR-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji05-RR05.txt |& tee -a Uji05-RR-ReqPerSec.txt
sleep 1

grep -w "Total:" Uji05-RR01.txt |& tee Uji05-RR-ReqPerSec.txt
sleep 
grep -w "Total:" Uji05-RR02.txt |& tee -a Uji05-RR-ReqPerSec.txt
sleep 1
grep -w "Total:" Uji05-RR03.txt |& tee -a Uji05-RR-ReqPerSec.txt
sleep 1
grep -w "Total:" Uji05-RR04.txt |& tee -a Uji05-RR-ReqPerSec.txt
sleep 1
grep -w "Total:" Uji05-RR05.txt |& tee -a Uji05-RR-ReqPerSec.txt
sleep 1
echo "Algoritma Random"
grep -w "Complete requests" Uji05-RD01.txt |& tee -a Uji05-RD-Complete-requests.txt
sleep 
grep -w "Complete requests" Uji05-RD02.txt |& tee -a Uji05-RD-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji05-RD03.txt |& tee -a Uji05-RD-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji05-RD04.txt |& tee -a Uji05-RD-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji05-RD05.txt |& tee -a Uji05-RD-Complete-requests.txt
sleep 1

grep -w "Failed requests" Uji05-RD01.txt |& tee -a Uji05-RD-Failed-requests.txt
sleep 
grep -w "Failed requests" Uji05-RD02.txt |& tee -a Uji05-RD-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji05-RD03.txt |& tee -a Uji05-RD-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji05-RD04.txt |& tee -a Uji05-RD-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji05-RD05.txt |& tee -a Uji05-RD-Failed-requests.txt
sleep 1

grep -w "(mean," Uji05-RD01.txt |& tee -a Uji05-RD-Timeper-requests.txt
sleep 
grep -w "(mean," Uji05-RD02.txt |& tee -a Uji05-RD-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji05-RD03.txt |& tee -a Uji05-RD-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji05-RD04.txt |& tee -a Uji05-RD-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji05-RD05.txt |& tee -a Uji05-RD-Timeper-requests.txt
sleep 1

grep -w "Transfer rate:" Uji05-RD01.txt |& tee -a Uji05-RD-Transfer-rate.txt
sleep 
grep -w "Transfer rate:" Uji05-RD02.txt |& tee -a Uji05-RD-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji05-RD03.txt |& tee -a Uji05-RD-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji05-RD04.txt |& tee -a Uji05-RD-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji05-RD05.txt |& tee -a Uji05-RD-Transfer-rate.txt
sleep 1

grep -w "Requests per second:" Uji05-RD01.txt |& tee Uji05-RD-ReqPerSec.txt
sleep 
grep -w "Requests per second:" Uji05-RD02.txt |& tee -a Uji05-RD-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji05-RD03.txt |& tee -a Uji05-RD-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji05-RD04.txt |& tee -a Uji05-RD-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji05-RD05.txt |& tee -a Uji05-RD-ReqPerSec.txt
sleep 1

grep -w "Total:" Uji05-RD01.txt |& tee Uji05-RD-ReqPerSec.txt
sleep 
grep -w "Total:" Uji05-RD02.txt |& tee -a Uji05-RD-ReqPerSec.txt
sleep 1
grep -w "Total:" Uji05-RD03.txt |& tee -a Uji05-RD-ReqPerSec.txt
sleep 1
grep -w "Total:" Uji05-RD04.txt |& tee -a Uji05-RD-ReqPerSec.txt
sleep 1
grep -w "Total:" Uji05-RD05.txt |& tee -a Uji05-RD-ReqPerSec.txt
sleep 1

echo "Algoritma Min Respon Time"
grep -w "Complete requests" Uji05-RT01.txt |& tee -a Uji05-RT-Complete-requests.txt
sleep 
grep -w "Complete requests" Uji05-RT02.txt |& tee -a Uji05-RT-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji05-RT03.txt |& tee -a Uji05-RT-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji05-RT04.txt |& tee -a Uji05-RT-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji05-RT05.txt |& tee -a Uji05-RT-Complete-requests.txt
sleep 1

grep -w "Failed requests" Uji05-RT01.txt |& tee -a Uji05-RT-Failed-requests.txt
sleep 
grep -w "Failed requests" Uji05-RT02.txt |& tee -a Uji05-RT-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji05-RT03.txt |& tee -a Uji05-RT-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji05-RT04.txt |& tee -a Uji05-RT-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji05-RT05.txt |& tee -a Uji05-RT-Failed-requests.txt
sleep 1

grep -w "(mean," Uji05-RT01.txt |& tee -a Uji05-RT-Timeper-requests.txt
sleep 
grep -w "(mean," Uji05-RT02.txt |& tee -a Uji05-RT-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji05-RT03.txt |& tee -a Uji05-RT-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji05-RT04.txt |& tee -a Uji05-RT-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji05-RT05.txt |& tee -a Uji05-RT-Timeper-requests.txt
sleep 1

grep -w "Transfer rate:" Uji05-RT01.txt |& tee -a Uji05-RT-Transfer-rate.txt
sleep 
grep -w "Transfer rate:" Uji05-RT02.txt |& tee -a Uji05-RT-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji05-RT03.txt |& tee -a Uji05-RT-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji05-RT04.txt |& tee -a Uji05-RT-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji05-RT05.txt |& tee -a Uji05-RT-Transfer-rate.txt
sleep 1

grep -w "Requests per second:" Uji05-RT01.txt |& tee Uji05-RT-ReqPerSec.txt
sleep 
grep -w "Requests per second:" Uji05-RT02.txt |& tee -a Uji05-RT-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji05-RT03.txt |& tee -a Uji05-RT-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji05-RT04.txt |& tee -a Uji05-RT-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji05-RT05.txt |& tee -a Uji05-RT-ReqPerSec.txt
sleep 1

grep -w "Total:" Uji05-RT01.txt |& tee Uji05-RT-ReqPerSec.txt
sleep 
grep -w "Total:" Uji05-RT02.txt |& tee -a Uji05-RT-ReqPerSec.txt
sleep 1
grep -w "Total:" Uji05-RT03.txt |& tee -a Uji05-RT-ReqPerSec.txt
sleep 1
grep -w "Total:" Uji05-RT04.txt |& tee -a Uji05-RT-ReqPerSec.txt
sleep 1
grep -w "Total:" Uji05-RT05.txt |& tee -a Uji05-RT-ReqPerSec.txt
sleep 1

echo "Algoritma Fuzy"
grep -w "Complete requests" Uji05-FZ01.txt |& tee -a Uji05-FZ-Complete-requests.txt
sleep 
grep -w "Complete requests" Uji05-FZ02.txt |& tee -a Uji05-FZ-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji05-FZ03.txt |& tee -a Uji05-FZ-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji05-FZ04.txt |& tee -a Uji05-FZ-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji05-FZ05.txt |& tee -a Uji05-FZ-Complete-requests.txt
sleep 1

grep -w "Failed requests" Uji05-FZ01.txt |& tee -a Uji05-FZ-Failed-requests.txt
sleep 
grep -w "Failed requests" Uji05-FZ02.txt |& tee -a Uji05-FZ-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji05-FZ03.txt |& tee -a Uji05-FZ-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji05-FZ04.txt |& tee -a Uji05-FZ-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji05-FZ05.txt |& tee -a Uji05-FZ-Failed-requests.txt
sleep 1

grep -w "(mean," Uji05-FZ01.txt |& tee -a Uji05-FZ-Timeper-requests.txt
sleep 
grep -w "(mean," Uji05-FZ02.txt |& tee -a Uji05-FZ-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji05-FZ03.txt |& tee -a Uji05-FZ-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji05-FZ04.txt |& tee -a Uji05-FZ-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji05-FZ05.txt |& tee -a Uji05-FZ-Timeper-requests.txt
sleep 1

grep -w "Transfer rate:" Uji05-FZ01.txt |& tee -a Uji05-FZ-Transfer-rate.txt
sleep 
grep -w "Transfer rate:" Uji05-FZ02.txt |& tee -a Uji05-FZ-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji05-FZ03.txt |& tee -a Uji05-FZ-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji05-FZ04.txt |& tee -a Uji05-FZ-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji05-FZ05.txt |& tee -a Uji05-FZ-Transfer-rate.txt
sleep 1

grep -w "Requests per second:" Uji05-FZ01.txt |& tee Uji05-FZ-ReqPerSec.txt
sleep 
grep -w "Requests per second:" Uji05-FZ02.txt |& tee -a Uji05-FZ-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji05-FZ03.txt |& tee -a Uji05-FZ-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji05-FZ04.txt |& tee -a Uji05-FZ-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji05-FZ05.txt |& tee -a Uji05-FZ-ReqPerSec.txt
sleep 1

grep -w "Total:" Uji05-FZ01.txt |& tee Uji05-FZ-ReqPerSec.txt
sleep 
grep -w "Total:" Uji05-FZ02.txt |& tee -a Uji05-FZ-ReqPerSec.txt
sleep 1
grep -w "Total:" Uji05-FZ03.txt |& tee -a Uji05-FZ-ReqPerSec.txt
sleep 1
grep -w "Total:" Uji05-FZ04.txt |& tee -a Uji05-FZ-ReqPerSec.txt
sleep 1
grep -w "Total:" Uji05-FZ05.txt |& tee -a Uji05-FZ-ReqPerSec.txt
sleep 1