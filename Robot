import dbus
import dbus.mainloop.glib
from picamera import PiCamera
from picamera.array import PiRGBArray
import numpy as np
import cv2
import time
import os

os.system('asebamedulla "ser:name=Thymio-II" ')
time.sleep(1)

dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
bus = dbus.SessionBus()
network = dbus.Interface(bus.get_object('ch.epfl.mobots.Aseba','/'), dbus_interface='ch.epfl.mobots.AsebaNetwork')


def motorLeft(target):
    network.SetVariable("thymio-II", "motor.left.target", [target])
    
def speedLeft():  
    return network.GetVariable("thymio-II", "motor.left.speed")[0].real

def motorRight(target):
    network.SetVariable("thymio-II", "motor.right.target", [target])
    
def speedRight():
    return network.GetVariable("thymio-II", "motor.right.speed")[0].real

def proxH():
    prox = []
    for p in network.GetVariable("thymio-II", "prox.horizontal")[0:7]:
        prox.append(p.real)
    return prox

def proxV():
    prox = []
    for p in network.GetVariable("thymio-II", "prox.ground.ambiant")[0:2]:
        prox.append(p.real)
    return prox

def avancer():
    motorLeft(300)
    motorRight(300)

def reculer():
    motorLeft(-300)
    motorRight(-300)
    
def stop():
    motorLeft(0)
    motorRight(0)

def circleL():
    motorRight(100)
    motorLeft(-100)

def circleR():
    motorRight(-100)
    motorLeft(100)

def explore():
    while True:
        p = []
        p = proxH()
        WL = [0.02, 0.01, 0, -0.009, -0.017]
        WR = [-0.017, -0.009, 0, 0.01, 0.02]
        L = 150
        R = 150
        for a in range(5):
            L += p[a]*WL[a]
            R += p[a]*WR[a]
        motorLeft(L)
        motorRight(R)
        time.sleep(0.1)
        
def BasicControl():
    if key == ord('w'):
        avancer()
    if key == ord('a'):
        circleL()
    if key == ord('d'):
        circleR()
    if key == ord('s'):
        reculer()
    if key == ord('x'):
        stop()



    


#CAMERA STUFF
camera = PiCamera()
camera.resolution = (368,240)
camera.framerate = 24
camera.hflip = True
camera.vflip = True
rawCapture = PiRGBArray(camera)
#CAMERA HEATING
time.sleep(0.1)

#VARIABLES 
#TRIANGLE MASK
triangle_mask = np.zeros((240,368), np.uint8)
triangle = np.array([[0,240],[184,120],[368,240]])
#triangle = triangle.reshape((-1,1,2))
cv2.fillPoly(triangle_mask,[triangle],True,255)
#LEFT MASK
upper_left_mask = np.zeros((240,368), np.uint8)
upper_left_vertices = np.array([[0,240],[184,120],[184,180],[92,240]])
cv2.fillPoly(upper_left_mask,[upper_left_vertices],True,255)
#RIGHT MASK
upper_right_mask = np.zeros((240,368), np.uint8)
upper_right_vertices = np.array([[368,240],[276,240],[184,180],[184,120]])
cv2.fillPoly(upper_right_mask,[upper_right_vertices],True,255)
#ClOSE LEFT MASK
lower_left_mask = np.zeros((240,368), np.uint8)
lower_left_vertices = np.array([[184,240],[184,180],[184,240]])
cv2.fillPoly(lower_left_mask,[lower_left_vertices],True,255)
#ClOSE RIGHT MASK
lower_right_mask = np.zeros((240,368), np.uint8)
lower_right_vertices = np.array([[276,240],[184,180],[184,240]])
cv2.fillPoly(lower_right_mask,[lower_right_vertices],True,255)


#speed
LSpeed = 0
RSpeed = 0
DSpeed = 100
auto_steering = False
#menu
show_menu = False
menu_cursor = 0
menu_back = np.zeros((240,368,3), np.uint8)
menu_back.fill(50)
menu_back = cv2.rectangle(menu_back, (20,20), (348,220), (255,0,0), -1)
menu = [['show speed', 1,40,1,0,1,1],['show guide', 1,60,1,0,1,1], ['show edges', 1,80,1,0,1,1],['show fps', 1,100,1,0,1,1],['blur', 7,120,1,1,9,2]]
#show_speed = menu[0][1]
#show_guide = menu[1][1]


