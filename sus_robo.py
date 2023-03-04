#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
import serial
import time
port="/dev/ttyUSB0"
baudrate=115200
Serial_Details=(port,baudrate)
serial_port=serial.Serial(Serial_Details[0],Serial_Details[1])	
print("Linear Velocity and Angular Velocity has set into 50% of motor Speed")
def Serial_sender(data):
    speed=122
    value=data.data
    print(value)
    if(value[0]=='a'):
    	print("Forward")
    	msg='a'
    	
    elif(value[0]=='b'):
        print('Backward')
        msg='b'
        
    elif(value[0]=='c'):
        print('Left')
        msg='c'
        
    elif(value[0]=='d'):
        print('Right')
        msg='d'
        
    elif(value[0]=='e'):
        print('Full_left')
        msg='e'
        
    elif(value[0]=='f'):
        print('Full_Right')
        msg='f'
        
    elif(value[0]=='s'):
        print('Stoped')
        msg='g'
        
    elif(value[0]=='i'):
        speed+=10
        if(speed>255):
            speed=255
        msg='t'+str(speed)
        print("Speed Increased",speed)
        
    elif(value[0]=='d'):
        speed-=10
        if(speed<0):
            speed=0
        msg='t'+str(speed)
        
        
        print("Speed Decreased",speed)   
    serial_port.write(msg.encode("utf-8"))    	
def Start_up():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", String, Serial_sender)
    rospy.spin()

if __name__ == '__main__':
    Start_up()
