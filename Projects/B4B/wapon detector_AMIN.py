import cv2
import imutils

# Load Cascade
gun_cascade = cv2.CascadeClassifier("cascade.xml")

if gun_cascade.empty():
    print("Error: cascade.xml load nahi hui!")
    exit()

# Open Camera
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Camera open nahi hui!")
    exit()

gun_exist = False

while True:
    ret, frame = camera.read()

    if not ret:
        break

    frame = imutils.resize(frame, width=600)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect Gun
    guns = gun_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=15,
        minSize=(150, 150)
    )

    # Draw Rectangle
    for (x, y, w, h) in guns:
        gun_exist = True
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
        cv2.putText(frame, "Gun Detected", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (0, 0, 255), 2)

    cv2.imshow("Gun Detection", frame)

    # Press Q to Exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()

if gun_exist:
    print("Gun Detected")
else:
    print("No Gun Detected")