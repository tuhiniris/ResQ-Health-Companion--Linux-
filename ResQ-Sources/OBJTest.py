from tensorflow.python.framework.ops import disable_eager_execution
disable_eager_execution()
modelpath = "yolo.h5"
from imageai import Detection
yolo = Detection.ObjectDetection()
yolo.setModelTypeAsYOLOv3()
yolo.setModelPath(modelpath)
yolo.loadModel()
import cv2
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)
while True:
	ret, img = cam.read()
	img, preds = yolo.detectCustomObjectsFromImage(input_image=img, 
					  custom_objects=None, input_type="array",
					  output_type="array",
					  minimum_percentage_probability=70,
					  display_percentage_probability=False,
					  display_object_name=True)                  
	cv2.imshow("", img)
	print(len(preds))
	if (cv2.waitKey(1) & 0xFF == ord("q")) or (cv2.waitKey(1)==27):
		break
		
cam.release()
cv2.destroyAllWindows()

#[{'name': 'cell phone', 'percentage_probability': 87.13493347167969, 'box_points': [188, 28, 334, 328]}, {'name': 'person', 'percentage_probability': 97.69157767295837, 'box_points': [211, 154, 528, 480]}]
