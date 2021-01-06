#!/usr/bin/env python   

import rospy
from std_msgs.msg import Float64
from serial_comm import SerialComm
from command import Commands
from servo_instruction import SBSServo
from time import sleep  

servo=SBSServo()
servo.connect(port="/dev/ttyS0", baudrate=115200)
ServoID=servo.readID()

rospy.init_node('Arduino', anonymous=True)
rospy.Subscriber("/joints_to_aurdino", Float64,code)        
rospy.spin()	

def code(msg):
   new_pos[6]={msg.data[0],msg.data[1],msg.data[2],msg.data[3],msg.data[4],msg.data[5]}
   i=0
   for i in range(6): 
       servo.servoWrite(ID= i+1, position=new_pos[i], r_time=0, r_speed=100)
       delay(100)   	

          
if __name__ == '__main__':
   try:
     #print(ServoID)
     code()
        
   except rospy.ROSInterruptException:
     pass

