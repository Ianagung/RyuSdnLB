#!/bin/bash
#defining a variable

#parser Apache AB Log

echo "Parser Data Uji01"
echo "Algoritma Round Robin"
grep -w "Complete requests" Uji01-RR01.txt |& tee -a Uji01-RR-Complete-requests.txt
sleep 
grep -w "Complete requests" Uji01-RR02.txt |& tee -a Uji01-RR-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji01-RR03.txt |& tee -a Uji01-RR-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji01-RR04.txt |& tee -a Uji01-RR-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji01-RR05.txt |& tee -a Uji01-RR-Complete-requests.txt
sleep 1

grep -w "Failed requests" Uji01-RR01.txt |& tee -a Uji01-RR-Failed-requests.txt
sleep 
grep -w "Failed requests" Uji01-RR02.txt |& tee -a Uji01-RR-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji01-RR03.txt |& tee -a Uji01-RR-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji01-RR04.txt |& tee -a Uji01-RR-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji01-RR05.txt |& tee -a Uji01-RR-Failed-requests.txt
sleep 1

grep -w "(mean," Uji01-RR01.txt |& tee -a Uji01-RR-Timeper-requests.txt
sleep 
grep -w "(mean," Uji01-RR02.txt |& tee -a Uji01-RR-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji01-RR03.txt |& tee -a Uji01-RR-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji01-RR04.txt |& tee -a Uji01-RR-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji01-RR05.txt |& tee -a Uji01-RR-Timeper-requests.txt
sleep 1

grep -w "Transfer rate:" Uji01-RR01.txt |& tee -a Uji01-RR-Transfer-rate.txt
sleep 
grep -w "Transfer rate:" Uji01-RR02.txt |& tee -a Uji01-RR-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji01-RR03.txt |& tee -a Uji01-RR-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji01-RR04.txt |& tee -a Uji01-RR-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji01-RR05.txt |& tee -a Uji01-RR-Transfer-rate.txt
sleep 1
echo "Algoritma Random"
grep -w "Complete requests" Uji01-Rd01.txt |& tee -a Uji01-Rd-Complete-requests.txt
sleep 
grep -w "Complete requests" Uji01-Rd02.txt |& tee -a Uji01-Rd-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji01-Rd03.txt |& tee -a Uji01-Rd-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji01-Rd04.txt |& tee -a Uji01-Rd-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji01-Rd05.txt |& tee -a Uji01-Rd-Complete-requests.txt
sleep 1

grep -w "Failed requests" Uji01-Rd01.txt |& tee -a Uji01-Rd-Failed-requests.txt
sleep 
grep -w "Failed requests" Uji01-Rd02.txt |& tee -a Uji01-Rd-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji01-Rd03.txt |& tee -a Uji01-Rd-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji01-Rd04.txt |& tee -a Uji01-Rd-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji01-Rd05.txt |& tee -a Uji01-Rd-Failed-requests.txt
sleep 1

grep -w "(mean," Uji01-Rd01.txt |& tee -a Uji01-Rd-Timeper-requests.txt
sleep 
grep -w "(mean," Uji01-Rd02.txt |& tee -a Uji01-Rd-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji01-Rd03.txt |& tee -a Uji01-Rd-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji01-Rd04.txt |& tee -a Uji01-Rd-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji01-Rd05.txt |& tee -a Uji01-Rd-Timeper-requests.txt
sleep 1

grep -w "Transfer rate:" Uji01-Rd01.txt |& tee -a Uji01-Rd-Transfer-rate.txt
sleep 
grep -w "Transfer rate:" Uji01-Rd02.txt |& tee -a Uji01-Rd-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji01-Rd03.txt |& tee -a Uji01-Rd-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji01-Rd04.txt |& tee -a Uji01-Rd-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji01-Rd05.txt |& tee -a Uji01-Rd-Transfer-rate.txt
sleep 1

