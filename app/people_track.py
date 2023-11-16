from collections import defaultdict
import cv2
import numpy as np
from ultralytics import YOLO
from PIL import Image
import io

class PeopleTrackModel():
    def __init__(self) -> None:
        self.model = YOLO('./app/best.pt')
        self.cap = cv2.VideoCapture(0)

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

    def video_cap(self):

        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            
            results = self.model.track(frame, conf=0.5)

            image_np = results[0].plot()
            # Преобразование кадра в формат base64
            ret, buffer = cv2.imencode('.jpg', image_np)
            frame = buffer.tobytes()
            
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        cap.release()
        cv2.destroyAllWindows()

    def get_image(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break
            
            results = self.model.track(frame)

            image_np = results[0].plot()
            break

        return image_np
