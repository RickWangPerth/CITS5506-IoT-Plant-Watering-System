import picamera
from time import sleep
import datetime
import os


class Camera:
    def __init__(self, photos_folder, keep_num_photos):
        """
        Connects to the Raspberry Pi camera module.
        @param photos_folder: Where to save the photos that are taken.
        @param keep_num_photos: How many photos to keep.
        """
        self.camera = picamera.PiCamera()
        self.photos_folder = photos_folder
        self.keep_num_photos = keep_num_photos
        if not os.path.exists(self.photos_folder):
            os.makedirs(self.photos_folder)

        self.latest_image = None
    
    def save_picture(self):
        """
        Take a save a picture.
        """
        for filename in sorted(os.listdir(self.photos_folder))[:-self.keep_num_photos]:  # Keep the n most recent
            filename_relPath = os.path.join(self.photos_folder,filename)
            os.remove(filename_relPath)

        self.latest_image = f'{self.photos_folder}/{datetime.datetime.now()}.jpg'
        self.camera.capture(self.latest_image)
    
    def camera_5s_preview(self):
        """
        Start a live preview of the camera for 5 seconds.
        Will only work if the Raspberry Pi is connected to a display.
        """
        self.start_video()
        sleep(5)
        self.stop_video()
    
    def start_video(self):
        """
        Starts the camera live preview.
        """
        self.camera.start_preview()
    
    def stop_video(self):
        """
        Stops the camera live preview.
        """
        self.camera.stop_preview()
    
    def timelapse_20s(self):
        """
        Takes a picture every second for 20 seconds.
        """
        for i in range(20):
            self.save_picture()
            sleep(1)

if __name__ == '__main__':
    camera = Camera()
    camera.camera_5s_preview()
