import cv2 as cv
import os
import datetime, time
import imutils

class Camera():
    
    # varible initilised under class
    nof_people = 0
    
    def __init__(self, webcam):
        
        # Prepare camera.
        self.cam = cv.VideoCapture(webcam, cv.CAP_DSHOW)
        
        # Path for saving images and Videos.
        self.image_path = "C:\\Users\\Developer_Inside\\Desktop\\Project\\images"
        self.processed_image_path = "C:\\Users\\Developer_Inside\\Desktop\\Project\\Processed_image"
        self.video_path = "C:\\Users\\Developer_Inside\\Desktop\\Project\\Video"
        
        # Standard Video Dimensions Sizes
        self.STD_DIMENSIONS =  {
        "360p": (640, 360),
        "480p": (640, 480),
        "540p": (960, 540),
        "720p": (1280, 720),
        "1080p": (1920, 1080),
        "4k": (3840, 2160),
        }
    
    # grab resolution dimensions and set video capture to it.
    def get_dims(self, resolution):
        
        if resolution in self.STD_DIMENSIONS:
            width, height = self.STD_DIMENSIONS[resolution]
            self.cam.set(3, width)
            self.cam.set(4, height)
        
        else:
            print("ERROR : Please set standard camera resolution.")
        
    def imageProcess(self):
        
        while True:
            # Reading and showing the camera view.
            result, frame = self.cam.read()
            # cv.imshow("Camera_Live", frame)
            self.wait = cv.waitKey(1)
            
        
        # Based on input capturing images and storing.
            if result:
                
                # Fetching date and time.
                curr_datetime = datetime.datetime.now().strftime('date_%Y-%m-%d_time_ %H-%M-%S')
                
                # Setting file name format.
                image_name = "Image_{}.png".format(curr_datetime)
                
                # Saving the image in specified memory location.
                image = cv.imwrite(os.path.join(self.image_path , image_name), frame)
                
                # Name of image which is captured and saved.
                print("{} Saved..!".format(image_name))
                
                '''
                Image processing
                ================
                '''
                
                hog = cv.HOGDescriptor()
                hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())
                
                image_read = cv.imread(os.path.join(self.image_path , image_name))
                # image_read = cv.imread("people.png") # for testing
                
                # Detecting all humans
                (self.humans, _) = hog.detectMultiScale(image_read, winStride=(5, 5), padding=(3, 3), scale=1.21)
                
                # getting no. of human detected
                print('Human Detected : ', len(self.humans))
                
                self.nof_people = len(self.humans)
                
                # Drawing the rectangle regions
                for (x, y, w, h) in self.humans:
                    cv.rectangle(image_read, (x, y), (x + w, y + h), (0, 0, 255), 3)
                
                # Naming for processed image
                processed_image_name = "Image_{}.png".format(curr_datetime)
                
                # Resizing the Image
                image_resize = imutils.resize(image_read, width=min(720, image_read.shape[1]))
                
                # Saving processed image
                img_processed = cv.imwrite(os.path.join(self.processed_image_path , processed_image_name), image_resize)
                
                print("{} Processed image saved..!".format(processed_image_name))
                # cv.imshow("Image processed", image_resize)
                # cv.waitKey(1000)
                cv.destroyAllWindows()
                
                # Deleting images from directory
                os.remove(os.path.join(self.image_path, image_name))
                os.remove(os.path.join(self.processed_image_path, processed_image_name))
                                    
                break
            
            else:
                break
            
                     
    def videoCapture(self):
        
        if self.nof_people > 0:
        
            frams_sec = 16
            fourcc = cv.VideoWriter_fourcc(*'XVID')
            curr_datetime = datetime.datetime.now().strftime('date_%Y-%m-%d_time_ %H-%M-%S')
            video_name = ("Video_{}.avi".format(curr_datetime))
        
            video_clip = cv.VideoWriter(os.path.join(self.video_path, video_name), fourcc, frams_sec, self.STD_DIMENSIONS["360p"])        
            capture_duration = 11
            startTime = time.time()
            timeElapsed = startTime - time.time()
            print("Video is recording..")
        
            while self.cam.isOpened():
            
                # Reading and showing the camera view.
                if ((time.time() - startTime) < capture_duration):
                
                    result, video = self.cam.read()
                
                    if result:
                    
                        video_clip.write(video)
                        cv.imshow("Live_Video", video)
                        cv.waitKey(1)
                else:
                    break
            print("Video recording finished.")
            cv.destroyAllWindows()
           
cam1 = Camera(0)
               
if __name__ == "__main__":
    
    while True:
        
        run = (input('Please press "r" or "R" to run : '))
        
        if len(run) == 1:
            
            if ord(run) == 114 or ord(run) == 82:
                
                # cv.waitKey(5000) # Witing for 5 secs to test the img process model.
                cam1.get_dims("480p")
                cam1.imageProcess()
                cam1.get_dims("360p")
                cam1.videoCapture()
                
            else:
                print("Invalid Key..!")
        else:
            print("invalid key..!")