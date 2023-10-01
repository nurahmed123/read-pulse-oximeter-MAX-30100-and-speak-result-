import time
import max30100
import os

mx30 = max30100.MAX30100()
mx30.enable_spo2()

def read_pulseoxi():
    while 1:
        
        mx30.read_sensor()

        mx30.ir, mx30.red

        hb = int(mx30.ir / 100)
        spo2 = int(mx30.red / 100)
        message = f'espeak -ven+f2 "your pulse rate is {hb} and oxizen level is {spo2}" 2>/dev/null'
        if mx30.ir != mx30.buffer_ir :
            if hb >= 60:
                os.system(message)
                print("hi");
            print("Pulse:",hb);
            
        if mx30.red != mx30.buffer_red:
            print("SPO2:",spo2);
            if spo2 >= 130:
                break

        time.sleep(.5)
read_pulseoxi()