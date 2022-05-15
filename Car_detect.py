import cv2
import numpy as np


photo = cv2.imread("C:/Users/Kivanc's Account/Downloads/car_2.jpg")
car_classifier = cv2.CascadeClassifier('Car.xml')
classifier_pedestrian = cv2.CascadeClassifier('Pedestrian.xml')


img_gray = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)

if img_gray is None:
    print("The gray image could not be loaded")

Gray_resize = cv2.resize(photo, (1000, 1000))
# cv2.imshow("Test image", Gray_resize)

detect_pedestrian = classifier_pedestrian.detectMultiScale(Gray_resize)


detect_car = car_classifier.detectMultiScale(Gray_resize)

for (x, y, w, h) in detect_pedestrian:
    cv2.rectangle(Gray_resize, (x, y), (x + w, y + h), (0, 0, 255), 4)

    if detect_pedestrian is True:
        cv2.putText(Gray_resize, "Pedestrian Recognition: Active", (25, 25), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=1.0, color=(0, 255, 0), thickness=3)
    else:
        cv2.putText(Gray_resize, "Pedestrian Recognition: Not Active", (25, 25), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=1.0, color=(0, 0, 255), thickness=3)

for (x, y, w, h) in detect_car:
    cv2.rectangle(Gray_resize, (x, y), (x + w, y + h), (0, 225, 0), 4)

    if detect_car is True:
        cv2.putText(Gray_resize, "Car Recognition: Active", (25, 70), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=1.0, color=(0, 255, 0), thickness=3)
    else:
        cv2.putText(Gray_resize, "Car Recognition: Not Active", (25, 70), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=1.0, color=(0, 0, 255), thickness=3)


cv2.imshow("Self Driving Car", Gray_resize)
q = cv2.waitKey()
