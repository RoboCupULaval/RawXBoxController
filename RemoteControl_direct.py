#! /usr/bin/env python3
import glob  # for automatic choosing of the serial port
import serial
import jstick
import time
import sys
from serial_protocol import serial_protocol

baudRate = 115200
speedfactor = 1
joystick = jstick.Joystick()
robotId = 0

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

    move_y = -joystick.buttons['stick1'].coords[0]
    move_x = -joystick.buttons['stick1'].coords[1]
    
    dpad_y = -joystick.buttons['stick3'].coords[0]
    dpad_x = -joystick.buttons['stick3'].coords[1]
	
    max_rotation_freq = 1

    rotation  = -joystick.buttons['stick2'].coords[0]*2*3.1416*max_rotation_freq # Valeur entre -1 et 1. vitesse de rotation envoyé == 0.8 RPM
    kick_command = joystick.buttons['a'].value
    dribble_command = joystick.buttons['b'].value
    speedfactor_command = joystick.buttons['r'].value - joystick.buttons['l'].value
    resetspeedfactor_command = joystick.buttons['y'].value
    if (kick_command):
        print("kick!!")
        command = bytearray(protocol.createKickCommand(10,robotId))
        ser.write(command)
        #_send_command(Command.Kick(player, 4))

    elif (dribble_command):
        print("kick harder!!")
        command = bytearray(protocol.createKickCommand(1000,robotId))
        ser.write(command)
    elif (resetspeedfactor_command):
        print("speedfactor set to 1")
        speedfactor = 1

    max_speed = 1.44
    if (speedfactor > max_speed):
        speedfactor = max_speed
    elif (speedfactor < 0.1):
        speedfactor = 0.1
    elif (speedfactor_command > 0):
        speedfactor = speedfactor + 0.02
    elif (speedfactor_command < 0):
        speedfactor = speedfactor - 0.02

        #self._send_command(Command.Dribble(player, 1))
	# Use dpad if not null
    if dpad_x != 0 or dpad_y != 0:
        x = dpad_x
        y = dpad_y
    else:
        x = move_x
        y = move_y

    velocity_module = (x**2+y**2)**0.5
    if (velocity_module == 0):
        velocity_module = 1

    (x, y) = (speedfactor*x/velocity_module, speedfactor*y/velocity_module)    
    
    print (x,y,rotation)
    command = bytearray(protocol.createSpeedCommand(x,y,rotation, robotId))
    #command[3:7] = command[6:2:-1]
    #command[7:11] = command[10:6:-1]
    #command[11:15] = command[14:10:-1]
    ser.write(command)