#emergency
front_emergency = False
back_emergency = False
ground_emergency = False
emergency = False
interrupt = True
timer = 20
FTime = 0
FPS = 0


for frame in camera.capture_continuous(rawCapture, format='bgr', use_video_port=True):
    STime = time.time()
    image = frame.array
    
    #average command speed
    MSpeed = (RSpeed + LSpeed)/2
    #true speed
    TSpeed = (speedLeft() + speedRight())/2
    #timer
    if timer == 0:
        interrupt = False
    else:
        timer -= 1
    
    
    #PROCESSING
    blur = menu[4][1]
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (blur,blur), 1)
    canny = cv2.Canny(gray, 200, 20)
    processed = canny.copy()

    #menu
    

    #GUI writing
    if menu[2][1]:
        edges = cv2.cvtColor(processed, cv2.COLOR_GRAY2RGB)
        edges[:,:,0]= 0
        edges[:,:,2]= 0
        cv2.addWeighted(edges, 0.2, image, 0.8, 0.0, image)
        
    if menu[0][1]:
        cv2.putText(image, 'Speed: '+str(TSpeed),(0,15), cv2.FONT_HERSHEY_PLAIN,1, (0,255,0),2)
    if menu[3][1]:
        cv2.putText(image, str(FPS),(340,15), cv2.FONT_HERSHEY_PLAIN,1, (0,255,0),2)
    if menu[1][1]:
        cv2.polylines(image,[upper_left_vertices],True,(0,255,0))
        cv2.polylines(image,[upper_right_vertices],True,(0,255,0))
        cv2.polylines(image,[lower_left_vertices],True,(0,255,0))
        cv2.polylines(image,[lower_right_vertices],True,(0,255,0))
        
    
    cv2.polylines(processed,[triangle],True,(255,255,255))

    #menu
    if show_menu:
        for m in menu:
            m[3] = 1
            menu[menu_cursor][3] = 2
        cv2.addWeighted(menu_back, 0.5, image, 0.5, 0, image)
        cv2.putText(image, 'MENU', (165, 35), cv2.FONT_HERSHEY_PLAIN, 1, (20,0,0), 2)
        cv2.rectangle(image,(20,20),(348,40),(225,0,0))
        for m in menu:
            cv2.rectangle(image,(20,m[2]),(348,m[2]+20),(200,0,0), m[3])
            cv2.putText(image, m[0], (25, m[2]+15), cv2.FONT_HERSHEY_PLAIN, 1, (20,0,0), 2)
            cv2.putText(image, str(m[1]), (300, m[2]+15), cv2.FONT_HERSHEY_PLAIN, 1, (20,0,0), 2)
        cv2.rectangle(image,(20,20),(348,220),(225,0,0),2)
        
    if emergency:
        cv2.putText(image, 'EMERGENCY',(140,15), cv2.FONT_HERSHEY_PLAIN,1, (0,0,255),2)
    

    
    
    #STEERING
    #UPPER
    #RIGHT
    upper_right = cv2.bitwise_and(canny, canny, mask=upper_right_mask)
    upper_rightW = cv2.inRange(upper_right,255,255)
    upper_rightN = cv2.countNonZero(upper_rightW)
    #LEFT
    upper_left = cv2.bitwise_and(canny, canny, mask=upper_left_mask)
    upper_leftW = cv2.inRange(upper_left,255,255)
    upper_leftN = cv2.countNonZero(upper_leftW)
    #LOWER
    #RIGHT
    lower_right = cv2.bitwise_and(canny, canny, mask=lower_right_mask)
    lower_rightW = cv2.inRange(lower_right,255,255)
    lower_rightN = cv2.countNonZero(lower_rightW)
    #LEFT
    lower_left = cv2.bitwise_and(canny, canny, mask=lower_left_mask)
    lower_leftW = cv2.inRange(lower_left,255,255)
    lower_leftN = cv2.countNonZero(lower_leftW)
    
    #cv2.putText(image, str(leftN)+' '+str(rightN),(330,15), cv2.FONT_HERSHEY_PLAIN,1, (0,255,0),2)

    #IR SAFETY
    prox = proxH()
    proxF = prox[:4]
    proxB = prox[5:7]
    if max(proxF) > 3000:
        front_emergency = True
        emergency = True
        auto_steering = False
    if max(proxB) > 3000:
        back_emergency = True
        emergency = True
        auto_steering = False

    
    #AUTOSTEERING
    if auto_steering:
        cv2.putText(image, 'AUTOSTEERING',(130,15), cv2.FONT_HERSHEY_PLAIN,1, (255,0,0),2)
        if interrupt:
            if lower_rightN < lower_leftN:
                RSpeed = -50
                LSpeed = 50
                timer = 20
            else:
                RSpeed = 50
                LSpeed = -50
                timer = 20

        else:    
            if upper_leftN < upper_rightN:
                direction = 'left'
                LSpeed = DSpeed - 50
                RSpeed = DSpeed + 50
            elif upper_leftN > upper_rightN:
                direction = 'right'
                LSpeed = DSpeed + 50
                RSpeed = DSpeed - 50
            #elif lower_leftN > 10 or lower_rightN > 10:
            #    interrupt = True
                
            else:
                direction = 'straight'
                LSpeed = DSpeed
                RSpeed = DSpeed
            #cv2.putText(image, direction ,(290,30), cv2.FONT_HERSHEY_PLAIN,1, (0,255,0),2) 
    
    


    #GUI
    cv2.imshow('iTExplorer', image)
    key = cv2.waitKey(1) & 0xFF

    rawCapture.truncate(0)


    #CONTROLS

    if show_menu:
        if key == ord('s'):
            menu_cursor += 1
            if menu_cursor > len(menu)-1:
                menu_cursor = 0
        if key == ord('w'):
            menu_cursor -= 1
            if menu_cursor < 0:
                menu_cursor = len(menu)-1
        if key == ord('d'):
            menu[menu_cursor][1] += menu[menu_cursor][6]
            if menu[menu_cursor][1] > menu[menu_cursor][5]:
                menu[menu_cursor][1] = menu[menu_cursor][4]
        if key == ord('a'):
            menu[menu_cursor][1] -= menu[menu_cursor][6]
            if menu[menu_cursor][1] < menu[menu_cursor][4]:
                menu[menu_cursor][1] = menu[menu_cursor][5]
                
    
    else:
        if auto_steering:
            if key == ord('w'):
                DSpeed += 50
                LSpeed = DSpeed
                RSpeed = DSpeed
            if key == ord('s'):
                DSpeed -= 50
                LSpeed = DSpeed
                RSpeed = DSpeed      
        else:
            if key == ord('w'):
                LSpeed += 100
                RSpeed += 100
            if key == ord('a'):
                LSpeed -= 50
                RSpeed += 50
            if key == ord('d'):
                LSpeed += 50
                RSpeed -= 50
            if key == ord('s'):
                LSpeed -= 100
                RSpeed -= 100

    

    if key == ord('q'):
        break
    if key == ord('x'):
        LSpeed = 0
        RSpeed = 0
        auto_steering = False
        
    if key == ord('y'):
        if auto_steering:
            auto_steering = False
        else:
            auto_steering = True
    if key == ord('m'):
        if show_menu:
            show_menu = False
        else:
            show_menu = True
            
    if key == ord('e'):
        if emergency:
            emergency = False
            front_emergency = False
            back_emergency = False
            ground_emergency = False
        else:
            emergency = True
            LSpeed = 0
            RSpeed = 0
            auto_steering = False

    #Emergency "breaks"
    if front_emergency:
        if MSpeed > 0:
            LSpeed = 0
            RSpeed = 0
    if back_emergency:
        if MSpeed < 0:
            LSpeed = 0
            RSpeed = 0
        
    
            
    motorLeft(LSpeed)
    motorRight(RSpeed)
    FTime = time.time() - STime
    FPS = int(1 / FTime)

stop()        
cv2.destroyAllWindows()

    


    
