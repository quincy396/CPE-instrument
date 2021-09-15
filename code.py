from adafruit_circuitplayground import cp
import time

on = False
n = [1,1,1,1]

if cp.button_a:
        on = not on
if on:
        cp.play_file("0.wav")
while True:
    #cp.play_file("0.wav")

    if cp.touch_A1:
        cp.play_file("1.wav")
    if cp.touch_A2:
        cp.play_file("2.wav")
    if cp.touch_A3:
        cp.play_file("3.wav")
    if cp.touch_A4:
        cp.play_file("4-"+str(n[0]) +".wav")
        n[0] +=1
    if cp.touch_A5:
        cp.play_file("5-"+str(n[1]) +".wav")
        n[1] +=1
    if cp.touch_A6:
        cp.play_file("6-"+str(n[2]) +".wav")
        n[2] +=1
    if cp.touch_A7:
        cp.play_file("7-"+str(n[3]) +".wav")
        n[3] +=1
    for i in [0,1,2,3]:
        if n[i]==4:
            n[i] = 1
    

    
