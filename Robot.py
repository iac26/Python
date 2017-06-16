import dbus
import dbus.mainloop.glib
from picamera import PiCamera
from picamera.array import PiRGBArray
import numpy as np
import cv2
import time
import os
import random


os.system('asebamedulla "ser:name=Thymio-II" ')
time.sleep(2)

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
    for p in network.GetVariable("thymio-II", "prox.ground.delta")[0:2]:
        prox.append(p.real)
    return prox

##def avancer():
##    motorLeft(300)
##    motorRight(300)
##
##def reculer():
##    motorLeft(-300)
##    motorRight(-300)
##    
##def stop():
##    motorLeft(0)
##    motorRight(0)
##
##def circleL():
##    motorRight(100)
##    motorLeft(-100)
##
##def circleR():
##    motorRight(-100)
##    motorLeft(100)

##def explore():
##    while True:
##        p = []
##        p = proxH()
##        WL = [0.02, 0.01, 0, -0.009, -0.017]
##        WR = [-0.017, -0.009, 0, 0.01, 0.02]
##        L = 150
##        R = 150
##        for a in range(5):
##            L += p[a]*WL[a]
##            R += p[a]*WR[a]
##        motorLeft(L)
##        motorRight(R)
##        time.sleep(0.1)
##        
##def BasicControl():
##    if key == ord('w'):
##        avancer()
##    if key == ord('a'):
##        circleL()
##    if key == ord('d'):
##        circleR()
##    if key == ord('s'):
##        reculer()
##    if key == ord('x'):
##        stop()



        

    
    


#INITIALISATION DE LA CAMERA
camera = PiCamera()
camera.resolution = (368,240)
camera.framerate = 24
camera.hflip = True
camera.vflip = True
rawCapture = PiRGBArray(camera)
#ON LAISSE LE TEMPS A LA CAMERA DE CHAUFFER
time.sleep(0.1)


#VARIABLES 
#TRIANGLE MASK
triangle_mask = np.zeros((240,368), np.uint8)
triangle = np.array([[0,240],[184,120],[368,240]])
cv2.fillPoly(triangle_mask,[triangle],True,255)
#UPPER LEFT MASK
upper_left_mask = np.zeros((240,368), np.uint8)
upper_left_vertices = np.array([[0,240],[184,120],[184,180],[92,240]])
cv2.fillPoly(upper_left_mask,[upper_left_vertices],True,255)
#UPPER RIGHT MASK
upper_right_mask = np.zeros((240,368), np.uint8)
upper_right_vertices = np.array([[368,240],[276,240],[184,180],[184,120]])
cv2.fillPoly(upper_right_mask,[upper_right_vertices],True,255)
#LOWER LEFT MASK
lower_left_mask = np.zeros((240,368), np.uint8)
lower_left_vertices = np.array([[184,240],[184,180],[184,240]])
cv2.fillPoly(lower_left_mask,[lower_left_vertices],True,255)
#LOWER RIGHT MASK
lower_right_mask = np.zeros((240,368), np.uint8)
lower_right_vertices = np.array([[276,240],[184,180],[184,240]])
cv2.fillPoly(lower_right_mask,[lower_right_vertices],True,255)

#VITESSE
LSpeed = 0
RSpeed = 0
DSpeed = 100
auto_steering = False
#MENU
show_menu = False
menu_cursor = 0
menu_back = np.zeros((240,368,3), np.uint8)
menu_back.fill(50)
menu_back = cv2.rectangle(menu_back, (20,20), (348,220), (255,50,50), -1)
menu_back = cv2.rectangle(menu_back, (20,20), (348,40), (255, 0,0), -1)
menu = [['show speed', 1,40,1,0,1,1],['show guide', 1,60,1,0,1,1], ['show edges', 1,80,1,0,1,1],['show fps', 1,100,1,0,1,1],['blur', 7,120,1,1,9,2], ['clear screen', 0,140,1,0,1,1]]
#QUITTER
quit_confirm_back = np.zeros((240,368,3), np.uint8)
quit_confirm_back.fill(50)
quit_confirm_back = cv2.rectangle(quit_confirm_back, (60,60), (308,180), (255,50,50), -1)
quit_confirm = False
qStart = 0
#EMERGENCE
front_emergency = False
back_emergency = False
ground_emergency = False
emergency = False
#MARCHE ARRIERE
reverse = False
left_reverse = False
right_reverse = False
back_reverse = False
rStart = 0
#IMAGES PAR SECONDE
FTime = 0
FPS = 0
    
    

