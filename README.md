# Object Detection Inference on Jetson Nano

## Problem Statement
The goal of this project is to develop a workflow for object detection inference on an embedded GPU edge device. The system must process camera input, detect objects in real time, and display bounding boxes and class labels. The workflow should demonstrate how GPU acceleration improves performance for AI-based image processing tasks.

---

## Possible Hardware, Frameworks, Libraries, and Models

### Hardware Options
- NVIDIA Jetson Nano
- GPU-enabled desktop/laptop

### Software Frameworks & Libraries
- Python
- OpenCV (for image/video processing)
- Ultralytics YOLO (object detection model)
- ONNX Runtime
- TensorRT (for GPU optimization)

### Pre-trained Models Considered
- YOLOv8n
- YOLOv5n

---

## Selected Solution

- **Hardware:** NVIDIA Jetson Nano  
- **Programming Language:** Python  
- **Model:** YOLOv8n (lightweight version)  
- **Frameworks:** OpenCV + Ultralytics YOLO  
- **Optimization Plan:** ONNX → TensorRT  

---

## Rationale

The Jetson Nano was selected because it is an embedded device with GPU acceleration, making it suitable for edge AI applications. YOLOv8n was chosen because it is a lightweight model that can run on resource-constrained hardware.

Python and OpenCV were selected due to ease of integration with camera input and visualization. ONNX and TensorRT are included in the workflow to optimize inference performance and reduce execution time, which is critical for real-time object detection.

---

## Connection to Parallel Computing

Object detection is a parallel computing problem because operations are performed on large numbers of pixels simultaneously. GPU acceleration allows these computations to be processed in parallel, significantly improving performance compared to CPU-based execution.
