#!/bin/bash
#defining a variable

#parser Apache AB Log

echo "Parser Data Uji06"
echo "Algoritma Round Robin"
grep -w "Complete requests" Uji06-RR01.txt 2>&1 | tee Uji06-RR-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji06-RR02.txt 2>&1 | tee -a Uji06-RR-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji06-RR03.txt 2>&1 | tee -a Uji06-RR-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji06-RR04.txt 2>&1 | tee -a Uji06-RR-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji06-RR05.txt 2>&1 | tee -a Uji06-RR-Complete-requests.txt
sleep 1

grep -w "Failed requests" Uji06-RR01.txt 2>&1 | tee Uji06-RR-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji06-RR02.txt 2>&1 | tee -a Uji06-RR-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji06-RR03.txt 2>&1 | tee -a Uji06-RR-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji06-RR04.txt 2>&1 | tee -a Uji06-RR-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji06-RR05.txt 2>&1 | tee -a Uji06-RR-Failed-requests.txt
sleep 1

grep -w "(mean," Uji06-RR01.txt 2>&1 | tee Uji06-RR-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji06-RR02.txt 2>&1 | tee -a Uji06-RR-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji06-RR03.txt 2>&1 | tee -a Uji06-RR-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji06-RR04.txt 2>&1 | tee -a Uji06-RR-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji06-RR05.txt 2>&1 | tee -a Uji06-RR-Timeper-requests.txt
sleep 1

grep -w "Transfer rate:" Uji06-RR01.txt 2>&1 | tee Uji06-RR-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji06-RR02.txt 2>&1 | tee -a Uji06-RR-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji06-RR03.txt 2>&1 | tee -a Uji06-RR-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji06-RR04.txt 2>&1 | tee -a Uji06-RR-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji06-RR05.txt 2>&1 | tee -a Uji06-RR-Transfer-rate.txt
sleep 1

grep -w "Requests per second:" Uji06-RR01.txt 2>&1 | tee Uji06-RR-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji06-RR02.txt 2>&1 | tee -a Uji06-RR-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji06-RR03.txt 2>&1 | tee -a Uji06-RR-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji06-RR04.txt 2>&1 | tee -a Uji06-RR-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji06-RR05.txt 2>&1 | tee -a Uji06-RR-ReqPerSec.txt
sleep 1

grep -w "Total:" Uji06-RR01.txt 2>&1 | tee Uji06-RR-ResponTime.txt
sleep 1
grep -w "Total:" Uji06-RR02.txt 2>&1 | tee -a Uji06-RR-ResponTime.txt
sleep 1
grep -w "Total:" Uji06-RR03.txt 2>&1 | tee -a Uji06-RR-ResponTime.txt
sleep 1
grep -w "Total:" Uji06-RR04.txt 2>&1 | tee -a Uji06-RR-ResponTime.txt
sleep 1
grep -w "Total:" Uji06-RR05.txt 2>&1 | tee -a Uji06-RR-ResponTime.txt
sleep 1
echo "Algoritma Random"
grep -w "Complete requests" Uji06-RD01.txt 2>&1 | tee Uji06-RD-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji06-RD02.txt 2>&1 | tee -a Uji06-RD-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji06-RD03.txt 2>&1 | tee -a Uji06-RD-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji06-RD04.txt 2>&1 | tee -a Uji06-RD-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji06-RD05.txt 2>&1 | tee -a Uji06-RD-Complete-requests.txt
sleep 1

grep -w "Failed requests" Uji06-RD01.txt 2>&1 | tee Uji06-RD-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji06-RD02.txt 2>&1 | tee -a Uji06-RD-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji06-RD03.txt 2>&1 | tee -a Uji06-RD-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji06-RD04.txt 2>&1 | tee -a Uji06-RD-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji06-RD05.txt 2>&1 | tee -a Uji06-RD-Failed-requests.txt
sleep 1

