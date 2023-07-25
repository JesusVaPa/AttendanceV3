import cv2
import os
import ctypes

def recognize_faces():
    recognized_names = set([])
    dataPath = "Data"
    imagePaths = os.listdir(dataPath)
    #print('imagePaths=', imagePaths)

    user32 = ctypes.windll.user32
    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)

    # Set the desired frame size
    frame_width = 800
    frame_height = 600

    # Calculate the position to center the frame
    x_pos = int((screen_width - frame_width) / 2)
    y_pos = int((screen_height - frame_height) / 2)

    # Resize and move the window to the center
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('frame', frame_width, frame_height)
    cv2.moveWindow('frame', x_pos, y_pos)

    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.read("modelLBPHFace.xml")

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Define a variable to store the recognized name
    recognized_name = ""
    previous_name = ""
    name_changed = False

    while True:
        ret, frame = cap.read()
        if ret == False:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = gray.copy()

        faces = faceClassif.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            visage = auxFrame[y:y + h, x:x + w]
            visage = cv2.resize(visage, (150, 150), interpolation=cv2.INTER_CUBIC)
            result = face_recognizer.predict(visage)

            cv2.putText(frame, '{}'.format(result), (x, y - 5), 1, 1.3, (255, 255, 0), 1, cv2.LINE_AA)

            if result[1] < 70:
                recognized_name = imagePaths[result[0]]  
                cv2.putText(frame, '{}'.format(recognized_name), (x, y - 25), 2, 1.1, (0, 255, 0), 1, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                if recognized_name != previous_name:
                    recognized_names.add(recognized_name)
                    #print(recognized_names)
                    previous_name = recognized_name
                    name_changed = True
            else:
                recognized_name = "Unknown"  
                cv2.putText(frame, recognized_name, (x, y - 20), 2, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

                if name_changed:
                    previous_name = recognized_name
                    name_changed = False

        cv2.imshow('frame', frame)
        k = cv2.waitKey(1)
        
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
    return(recognized_names)