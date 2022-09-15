import picamera
from time import sleep
import datetime
import os

class Camera:
    def __init__(self):
        self.camera = picamera.PiCamera()
        self.photos_folder = '/home/cits5506/plant_photos'
        if not os.path.exists(self.photos_folder):
            os.makedirs(self.photos_folder)
    
    def save_picture(self):
        # TODO delete older pictures in the folder
        self.camera.capture(f'{self.photos_folder}/{datetime.datetime.now()}.jpg')
    
    def camera_5s_preview(self):
        self.start_video()
        sleep(5)
        self.stop_video()
    
    def start_video(self):
        self.camera.start_preview()
    
    def stop_video(self):
        self.camera.stop_preview()
    
    def timelapse_20s(self):
        for i in range(20):
            self.save_picture()
            sleep(1)

if __name__ == '__main__':
    camera = Camera()
    camera.camera_5s_preview()
