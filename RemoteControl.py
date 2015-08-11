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

        player = self.team.players[0]

        x = player.pose.position.x
        y = player.pose.position.y

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
            x = move_x / 100
            y = move_y / 100
            position = Position(y , -x) # -90 degree

            pose = Pose(position, rotation * -1)

            print(position)

            command = Command.MoveToAndRotate(player, self.team, pose)
            command.is_speed_command = True

            self._send_command(command)



    def on_halt(self):
        self.on_start()

    def on_stop(self):
        self.on_start()




start_game(RemoteControlStrategy)
