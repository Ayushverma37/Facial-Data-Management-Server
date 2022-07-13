import face_recognition
import numpy as np

class faceRecognition:
    
    # returns encoding as a NumPy array for an image file provided as a parameter
    def give_encoding(self, img_file):
        img = face_recognition.load_image_file(img_file)
        known_face_encodings = face_recognition.face_encodings(img)
        return known_face_encodings
    
    #  returns list of distance between source and target image encodings by calculating the euclidean distance between them
    def img_distance(self, source, target):
        dist=face_recognition.face_distance(source, target)
        return dist
    
    