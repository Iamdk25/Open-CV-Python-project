import numpy as np
import cv2

cap = cv2.VideoCapture('../images/shore.mov') # reads the video

rows = open('../model/synset_words.txt').read().strip().split("\n") # read the synset_words.txt file

classes = [r[r.find('')+1:] for r in rows]# get the class names

net = cv2.dnn.readNetFromCaffe('../model/bvlc_googlenet.prototxt', '../model/bvlc_googlenet.caffemodel') # read the model

if cap.isOpened() == False: # checks if the video is opened
    print('Cannot open file or video stream')

while True:
    ret, frame = cap.read() # reads the video

    blob = cv2.dnn.blobFromImage(frame, 1, (224, 224))# convert the image to blob

    net.setInput(blob) # set the input

    outp = net.forward() # get the output
    
    r = 1
    
    for i in np.argsort(outp[0])[::-1][:5]:     # get the top 5 classes
        txt = ('"%s" probability "%.3f"' % (classes[i], outp[0][i]*100)) # print the top 5 classes
        cv2.putText(frame, txt, (0, 25 + r*40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0 , 0), 2)
        r+=1

        if ret == True:
            cv2.imshow('Frame', frame)  # displays the video

            if cv2.waitKey(25) & 0xFF == 27:    # waits for any key to be pressed
                break
            else:
                break

cap.release(0)    # closes the video
cv2.destroyAllWindows()
