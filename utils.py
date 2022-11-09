#Drone and Robotics Team_5B
import cv2
import time
from datetime import datetime
from djitellopy import Tello

def initTello():
    myDrone = Tello()

    myDrone.connect()

    myDrone.for_back_velocity = 5
    myDrone.left_right_velocity = 5
    myDrone.up_down_velocity = 5
    myDrone.yaw_velocity = 5
    myDrone.speed = 5

    print("\n * Drone Battery Percentage : " + str(myDrone.get_battery()) + "%")

    return myDrone

# def resetCoordinate(drone):

def scene1(drone): #장면1, 정면에서 후면으로

    drone.move_up(200)
    drone.go(0,-300,200, 10)
    drone.cw(180)

def scene2(drone): #장면2, 후면에서 정면으로

    drone.move_up(200)
    drone.go(0, 300, 200, 10)
    drone.cw(180)

def scene3(drone): #장면3, 우측 정면에서 후면으로
    drone.move_up(200)
    drone.go(300,300,200, 10)
    drone.cw(90)
    drone.go(300,-300,200,10)
    drone.cw(90)

def scene4(drone): #장면4, 좌측 후면에서 정면으로
    drone.move_up(200)
    drone.go(-300,-300,200,10)
    drone.cw(90)
    drone.go(-300,300,200,10)
    drone.cw(90)

def toInitial(drone):
    drone.move_up(200)
    drone.go(0, 300, 200, 10)


#타겟 초반 설정. 1. 초반에 카메라를 사람앞에 적절한 위치에 두기(4면 / 8면 촬영), 2. 형광조끼, 3. 크롭 이미지 미리 삽입
def getTarget(drone):
    drone.cw(360)

#타겟 찾는 과정
def findTarget(drone):
    drone.ccw(45)
    drone.cw(90)
    drone.ccw(45)

# def recordandSave(img):


