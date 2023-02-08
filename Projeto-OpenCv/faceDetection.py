import numpy as np
import cv2 as cv

face_classifier = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

image = cv.imread('https://media.istockphoto.com/id/1346125184/photo/group-of-successful-multiethnic-business-team.jpg?s=612x612&w=0&k=20&c=5FHgRQZSZed536rHji6w8o5Hco9JVMRe8bpgTa69hE8=')
image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

faces = face_classifier.detectMutiScale(image_gray, 1.3, 5)

for(x, y, w, h) in faces:
    cv.rectangle(image, (x, y), (x+w+h), (255, 0, 0), 2)

cv.imshow('imagem', image)
cv.waitKey(0)
cv.destroyAllWindows()
