from piarm import PiArm
from time import sleep

robo = PiArm()
robo.connect('/dev/ttyUSB0')
pos = [[472, 497, 306, 478, 484, 570],[471, 499,303 ,739, 486, 571],
        [472 ,499,206 ,739 ,421, 576],
        [579, 499 ,207, 739 ,408, 576],
        [579, 499 ,206, 739 ,533, 576],
        [579, 499 ,206 ,748 ,555, 944],
        [579, 499 ,207 ,748 ,413, 944],
        [498, 499 ,207 ,748 ,420, 944],
        [498, 499 ,208 ,748 ,575, 944],
        [496, 499 ,206 ,749 ,614 ,575]]
for command in pos:
    for ID in range(5):
        robo.servoWrite(ID + 1, command[ID], 80)
    sleep(1)
