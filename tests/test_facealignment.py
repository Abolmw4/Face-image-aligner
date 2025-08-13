from pathlib import Path
import unittest
from facealigner.facealignment import align_face
from utils.util import load_json
import cv2
import os
import numpy as np

ACCEPTANLE_FORMATS = ['jpg', 'jpeg', 'png']

class TestFaceAlignment(unittest.TestCase):
    def test_face_align(self):
        conf = load_json()
        directory = conf.get("dataset_dir")
        reuslt_directory = conf.get("result_path")
        for item in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, item)) and item.split('.')[-1] in ACCEPTANLE_FORMATS:
                image = cv2.imread(os.path.join(directory, item))
                try:
                    aligned = align_face(image)
                    cv2.imwrite(os.path.join(reuslt_directory, f"aligned_{item}"), aligned)
                except ValueError as e:
                    print(e)
                    continue
            else:
                continue
    
    def test_performance_test(self):
        conf = load_json()
        directory = conf.get("dataset_dir")
        reuslt_directory = conf.get("result_path")
        number_processed_image: int = 0
        for item in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, item)) and item.split('.')[-1] in ACCEPTANLE_FORMATS:
                image = cv2.imread(os.path.join(directory, item))
                try:
                    aligned = align_face(image)
                    cv2.imwrite(os.path.join(reuslt_directory, f"aligned_{item}"), aligned)
                    number_processed_image += 1
                except ValueError as e:
                    print(e)
                    continue
            else:
                continue
        self.assertEqual(number_processed_image, len(os.listdir(conf.get("result_path"))))
    
    def test_discriminat_aligned_and_not_processed(self):
        conf = load_json()
        directory = conf.get("dataset_dir")
        reuslt_directory = conf.get("result_path")
        for item in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, item)) and item.split('.')[-1] in ACCEPTANLE_FORMATS:
                image = cv2.imread(os.path.join(directory, item))
                try:
                    aligned = align_face(image)
                    cv2.imwrite(os.path.join(reuslt_directory, f"aligned_{item}"), aligned)
                except ValueError as e:
                    print(e)
                    if not os.path.exists(os.path.join(reuslt_directory, "not_processed")):
                        os.mkdir(os.path.join(reuslt_directory, "not_processed"))
                    cv2.imwrite(os.path.join(reuslt_directory, "not_processed", f"{item}"), image)    
                    continue 
            else:
                continue
        
    def test_improve_performance(self):
        conf = load_json()
        directory = conf.get("dataset_dir")
        reuslt_directory = conf.get("result_path")
        for item in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, item)) and item.split('.')[-1] in ACCEPTANLE_FORMATS:
                image = cv2.imread(os.path.join(directory, item))
                if image.size <= 120000:
                    image = cv2.resize(image, (350, 350))
                try:
                    aligned = align_face(image)
                    cv2.imwrite(os.path.join(reuslt_directory, f"aligned_{item}"), aligned)
                except ValueError as e:
                    try:
                        kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
                        image = cv2.filter2D(image, -1, kernel)
                        aligned = align_face(image)
                        cv2.imwrite(os.path.join(reuslt_directory, f"aligned_{item}"), aligned)
                    except ValueError as e:
                        if not os.path.exists(os.path.join(reuslt_directory, "not_processed")):
                            os.mkdir(os.path.join(reuslt_directory, "not_processed"))
                        cv2.imwrite(os.path.join(reuslt_directory, "not_processed", f"{item}"), image)
                        continue
            else:
                continue
    
    def test_request_response_test(self):
        import requests
        IP="0.0.0.0"
        PORT=8081
        result = requests.get('http://'+IP+':'+str(PORT)+'/')
        self.assertEqual(result.status_code, 200)
        
    def test_request_response_post_test(self):
        import requests
        from utils.util import serialize, deserialize
        import json
        IP="0.0.0.0"
        PORT=8081
        iamge = cv2.imread("/home/app/alignment/dataset/2.jpeg")
        pyload = {"image": serialize(iamge)}
        result = requests.post('http://'+IP+':'+str(PORT)+'/align', json=pyload)
        aligned_image = deserialize(result.json()['result'])
        cv2.imshow("result.png", aligned_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
if __name__ == '__main__':
    unittest.main()