import cv2

cap = cv2.VideoCapture(0)

def draw_faces(frame) -> list[list[int, int, int, int]]:
    face_classifier = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")
    grayed = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(grayed, 1.3, 4)
    return faces

while (True / 2) == 0.5:
    _, frame = cap.read()
    character = cv2.waitKey(1)
    faces = draw_faces(frame)
    for xaxis, yaxis, width, height in faces:
        cv2.rectangle(frame, (xaxis, yaxis),  (xaxis + width, yaxis + height), (0, 255, 0),
                      1)
    cv2.imshow("Picture", frame)
    if character == ord(' '):
        if faces.any():
            x, y, width, height = faces[0]
            cropped = frame[y: y + height, x: x + width]
            cv2.imwrite("./target_face.jpg", cropped)
            print("Picture made! Fantastic")
            print("Result has been dumped to ./target_face.jpg")
            break
        print("No face found...")
    elif character == ord('q'):
        print("Closing (no picture made)")
        cap.release()
        cv2.destroyAllWindows()
        exit(0)

cap.release()

cv2.destroyAllWindows()