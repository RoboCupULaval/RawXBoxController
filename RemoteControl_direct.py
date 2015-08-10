import serial
import jstick
import time
from serial_protocol import serial_protocol


joystick = jstick.Joystick()

ser = serial.Serial('/dev/ttyACM0', 9600)

protocol = serial_protocol()

while True:

    time.sleep(0.5)

    if ser.inWaiting():
        print(ser.readline()[:-1])

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
        x, y = (y , -x) # -90 degree
        print (x,y)
        command = bytearray(protocol.createSpeedCommand(x,y,rotation, 0))
        command[3:7] = command[6:2:-1]
        command[7:11] = command[10:6:-1]
        command[11:15] = command[14:10:-1]
        ser.write(command)

