from utils.util import load_json, caculate_execution_time
import cv2
import dlib
import numpy as np
import os

conf = load_json()


DETECTOR = dlib.get_frontal_face_detector()
PREDICTOR = dlib.shape_predictor(conf.get("model_path"))

@caculate_execution_time
def align_face(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    rects = DETECTOR(gray, 0)
    if len(rects) == 0:
        raise ValueError("No faces detected")
    
    # Get landmarks
    shape = PREDICTOR(gray, rects[0])
    landmarks = np.array([(p.x, p.y) for p in shape.parts()])
    
    # Extract left and right eye corners (landmarks 36, 45)
    left_eye = landmarks[36]
    right_eye = landmarks[45]
    del landmarks
    
    # Calculate eye center and angle
    eye_center = (
        float(left_eye[0] + right_eye[0]) / 2.0,  # x-coordinate as float
        float(left_eye[1] + right_eye[1]) / 2.0   # y-coordinate as float
    )
    
    dy = right_eye[1] - left_eye[1]
    dx = right_eye[0] - left_eye[0]

    angle = np.degrees(np.arctan2(dy, dx))
    
    # Rotate image
    M = cv2.getRotationMatrix2D(eye_center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]), 
                            flags=cv2.INTER_CUBIC, 
                            borderMode=cv2.BORDER_REPLICATE)
    
    return rotated
