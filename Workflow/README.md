# Workflow

## Overview
This project focuses on developing an object detection workflow on an embedded GPU device (NVIDIA Jetson Nano). The goal is to run a pre-trained YOLO model to detect objects from images or camera input and display bounding boxes and labels.

The workflow includes environment setup, model testing, performance observation, and optimization planning using ONNX and TensorRT.

---

## System Block Diagram

[Input Source]  
(Camera / Image)

↓  

[Preprocessing]  
(Resize, Normalize)

↓  

[YOLO Model]  
(Object Detection Inference)

↓  

[Post-processing]  
(Bounding Boxes, Labels)

↓  

[Output]  
(Display Detection Results)

---

## Steps

### Step 1: Environment Setup
- Opened terminal on Jetson Nano
- Verified Python installation
- Created project folder for object detection workflow

### Step 2: Camera Testing
- Tested camera using OpenCV to ensure input source is working

### Step 3: Model Selection
- Selected YOLOv8n as the pre-trained object detection model due to its lightweight design

### Step 4: Initial Model Execution
- Ran YOLO model using Python on Jetson Nano
- Verified that object detection works on input image/video

### Step 5: Prototype Development
- Built a basic pipeline for object detection using YOLO and OpenCV
- Displayed detection results with bounding boxes

### Step 6: Performance Observation
- Observed that the model runs successfully but is slow on Jetson Nano
- Identified need for optimization

### Step 7: Optimization Plan (ONNX + TensorRT)
- Planned to convert YOLO model to ONNX format
- Planned to convert ONNX model to TensorRT engine
- Goal is to improve inference speed using GPU acceleration

### Environment Setup

- Installed ultralytics:
  python3 -m pip install ultralytics

- Installed OpenCV:
  sudo apt install python3-opencv

- Installed TensorRT and related libraries

---

## Software Framework and Model Used

- Hardware: NVIDIA Jetson Nano  
- Programming Language: Python  
- Model: YOLOv8n  
- Libraries: OpenCV, Ultralytics YOLO  
- Optimization Tools: ONNX, TensorRT  

---

## Results

The object detection workflow was successfully implemented up to the baseline stage.

- The YOLOv8n model was executed on Jetson Nano
- Object detection worked correctly
- Bounding boxes and labels were displayed

### Observation
The model performance was slow when running the `.pt` model directly.

### Discussion
This indicates that GPU optimization is required. The next step is to convert the model to ONNX and then to TensorRT engine format for faster inference.

---

## References

- Ultralytics YOLO Documentation  
- OpenCV Documentation  
- NVIDIA Jetson Nano Documentation  
- TensorRT Documentation  

---

## Code

All code files used in this workflow are available in the `code/` folder, including:
- YOLO test script
- ONNX export script
- ONNX inference script
