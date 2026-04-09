# Workflow

## Overview
This project focuses on developing an object detection workflow for an embedded GPU edge device. The selected target platform is the NVIDIA Jetson Nano, and the solution uses a pretrained YOLO model for object detection with Python-based implementation. The workflow is intended to support future TensorRT optimization for improved inference speed on the Jetson platform. The assignment requires a repeatable workflow, prototype, documentation, results, references, and code organization in GitHub. :contentReference[oaicite:0]{index=0}

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

### Step 1: Environment Setup
The Jetson Nano terminal was opened and Python was verified to be available. A project directory was created to organize the workflow files, code, and test data. This established the working environment for the object detection prototype.

### Step 2: Project Folder Setup
A project folder named `object-detection-jetson` was created. Inside this folder, code files and test files were organized so that the workflow could be documented and repeated later.

### Step 3: Camera Testing
A basic camera test script was created and executed on the Jetson Nano to confirm that image input could be accessed. This step was necessary because the final workflow is intended to support live detection from a camera source.

### Step 4: Python Package Preparation
Required Python support was checked on the Jetson device. This included verifying Python execution and preparing the environment for model testing.

### Step 5: YOLO Model Selection
The pretrained YOLOv8n model was selected for the workflow. This model was chosen because it is lightweight and suitable for embedded object detection tasks.

### Step 6: Initial YOLO Testing
The YOLO model was tested successfully on the Jetson Nano using Python. This confirmed that the object detection pipeline was functional and that the model could perform inference on the device.

### Step 7: Prototype Validation
The initial prototype successfully completed the basic workflow up to model execution and detection output. This validated the selected framework and model for the project.

### Step 8: Performance Observation
The model executed successfully on the Jetson Nano, but the inference speed was observed to be slow. This indicates that the current implementation is a baseline version and that further optimization is required for real-time performance.

### Planned Next Steps
- Export the YOLO model to a TensorRT engine
- Run optimized inference using TensorRT
- Measure inference time and FPS
- Compare baseline and optimized performance
- Finalize live camera-based detection workflow

## Software Framework and Model
The following tools and technologies are used in this workflow:

- **Target Platform:** NVIDIA Jetson Nano
- **Programming Language:** Python
- **Object Detection Model:** YOLOv8n
- **Planned Optimization Framework:** TensorRT
- **Supporting Libraries:** OpenCV and Ultralytics YOLO

### Rationale
Python was selected because it allows rapid development and testing. YOLOv8n was selected because it is a lightweight pretrained object detection model suitable for embedded systems. TensorRT was selected as the optimization framework because it is designed to accelerate deep learning inference on NVIDIA hardware. This matches the project requirement for GPU-based accelerated inference on an embedded edge device. :contentReference[oaicite:1]{index=1}

## Results
The workflow was successfully developed up to the baseline model execution stage on the Jetson Nano.

The following outcomes were achieved:
- Python was verified on the Jetson Nano
- A working project folder and code structure were created
- Camera access was tested
- The pretrained YOLOv8n model was selected and executed successfully
- The prototype confirmed that object detection inference could run on the Jetson Nano

Observation:
- The baseline YOLO execution was functional but slow on the Jetson Nano

Discussion:
This result is important because it confirms that the selected object detection workflow is correct and working at a functional level. However, the observed slow performance shows that additional optimization is necessary before the system can be considered suitable for real-time deployment. The next phase of the project will focus on TensorRT-based optimization and performance measurement. This matches the workflow requirement to develop a prototype, document outputs, and analyze results. :contentReference[oaicite:2]{index=2}

## References
- NVIDIA Jetson documentation
- NVIDIA TensorRT documentation
- Ultralytics YOLO documentation
- OpenCV documentation
- Course handout and project instructions

## Code
The code files used for this workflow are stored in the `code/` subfolder of the repository, as required by the project instructions. :contentReference[oaicite:3]{index=3}