grep -w "(mean," Uji06-RD01.txt 2>&1 | tee Uji06-RD-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji06-RD02.txt 2>&1 | tee -a Uji06-RD-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji06-RD03.txt 2>&1 | tee -a Uji06-RD-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji06-RD04.txt 2>&1 | tee -a Uji06-RD-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji06-RD05.txt 2>&1 | tee -a Uji06-RD-Timeper-requests.txt
sleep 1

grep -w "Transfer rate:" Uji06-RD01.txt 2>&1 | tee Uji06-RD-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji06-RD02.txt 2>&1 | tee -a Uji06-RD-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji06-RD03.txt 2>&1 | tee -a Uji06-RD-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji06-RD04.txt 2>&1 | tee -a Uji06-RD-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji06-RD05.txt 2>&1 | tee -a Uji06-RD-Transfer-rate.txt
sleep 1

grep -w "Requests per second:" Uji06-RD01.txt 2>&1 | tee Uji06-RD-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji06-RD02.txt 2>&1 | tee -a Uji06-RD-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji06-RD03.txt 2>&1 | tee -a Uji06-RD-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji06-RD04.txt 2>&1 | tee -a Uji06-RD-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji06-RD05.txt 2>&1 | tee -a Uji06-RD-ReqPerSec.txt
sleep 1

grep -w "Total:" Uji06-RD01.txt 2>&1 | tee Uji06-RD-ResponTime.txt
sleep 1
grep -w "Total:" Uji06-RD02.txt 2>&1 | tee -a Uji06-RD-ResponTime.txt
sleep 1
grep -w "Total:" Uji06-RD03.txt 2>&1 | tee -a Uji06-RD-ResponTime.txt
sleep 1
grep -w "Total:" Uji06-RD04.txt 2>&1 | tee -a Uji06-RD-ResponTime.txt
sleep 1
grep -w "Total:" Uji06-RD05.txt 2>&1 | tee -a Uji06-RD-ResponTime.txt
sleep 1

echo "Algoritma Min Respon Time"
grep -w "Complete requests" Uji06-RT01.txt 2>&1 | tee Uji06-RT-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji06-RT02.txt 2>&1 | tee -a Uji06-RT-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji06-RT03.txt 2>&1 | tee -a Uji06-RT-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji06-RT04.txt 2>&1 | tee -a Uji06-RT-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji06-RT05.txt 2>&1 | tee -a Uji06-RT-Complete-requests.txt
sleep 1

grep -w "Failed requests" Uji06-RT01.txt 2>&1 | tee Uji06-RT-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji06-RT02.txt 2>&1 | tee -a Uji06-RT-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji06-RT03.txt 2>&1 | tee -a Uji06-RT-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji06-RT04.txt 2>&1 | tee -a Uji06-RT-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji06-RT05.txt 2>&1 | tee -a Uji06-RT-Failed-requests.txt
sleep 1

grep -w "(mean," Uji06-RT01.txt 2>&1 | tee Uji06-RT-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji06-RT02.txt 2>&1 | tee -a Uji06-RT-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji06-RT03.txt 2>&1 | tee -a Uji06-RT-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji06-RT04.txt 2>&1 | tee -a Uji06-RT-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji06-RT05.txt 2>&1 | tee -a Uji06-RT-Timeper-requests.txt
sleep 1

grep -w "Transfer rate:" Uji06-RT01.txt 2>&1 | tee Uji06-RT-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji06-RT02.txt 2>&1 | tee -a Uji06-RT-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji06-RT03.txt 2>&1 | tee -a Uji06-RT-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji06-RT04.txt 2>&1 | tee -a Uji06-RT-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji06-RT05.txt 2>&1 | tee -a Uji06-RT-Transfer-rate.txt
sleep 1

grep -w "Requests per second:" Uji06-RT01.txt 2>&1 | tee Uji06-RT-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji06-RT02.txt 2>&1 | tee -a Uji06-RT-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji06-RT03.txt 2>&1 | tee -a Uji06-RT-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji06-RT04.txt 2>&1 | tee -a Uji06-RT-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji06-RT05.txt 2>&1 | tee -a Uji06-RT-ReqPerSec.txt
sleep 1

