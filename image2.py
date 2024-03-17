import numpy as np
import cv2
img = cv2.imread('../images/typewriter.jpg') # reads the image in the form of numpy array
print(img.shape)

rows = open('../model/synset_words.txt').read().strip().split("\n") # read the synset_words.txt file

classes = [r[r.find('')+1:] for r in rows]# get the class names

net = cv2.dnn.readNetFromCaffe('../model/bvlc_googlenet.prototxt', '../model/bvlc_googlenet.caffemodel') # read the model

blob = cv2.dnn.blobFromImage(img, 1, (224, 224))# convert the image to blob

net.setInput(blob) # set the input

outp = net.forward() # get the output
#print(outp)
idx = np.argsort(outp[0])[::-1][:5]     # get the top 5 classes

for (i, idx_class) in enumerate(idx): # print the top 5 classes
    print('{}. {} ({}): Probability {:.3}%' .format(i+1, classes[idx_class], idx_class , outp[0][idx_class]*100)) # print the top 5 classes
# for (i,c) in enumerate(classes):
#     if i == 4:
#         break
#     print(i,c)

cv2.imshow('Image', img) # display the image
cv2.waitKey(0)  # waits for any key to be pressed
cv2.destroyAllWindows()     # closes the window
