from collections import defaultdict
import cv2
import numpy as np
from ultralytics import YOLO

class PeopleTrackModel():
    def __init__(self) -> None:
        self.model = YOLO('./app/best.pt')
    
    def people_count_by_path(self, img_path):
        img = cv2.imread(img_path)

        results = self.model.track(img, persist=True)
        #annotated_frame = results[0].plot()
        #cv2.imshow("YOLOv8 Tracking", annotated_frame)
        #cv2.waitKey(0)

        people_count = sum(len(result.boxes) for result in results)
        
        return people_count
    
    def people_count_by_img(self, img):

        results = self.model.track(img, persist=True)
        #annotated_frame = results[0].plot()
        #cv2.imshow("YOLOv8 Tracking", annotated_frame)
        #cv2.waitKey(0)

        people_count = sum(len(result.boxes) for result in results)
        
        return people_count