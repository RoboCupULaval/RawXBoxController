import math

from PythonFramework.Command import Command
from PythonFramework.Strategy.Strategy import Strategy
from PythonFramework.Util.Position import Position
import jstick
from PythonFramework.Util.Pose import Pose
from PythonFramework.Framework import start_game

class RemoteControlStrategy(Strategy):
    def __init__(self, field, referee, team, opponent_team):
        super().__init__(field, referee, team, opponent_team)
        self.joystick = jstick.Joystick()

    def on_start(self):

        player = self.team.players[4]

        x = player.pose.position.x
        y = player.pose.position.y
        
        ball = self.field.ball.position

        #print ("player " + str(player.pose.position))
        #print ("Ball " + str(ball))

        move_x = self.joystick.buttons['stick1'].coords[0]
        move_y = self.joystick.buttons['stick1'].coords[1]*-1

        #rotation = math.atan2(self.joystick.buttons['stick2'].coords[1]*-1, self.joystick.buttons['stick2'].coords[0])
        #Probably going to be used when using 1 stick for x/y movements

        rotation  =  self.joystick.buttons['stick2'].coords[0]*3 #times 3 for bigger rotation speed

        kick_command = self.joystick.buttons['a'].value
        dribble_command = self.joystick.buttons['b'].value

        if (kick_command):
            self._send_command(Command.Kick(player, 4))

        elif (dribble_command):
            self._send_command(Command.Dribble(player, 1))

        else:
            #x = move_x
            #y = move_y
            
            #x, y, theta = convertPositionToSpeed(player, ball.x ,ball.y, rotation * -1)
            
            #pose = Pose(position, rotation * -1)
            
            position = Position(ball.x, ball.y)

            #print(current_theta)

            command = Command.MoveTo(player, self.team, position)
            self._send_command(command)
            #command.is_speed_command = True
            
            #print ("command " + str((x,y)))

            #command = bytearray(protocol.createSpeedCommand(x*2,y*2 ,0, 0))
            #ser.write(command)


    def on_halt(self):
        self.on_start()

    def on_stop(self):
        self.on_start()


start_game(RemoteControlStrategy)
