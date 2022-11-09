#Drone and Robotics Team_5B

import cv2
from djitellopy import Tello
import numpy
from threading import Thread
from utils import *

def initializeVideo(drone, sceneCounter):
    frame_read = drone.get_frame_read().frame  # video on

    height, width, _ = frame_read.frame.shape
    today = datetime.today().strfttime("%m%d-%H%M%S")
    video = today + sceneCounter + '.mp4'
    write_video = cv2.VideoWriter(video, cv2.VideoWriter_fourcc(*'XVID'), 45, (width, height))

    return frame_read, write_video

def saveVideo(frame_read, write_video, keep_record):
    while keep_record:
        write_video.write(frame_read.frame)
        time.sleep(1 / 45)

def video_stream(drone):
    cv2.namedWindow("Drone Feed")
    frame_read_f = drone.get_frame_read()  # video on
    img = frame_read_f.frame
    cv2.imshow("Drone Feed", img)
    cv2.waitKey(1)


if __name__ == '__main__':

    myDrone = initTello() #initialize

    th1 = Thread(target=video_stream(), args=myDrone) #drone feed on
    th1.start()

    sceneCounter = 1
    keep_record = True

    time.sleep(10)

    while True:

        keyboard = cv2.waitKey(1)
        if keyboard & 0xff == ord('q'): #종료 q
            # myDrone.land()
            # frame_read.stop()
            # myDrone.streamoff()
            exit(0)
            break
        # if keyboard & 0xff == ord('c'): #촬영 시작 c
        #     myDrone.takeoff()
        #     myDrone.move_up(150)
        #     cv2.waitKey(10)
        #     #타겟 인식이 들어갈 자리
        #     waitKey(1)
