#!/bin/bash

#15*2=36 request
# Load python toggle start
python3 AppToggleUjiStart.py
for i in {0..15..1}
  do
    ITGSend script_file_telnet -l send_log_file_telnet_$i -L 192.168.53.101 UDP -X 192.168.53.101 UDP -x recv_log_file_telnet_$i      
  done
# Load python toggle stop
python3 AppToggleUjiStop.py
sleep 1

#20*2=40 request
# Load python toggle start
python3 AppToggleUjiStart.py
for i in {0..20..1}
  do
    ITGSend script_file_telnet -l send_log_file_telnet_$i -L 192.168.53.101 UDP -X 192.168.53.101 UDP -x recv_log_file_telnet_$i      
  done
# Load python toggle stop
python3 AppToggleUjiStop.py
sleep 1

#25*2=50 request
# Load python toggle start
python3 AppToggleUjiStart.py
for i in {0..25..1}
  do
    ITGSend script_file_telnet -l send_log_file_telnet_$i -L 192.168.53.101 UDP -X 192.168.53.101 UDP -x recv_log_file_telnet_$i      
  done
# Load python toggle stop
python3 AppToggleUjiStop.py
sleep 1

#30*2=60 request
# Load python toggle start
python3 AppToggleUjiStart.py
for i in {0..30..1}
  do
    ITGSend script_file_telnet -l send_log_file_telnet_$i -L 192.168.53.101 UDP -X 192.168.53.101 UDP -x recv_log_file_telnet_$i      
  done
# Load python toggle stop
python3 AppToggleUjiStop.py
sleep 1

#35*2=70 request
# Load python toggle start
python3 AppToggleUjiStart.py
for i in {0..35..1}
  do
    ITGSend script_file_telnet -l send_log_file_telnet_$i -L 192.168.53.101 UDP -X 192.168.53.101 UDP -x recv_log_file_telnet_$i      
  done
# Load python toggle stop
python3 AppToggleUjiStop.py
sleep 1

#40*2=80 request
# Load python toggle start
python3 AppToggleUjiStart.py
for i in {0..15..1}
  do
    ITGSend script_file_telnet -l send_log_file_telnet_$i -L 192.168.53.101 UDP -X 192.168.53.101 UDP -x recv_log_file_telnet_$i      
  done
# Load python toggle stop
python3 AppToggleUjiStop.py
sleep 1

#15*2=30 request
# Load python toggle start
python3 AppToggleUjiStart.py
for i in {0..15..1}
  do
    ITGSend script_file_voip -l send_log_file_voip_$i -L 192.168.53.101 UDP -X 192.168.53.101 UDP -x recv_log_file_voip_$i    
  done
# Load python toggle stop
python3 AppToggleUjiStop.py
sleep 1

#20*2=40 request
# Load python toggle start
python3 AppToggleUjiStart.py
for i in {0..20..1}
  do
    ITGSend script_file_voip -l send_log_file_voip_$i -L 192.168.53.101 UDP -X 192.168.53.101 UDP -x recv_log_file_voip_$i    
  done
# Load python toggle stop
python3 AppToggleUjiStop.py
sleep 1

#25*2=50 request
# Load python toggle start
python3 AppToggleUjiStart.py
for i in {0..25..1}
  do
    ITGSend script_file_voip -l send_log_file_voip_$i -L 192.168.53.101 UDP -X 192.168.53.101 UDP -x recv_log_file_voip_$i   
  done
# Load python toggle stop
python3 AppToggleUjiStop.py
sleep 1

#30*2=60 request
# Load python toggle start
python3 AppToggleUjiStart.py
for i in {0..30..1}
  do
    ITGSend script_file_voip -l send_log_file_voip_$i -L 192.168.53.101 UDP -X 192.168.53.101 UDP -x recv_log_file_voip_$i    
  done
# Load python toggle stop
python3 AppToggleUjiStop.py
sleep 1

#35*2=70 request
# Load python toggle start
python3 AppToggleUjiStart.py
for i in {0..35..1}
  do
    ITGSend script_file_voip -l send_log_file_voip_$i -L 192.168.53.101 UDP -X 192.168.53.101 UDP -x recv_log_file_voip_$i    
  done
# Load python toggle stop
python3 AppToggleUjiStop.py
sleep 1

#15*2=30 request
# Load python toggle start
python3 AppToggleUjiStart.py
for i in {0..15..1}
  do
    ITGSend script_file_video -l send_log_file_video_$i -L 192.168.53.101 UDP -X 192.168.53.101 UDP -x recv_log_file_video_$i    
  done
# Load python toggle stop
python3 AppToggleUjiStop.py
sleep 1

#20*2=40 request
# Load python toggle start
python3 AppToggleUjiStart.py
for i in {0..29..1}
  do
    ITGSend script_file_video -l send_log_file_video_$i -L 192.168.53.101 UDP -X 192.168.53.101 UDP -x recv_log_file_video_$i        
  done
# Load python toggle stop
python3 AppToggleUjiStop.py
sleep 1

#25*2=50 request
# Load python toggle start
python3 AppToggleUjiStart.py
for i in {0..25..1}
  do
    ITGSend script_file_video -l send_log_file_video_$i -L 192.168.53.101 UDP -X 192.168.53.101 UDP -x recv_log_file_video_$i    
  done
# Load python toggle stop
python3 AppToggleUjiStop.py
sleep 1

#30*2=60 request
# Load python toggle start
python3 AppToggleUjiStart.py
for i in {0..30..1}
  do
    ITGSend script_file_video -l send_log_file_video_$i -L 192.168.53.101 UDP -X 192.168.53.101 UDP -x recv_log_file_video_$i    
  done
# Load python toggle stop
python3 AppToggleUjiStop.py
sleep 1

#35*2=70 request
# Load python toggle start
python3 AppToggleUjiStart.py
for i in {0..35..1}
  do
    ITGSend script_file_video -l send_log_file_video_$i -L 192.168.53.101 UDP -X 192.168.53.101 UDP -x recv_log_file_video_$i    
  done
# Load python toggle stop
python3 AppToggleUjiStop.py
sleep 1