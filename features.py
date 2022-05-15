import cv2
import numpy as np

    if detect_pedestrian is True:
        cv2.putText(Gray_resize, "Pedestrian Recognition: Active", (25, 25), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=1.0, color=(0, 255, 0), thickness=3)
    else:
        cv2.putText(Gray_resize, "Pedestrian Recognition: Not Active", (25, 25), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=1.0, color=(0, 0, 255), thickness=3)
        
            if detect_car is True:
        cv2.putText(Gray_resize, "Car Recognition: Active", (25, 70), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=1.0, color=(0, 255, 0), thickness=3)
    else:
        cv2.putText(Gray_resize, "Car Recognition: Not Active", (25, 70), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=1.0, color=(0, 0, 255), thickness=3)
