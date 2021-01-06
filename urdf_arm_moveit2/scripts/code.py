#!/usr/bin/env python   

import rospy
from std_msgs.msg import Float64
from piarm import PiArm
from time import sleep
 

robo = PiArm()
robo.connect('/dev/ttyUSB0') 

rospy.init_node('Arduino', anonymous=True)
rospy.Subscriber("/joints_to_aurdino", Float64,code)        
rospy.spin()	

def code(msg):
   pos=[msg.data[0],msg.data[1],msg.data[2],msg.data[3],msg.data[4],msg.data[5]]

   for command in pos:
    for ID in range(6):
        robo.servoWrite(ID + 1, command[ID], 80)
    sleep(1) 
          
if __name__ == '__main__':
   try:
     code()        
   except rospy.ROSInterruptException:
     pass

