#!/usr/bin/env python   

import rospy
from std_msgs.msg import Float32
from serial_comm import SerialComm
from command import Commands
from servo_instruction import SBSServo
from time import sleep  

servo=SBSServo()
servo.connect(port="/dev/ttyS0", baudrate=115200)
ServoID=servo.readID()

rospy.init_node('Arduino', anonymous=True)
rospy.Subscriber("/joints_to_aurdino", Float32,code)        
rospy.spin()	

def code(msg):
   new_pos[6]={msg.data[0],msg.data[1],msg.data[2],msg.data[3],msg.data[4],msg.data[5]}
   i=0
   for i in range(6): 
       servo.servoWrite(ID= i+1, position=new_pos[i], r_time=0, r_speed=900)
       delay(100)   	

          
if __name__ == '__main__':
   try:
     #print(ServoID)
     code()
        
   except rospy.ROSInterruptException:
     pass





##########################################################################################################################################
##from serial_comm import SerialComm
##from command import Commands
##from servo_instruction import SBSServo
##from time import sleep


##if __name__ == "__main__":
##        servo=SBSServo()
##        servo.connect(port="/dev/ttyS0", baudrate=115200)
##        ServoID=servo.readID()
##        print(ServoID) 
##        while 1:
##            servo.writeAngleLimit(ID=1, angleMin=0, angleMax=1000) #set min max angle

##            servo.servoWrite(ID=1, position=0, r_time=0, r_speed=900) #Set to 0 position
##            sleep(3)
##            servo.servoWrite(ID=1, position=999, r_time=0, r_speed=900) #Set to 999 position
##            sleep(3)

##for i in range(6):
  	
    	    ##if new_pos[i]>global_cur_pos[i]:
    	  
##      	    	servo.servoWrite(ID= i, position=new_pos[i], r_time=0, r_speed=900)
     	    	##//global_cur_pos[i]=new_pos[i]        	
    	  
    	    ##else new_pos[i]<global_cur_pos[i]:
    	  
     	    	##rotate_servo(i,new_pos[i],global_cur_pos[i],-1)
      	    	##//global_cur_pos[i]=new_pos[i]
   	  
    	    	##//rotate_servo(i,new_pos[i],global_cur_pos[i],1)
    	    	##//delay(100) 


##   int global_cur_pos[6]={0,0,0,0,0,0}
##   Servo servo1,servo2,servo3,servo4,servo5,servo6

##   def rotate_servo(int servo,int new_pos)

    
##          if (servo==0)
  
##                 //nh.loginfo("Servo1")    
##                 servo.servoWrite(ID=1, position=new_pos[1], r_time=0, r_speed=900)        
##                 delay(10) 
##    		 //servo1.write(new_pos)
                   
  
