#! /usr/bin/env python3
import glob  # for automatic choosing of the serial port
import serial
import jstick
import time
import sys
from serial_protocol import serial_protocol

baudRate = 115200

joystick = jstick.Joystick()

## the previous method of choosing the serial port manually.
#ser = serial.Serial('/dev/ttyUSB0', 115200)
#ser = serial.Serial('/dev/ttyUSB1', 115200)
#ser = serial.Serial('/dev/ttyUSB2', 115200)

## the new all-improved method that is semi-automatic
# PROPOSED ENHANCEMENT: detect which device is the communication tower
ttyListA = glob.glob('/dev/ttyUSB*')
ttyList = ttyListA

if len(ttyList) == 0:
    print('No serial device found! Exiting...')
    exit()
elif len(ttyList) == 1:
    print('One serial device found and selected: ' + str(ttyList[0]))
    ser = serial.Serial(ttyList[0], baudRate)
else:
    print('Multiple serial devices detected, please select a number:')
    inputNumber = None
    while inputNumber not in range(len(ttyList)):
        for i in range(len(ttyList)):
            print(str(i) + ') ' + ttyList[i])
        try:
            inputNumber = int(input())
        except:
            pass
    ser = serial.Serial(ttyList[inputNumber], baudRate)
    print('Serial device selected: ' + str(ttyList[inputNumber]))
time.sleep(1)

protocol = serial_protocol()

while True:

    time.sleep(0.03)

    if ser.inWaiting():
      print(ser.read())

    move_x = joystick.buttons['stick1'].coords[0]
    move_y = joystick.buttons['stick1'].coords[1]*-1

    rotation  = joystick.buttons['stick2'].coords[0]*3 #times 3 for bigger rotation speed
    kick_command = joystick.buttons['a'].value
    dribble_command = joystick.buttons['b'].value

    if (kick_command):
        pass
        #_send_command(Command.Kick(player, 4))

    elif (dribble_command):
        pass
        #self._send_command(Command.Dribble(player, 1))

    else:
        x = move_x
        y = move_y
        x, y = (y*0.5 , -x*0.5) # -90 degree changement de valeur !!! wtg 18 septembre 2015
        print (x,y)
        command = bytearray(protocol.createSpeedCommand(x,y,rotation, 0))
        #command[3:7] = command[6:2:-1]
        #command[7:11] = command[10:6:-1]
        #command[11:15] = command[14:10:-1]
        ser.write(command)

