import cv2
import os
import numpy as np
from src.FacialRecognition import recognize_faces

def train_model():
	dataPath = "Data"
	peopleList = os.listdir(dataPath)
	print('Students: ', peopleList)

	labels = []
	facesData = []
	label = 0

	for nameDir in peopleList:
		personPath = dataPath + '/' + nameDir
		print('Reading pictures')

		for fileName in os.listdir(personPath):
			print('User: ', nameDir + '/' + fileName)
			labels.append(label)
			facesData.append(cv2.imread(personPath+'/'+fileName,0))
			
		label = label + 1

	face_recognizer = cv2.face.LBPHFaceRecognizer_create()

	print("Training...")

	face_recognizer.train(facesData, np.array(labels))

	face_recognizer.write('modelLBPHFace.xml')
	print("Model saved.")

	names = recognize_faces()
	return(names)