#ITERATION PRINCIPALE
for frame in camera.capture_continuous(rawCapture, format='bgr', use_video_port=True):
    #debut de l iteration
    STime = time.time()
    image = frame.array
    
    #vitesse (ordonnee par l utilisateur)
    MSpeed = (RSpeed + LSpeed)/2
    #vraie vitesse 
    TSpeed = (speedLeft() + speedRight())/2
    
    
    #filtre de detection de bords
    blur = menu[4][1]
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (blur,blur), 1)
    canny = cv2.Canny(gray, 200, 20)
    processed = canny.copy()

    

    #interface utilisateur
    if not menu[5][1]:#clear screen
        if menu[2][1]:#show edges
            edges = cv2.cvtColor(processed, cv2.COLOR_GRAY2RGB)
            edges[:,:,0]= 0
            edges[:,:,2]= 0
            cv2.addWeighted(edges, 0.2, image, 0.8, 0.0, image)
            
        if menu[0][1]:#show speed
            cv2.putText(image, 'Speed: '+str(TSpeed),(0,15), cv2.FONT_HERSHEY_PLAIN,1, (0,255,0),2)
        if menu[3][1]:#show fps
            cv2.putText(image, str(FPS),(340,15), cv2.FONT_HERSHEY_PLAIN,1, (0,255,0),2)
        if menu[1][1]:#show guide
            cv2.polylines(image,[upper_left_vertices],True,(0,255,0))
            cv2.polylines(image,[upper_right_vertices],True,(0,255,0))
            cv2.polylines(image,[lower_left_vertices],True,(0,255,0))
            cv2.polylines(image,[lower_right_vertices],True,(0,255,0))
        if auto_steering:#autopilote
            cv2.putText(image, 'AUTOSTEERING',(130,15), cv2.FONT_HERSHEY_PLAIN,1, (255,0,0),2)
        if emergency:#emergence
            cv2.putText(image, 'EMERGENCY',(140,15), cv2.FONT_HERSHEY_PLAIN,1, (0,0,255),2)
        if front_emergency:
            cv2.putText(image, 'FRONT',(160,30), cv2.FONT_HERSHEY_PLAIN,1, (0,0,255),2)
        elif back_emergency:
            cv2.putText(image, 'BACK',(165,30), cv2.FONT_HERSHEY_PLAIN,1, (0,0,255),2)
        elif ground_emergency:
            cv2.putText(image, 'GROUND',(155,30), cv2.FONT_HERSHEY_PLAIN,1, (0,0,255),2)

        
    
    #cv2.polylines(processed,[triangle],True,(255,255,255))

    #menu
    if show_menu:
        for m in menu:
            m[3] = 1
            menu[menu_cursor][3] = -1
        cv2.addWeighted(menu_back, 0.5, image, 0.5, 0, image)
        cv2.putText(image, 'MENU', (165, 35), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
        for m in menu:
            cv2.rectangle(image,(20,m[2]),(348,m[2]+20),(200,50,50), m[3])
            cv2.putText(image, m[0], (25, m[2]+15), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
            cv2.putText(image, str(m[1]), (300, m[2]+15), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
        cv2.rectangle(image,(20,20),(348,220),(200,50,50),1)
    #quit    
    if quit_confirm:
        cv2.addWeighted(quit_confirm_back, 0.5, image, 0.5, 0, image)
        cv2.putText(image, 'QUIT?', (165, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
        #cv2.putText(image, 'Q:YES', (110, 150), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
        #cv2.putText(image, 'X:NO', (220, 150), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 2)
        cv2.rectangle(image,(60,60),(308,180),(0,0,0),1)
    if time.time() - qStart > 3:
        quit_confirm = False
        
    

    
    
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
    proxv = proxV()
    proxF = prox[:5]
    proxB = prox[5:7]
    if max(proxF) > 3000:
        front_emergency = True
        emergency = True
        #auto_steering = False
    if max(proxB) > 3000:
        back_emergency = True
        emergency = True
        #auto_steering = False
    if min(proxv) < 100:
        ground_emergency = True
        emergency = True
        auto_steering = False

    
    #AUTOSTEERING
    if auto_steering:
        if reverse: #marche arriere
            if right_reverse:
                if (time.time() - rStart) < 3 :
                    LSpeed = -100
                    RSpeed = -100
                elif (time.time() - rStart) < random.randint(5,9) :
                    LSpeed = -50
                    RSpeed = 50
                else:
                    reverse = False
                    right_reverse = False
                    emergency = False
                    front_emergency = False
                    
            elif left_reverse:
                if (time.time() - rStart) < 3 :
                    LSpeed = -100
                    RSpeed = -100
                elif (time.time() - rStart) < random.randint(5,9) :
                    LSpeed = 50
                    RSpeed = -50
                else:      
                    rStart = 0
                    reverse = False
                    right_reverse = False
                    emergency = False
                    front_emergency = False
##            elif back_reverse:
##                if (time.time() - rStart) < 5 :
##                    LSpeed = -50
##                    RSpeed = -50
##                elif (time.time() - rStart) < 10 :
##                    ground_emergency = False
##                    LSpeed = -50
##                    RSpeed = 50
##                else:      
##                    rStart = 0
##                    reverse = False
##                    back_reverse = False
##                    emergency = False
                    
            

        else:
            #OBSTACLE LOIN
            if upper_leftN < upper_rightN:
                direction = 'left'
                LSpeed = DSpeed - 50
                RSpeed = DSpeed + 50
            #OBSTACLE LOIN
            elif upper_leftN > upper_rightN:
                direction = 'right'
                LSpeed = DSpeed + 50
                RSpeed = DSpeed - 50
            #OBSTACLE PROCHE
            elif lower_leftN > 5 or lower_rightN > 5:
                if lower_rightN < lower_leftN:
                    RSpeed = -100
                    LSpeed = 100
                else:
                    RSpeed = 100
                    LSpeed = -100
            #CONTACT
            elif front_emergency:
                rStart = time.time()
                reverse = True
                if proxF[0]+proxF[1] < prox[3]+proxF[4]:
                    right_reverse = True
                else:
                    left_reverse = True
##            elif ground_emergency:
##                rStart = time.time()
##                reverse = True
##                back_reverse = True
            else:
                direction = 'straight'
                LSpeed = DSpeed
                RSpeed = DSpeed
                #cv2.putText(image, direction ,(290,30), cv2.FONT_HERSHEY_PLAIN,1, (0,255,0),2) 
    
    


    #GUI
    cv2.imshow('Robot', image)
    #cv2.imwrite('stream.jpeg', image)
    key = cv2.waitKey(1) & 0xFF


    
    #debut de la nouvelle image
    rawCapture.truncate(0)
    


    #CONTROLS

    if show_menu: #controles du menu
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
        if auto_steering:#controles de l autopilote
            if key == ord('w'):
                DSpeed += 50
                LSpeed = DSpeed
                RSpeed = DSpeed
            if key == ord('s'):
                DSpeed -= 50
                LSpeed = DSpeed
                RSpeed = DSpeed      
        else:#controles manuels
            if key == ord('w'):
                if not front_emergency and not ground_emergency:
                    LSpeed += 100
                    RSpeed += 100
                else:
                    LSpeed = 0
                    RSpeed = 0
            if key == ord('a'):
                LSpeed -= 50
                RSpeed += 50
            if key == ord('d'):
                LSpeed += 50
                RSpeed -= 50
            if key == ord('s'):
                if not back_emergency:
                    LSpeed -= 100
                    RSpeed -= 100
                else:
                    LSpeed = 0
                    RSpeed = 0

    

    if key == ord('q'): #quitter
        if quit_confirm:
            break
        qStart = time.time()
        quit_confirm = True
    if key == ord('x'): # arreter les moteurs
        LSpeed = 0
        RSpeed = 0
        auto_steering = False
        
    if key == ord('y'): # activer/desactiver l autopilote
        if auto_steering:
            auto_steering = False
        else:
            auto_steering = True
    if key == ord('m'): # ouvrir/fermer le menu
        if show_menu:
            show_menu = False
        else:
            show_menu = True
            
    if key == ord('e'): # arret d urgence
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

    #freins d emergence
    if front_emergency:
        if MSpeed > 0:
            LSpeed = 0
            RSpeed = 0
    if back_emergency:
        if MSpeed < 0:
            LSpeed = 0
            RSpeed = 0
    if ground_emergency:
        if MSpeed > 0:
            LSpeed = 0
            RSpeed = 0
        
    
            
    motorLeft(LSpeed) 
    motorRight(RSpeed)
    # calcul du nombre d images par sec
    FTime = time.time() - STime 
    FPS = int(1 / FTime)


motorLeft(0)
motorRight(0)       
cv2.destroyAllWindows()

    


    
