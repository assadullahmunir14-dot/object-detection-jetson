# Workflow

## Overview
Object detection system using YOLO model with future deployment on NVIDIA Jetson Nano.
### System Block Diagram

[Input Source]  
(Camera / Image / Video)  

↓  

[Preprocessing]  
(Resize, Normalize)  

↓  

[YOLOv8 Model]  
(Object Detection Inference)  

↓  

[Post-processing]  
(Bounding Boxes, Confidence Scores)  

↓  

[Output]  
(Display Detected Objects)
## Steps
- Installed Python and required libraries
- Installed ultralytics YOLO framework
- Downloaded pretrained YOLOv8n model
- Tested object detection on a sample image
- Verified detection output with bounding boxes and labels
## Software Framework and Model
- Python
- OpenCV
- Ultralytics YOLOv8n model
- (Planned) NVIDIA Jetson Nano
- (Planned) TensorRT for optimization
## Results
The YOLOv8n model was successfully tested using Python with a sample input image.

The model was able to detect objects and generate bounding boxes with class labels and confidence scores.

This initial test confirms that the object detection pipeline is working correctly.

This test was performed as a preliminary validation step. Final implementation, including real-time detection, TensorRT optimization, and performance evaluation, will be carried out on the NVIDIA Jetson Nano platform.

## References
