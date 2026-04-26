from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("yolov8n.pt")

# Load image
img = cv2.imread("test.png")

if img is None:
    print("Image not found")
    exit()

# Run detection
results = model(img)

# Draw bounding boxes
annotated = results[0].plot()

# Show result
cv2.imshow("YOLO Detection", annotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
