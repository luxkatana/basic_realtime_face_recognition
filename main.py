import cv2
import sys
import face_recognition

def WriteStderr(msg: str):
    sys.stderr.write(msg)
    sys.stderr.flush()

def process_frame(img_todetect):
    img_todetect_locations = face_recognition.face_locations(img_todetect)
    img_todetect_encodings = face_recognition.face_encodings(img_todetect, img_todetect_locations)
    for face_encoding in img_todetect_encodings:
        results = face_recognition.compare_faces([reference_encoding], face_encoding)
        if results[0]:
            print("Found him :D")
            # Draw rectangle on the first element of img_todetect_locations
            x, y, width, height = img_todetect_locations[0]
            cv2.rectangle(img_todetect, (x, y), (x + width, y + height), (0, 255, 0))
            break
    else:
        print("Not found D:")
    return img_todetect
try:
    reference_img = face_recognition.load_image_file("./target_face.jpg")
except FileNotFoundError:
    WriteStderr("target_face.jpg is missing, maybe you forgot to run \"python capture_face_dump.py\"?")
    exit(1)
try:
    cap = cv2.VideoCapture(0)
except: # noqa
    WriteStderr("Unable to find a video device. You'll need a webcam or a camera to run this project D:")
    exit(1)

reference_encoding = face_recognition.face_encodings(reference_img)[0]
while cv2.waitKey(1) != ord('q'):
    _, img_todetect = cap.read()
    modified_frame = process_frame(img_todetect)
    cv2.imshow("Face detection", modified_frame)

cap.release()
cv2.destroyAllWindows()
