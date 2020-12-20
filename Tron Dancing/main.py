import cv2
import vlc
import time
import numpy as np
from ffpyplayer.player import MediaPlayer

#Rescaling frames to concatenate later
def rescale_frame(frame, percent):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

#Takind audio and video separately to sync them easily
#Audio
sound = MediaPlayer('Audio/audio1.mp3')             
audio_frame, value = sound.get_frame()
#Video
cap = cv2.VideoCapture('Video/video1.mp4')       

#Mask thershold values
#Can be modified for optimum effect
#(Hue,Saturation, Value)
lower = np.array([0,0,150])
upper = np.array([179,60,255])

while (cap.isOpened() == True):

    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)         #Converting frames to HSV format for processing
    
    mask = cv2.inRange(hsv, lower, upper)                #Initialising mask

    final = cv2.bitwise_and(frame, frame, mask = mask)   #Applying mask

    final = rescale_frame(final, percent=75)             #Rescaling processed frame
    frame = rescale_frame(frame, percent=75)             #Rescaling original frame

    concat = np.concatenate((final, frame), axis = 1)    #Displaying "before-after" in a single window

    cv2.imshow('Final', concat)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        sound.close_player()
        cap.release()
        cv2.destroyAllWindows()
        break

cap.release()
sound.close_player()

cv2.destroyAllWindows()