echo "Algoritma Min Respon Time"
grep -w "Complete requests" Uji01-RT01.txt |& tee -a Uji01-RT-Complete-requests.txt
sleep 
grep -w "Complete requests" Uji01-RT02.txt |& tee -a Uji01-RT-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji01-RT03.txt |& tee -a Uji01-RT-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji01-RT04.txt |& tee -a Uji01-RT-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji01-RT05.txt |& tee -a Uji01-RT-Complete-requests.txt
sleep 1

grep -w "Failed requests" Uji01-RT01.txt |& tee -a Uji01-RT-Failed-requests.txt
sleep 
grep -w "Failed requests" Uji01-RT02.txt |& tee -a Uji01-RT-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji01-RT03.txt |& tee -a Uji01-RT-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji01-RT04.txt |& tee -a Uji01-RT-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji01-RT05.txt |& tee -a Uji01-RT-Failed-requests.txt
sleep 1

grep -w "(mean," Uji01-RT01.txt |& tee -a Uji01-RT-Timeper-requests.txt
sleep 
grep -w "(mean," Uji01-RT02.txt |& tee -a Uji01-RT-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji01-RT03.txt |& tee -a Uji01-RT-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji01-RT04.txt |& tee -a Uji01-RT-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji01-RT05.txt |& tee -a Uji01-RT-Timeper-requests.txt
sleep 1

grep -w "Transfer rate:" Uji01-RT01.txt |& tee -a Uji01-RT-Transfer-rate.txt
sleep 
grep -w "Transfer rate:" Uji01-RT02.txt |& tee -a Uji01-RT-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji01-RT03.txt |& tee -a Uji01-RT-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji01-RT04.txt |& tee -a Uji01-RT-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji01-RT05.txt |& tee -a Uji01-RT-Transfer-rate.txt
sleep 1
echo "Algoritma Fuzy"
grep -w "Complete requests" Uji01-FZ01.txt |& tee -a Uji01-FZ-Complete-requests.txt
sleep 
grep -w "Complete requests" Uji01-FZ02.txt |& tee -a Uji01-FZ-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji01-FZ03.txt |& tee -a Uji01-FZ-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji01-FZ04.txt |& tee -a Uji01-FZ-Complete-requests.txt
sleep 1
grep -w "Complete requests" Uji01-FZ05.txt |& tee -a Uji01-FZ-Complete-requests.txt
sleep 1

grep -w "Failed requests" Uji01-FZ01.txt |& tee -a Uji01-FZ-Failed-requests.txt
sleep 
grep -w "Failed requests" Uji01-FZ02.txt |& tee -a Uji01-FZ-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji01-FZ03.txt |& tee -a Uji01-FZ-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji01-FZ04.txt |& tee -a Uji01-FZ-Failed-requests.txt
sleep 1
grep -w "Failed requests" Uji01-FZ05.txt |& tee -a Uji01-FZ-Failed-requests.txt
sleep 1

grep -w "(mean," Uji01-FZ01.txt |& tee -a Uji01-FZ-Timeper-requests.txt
sleep 
grep -w "(mean," Uji01-FZ02.txt |& tee -a Uji01-FZ-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji01-FZ03.txt |& tee -a Uji01-FZ-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji01-FZ04.txt |& tee -a Uji01-FZ-Timeper-requests.txt
sleep 1
grep -w "(mean," Uji01-FZ05.txt |& tee -a Uji01-FZ-Timeper-requests.txt
sleep 1

grep -w "Transfer rate:" Uji01-FZ01.txt |& tee -a Uji01-FZ-Transfer-rate.txt
sleep 
grep -w "Transfer rate:" Uji01-FZ02.txt |& tee -a Uji01-FZ-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji01-FZ03.txt |& tee -a Uji01-FZ-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji01-FZ04.txt |& tee -a Uji01-FZ-Transfer-rate.txt
sleep 1
grep -w "Transfer rate:" Uji01-FZ05.txt |& tee -a Uji01-FZ-Transfer-rate.txt
sleep 1