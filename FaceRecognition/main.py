import cv2

# Load the image
image_path = "path/to/your/image.jpg"
image = cv2.imread(image_path)

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.3, minNeighbors=5)

# Check if faces were detected
if len(faces) > 0:
    print("Faces detected in the image.")
else:
    print("No faces detected in the image.")
