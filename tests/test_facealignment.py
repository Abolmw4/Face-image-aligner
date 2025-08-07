from pathlib import Path
import unittest
from facealigner.facealignment import align_face
from utils.util import load_json
import cv2
import os
import numpy as np

class TestFaceAlignment(unittest.TestCase):
    def test_face_align(self):
        conf = load_json()
        directory = conf.get("dataset_dir")
        reuslt_directory = conf.get("result_path")
        for item in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, item)):
                image = cv2.imread(os.path.join(directory, item))
                try:
                    aligned = align_face(image)
                    cv2.imwrite(os.path.join(reuslt_directory, f"aligned_{item}"), aligned)
            # cv2.imwrite("/home/app/alignment/dataset/aligned_result/3_aligned.png", aligned)
                except ValueError as e:
                    print(e)
                    continue
            else:
                continue
    
    
if __name__ == '__main__':
    unittest.main()