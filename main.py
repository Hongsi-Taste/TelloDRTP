#Drone and Robotics Team_5B

import cv2
from djitellopy import Tello
import numpy
from utils import *


if __name__ == '__main__':

    myDrone = initTello() #initialize
    myDrone.streamon() #cam On

    cv2.namedWindow("Camera Feed")
    frame_read = myDrone.get_frame_read() #video on

    time.sleep(10)
    while True:
        img = frame_read.frame
        cv2.imshow("Camera Feed", img)

        keyboard = cv2.waitKey(1)
        if keyboard & 0xff == ord('q'): #종료 q
            myDrone.land()
            frame_read.stop()
            myDrone.streamoff()
            exit(0)
            break
        if keyboard & 0xff == ord('c'): #촬영 시작 c
            myDrone.takeoff()
            myDrone.move_up(150)
            cv2.waitKey(10)
            #타겟 인식이 들어갈 자리