grep -w "Total:" Uji06-RT01.txt 2>&1 | tee Uji06-RT-ResponTime.txt
sleep 1
grep -w "Total:" Uji06-RT02.txt 2>&1 | tee -a Uji06-RT-ResponTime.txt
sleep 1
grep -w "Total:" Uji06-RT03.txt 2>&1 | tee -a Uji06-RT-ResponTime.txt
sleep 1
grep -w "Total:" Uji06-RT04.txt 2>&1 | tee -a Uji06-RT-ResponTime.txt
sleep 1
grep -w "Total:" Uji06-RT05.txt 2>&1 | tee -a Uji06-RT-ResponTime.txt
sleep 1

echo "Algoritma Fuzy"
grep -w "Complete requests" Uji06-FZ01.txt 2>&1 | tee Uji06-FZ-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji06-FZ02.txt 2>&1 | tee -a Uji06-FZ-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji06-FZ03.txt 2>&1 | tee -a Uji06-FZ-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji06-FZ04.txt 2>&1 | tee -a Uji06-FZ-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji06-FZ05.txt 2>&1 | tee -a Uji06-FZ-Complete-requests.txt
sleep 1

grep -w "Failed requests" Uji06-FZ01.txt 2>&1 | tee Uji06-FZ-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji06-FZ02.txt 2>&1 | tee -a Uji06-FZ-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji06-FZ03.txt 2>&1 | tee -a Uji06-FZ-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji06-FZ04.txt 2>&1 | tee -a Uji06-FZ-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji06-FZ05.txt 2>&1 | tee -a Uji06-FZ-Failed-requests.txt
sleep 1

grep -w "(mean," Uji06-FZ01.txt 2>&1 | tee Uji06-FZ-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji06-FZ02.txt 2>&1 | tee -a Uji06-FZ-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji06-FZ03.txt 2>&1 | tee -a Uji06-FZ-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji06-FZ04.txt 2>&1 | tee -a Uji06-FZ-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji06-FZ05.txt 2>&1 | tee -a Uji06-FZ-Timeper-requests.txt
sleep 1

grep -w "Transfer rate:" Uji06-FZ01.txt 2>&1 | tee Uji06-FZ-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji06-FZ02.txt 2>&1 | tee -a Uji06-FZ-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji06-FZ03.txt 2>&1 | tee -a Uji06-FZ-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji06-FZ04.txt 2>&1 | tee -a Uji06-FZ-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji06-FZ05.txt 2>&1 | tee -a Uji06-FZ-Transfer-rate.txt
sleep 1

grep -w "Requests per second:" Uji06-FZ01.txt 2>&1 | tee Uji06-FZ-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji06-FZ02.txt 2>&1 | tee -a Uji06-FZ-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji06-FZ03.txt 2>&1 | tee -a Uji06-FZ-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji06-FZ04.txt 2>&1 | tee -a Uji06-FZ-ReqPerSec.txt
sleep 1
grep -w "Requests per second:" Uji06-FZ05.txt 2>&1 | tee -a Uji06-FZ-ReqPerSec.txt
sleep 1

grep -w "Total:" Uji06-FZ01.txt 2>&1 | tee Uji06-FZ-ResponTime.txt
sleep 1
grep -w "Total:" Uji06-FZ02.txt 2>&1 | tee -a Uji06-FZ-ResponTime.txt
sleep 1
grep -w "Total:" Uji06-FZ03.txt 2>&1 | tee -a Uji06-FZ-ResponTime.txt
sleep 1
grep -w "Total:" Uji06-FZ04.txt 2>&1 | tee -a Uji06-FZ-ResponTime.txt
sleep 1
grep -w "Total:" Uji06-FZ05.txt 2>&1 | tee -a Uji06-FZ-ResponTime.txt
sleep 1