<img width="640" height="511" alt="example" src="https://github.com/user-attachments/assets/f6386f02-8c3a-44b0-9d2c-6340f830176f" />


# Overview

**Real-time computer vision system** for **AMD GPUs** to identify elements of my photography setup. Uses **ONNX Runtime** to ensure stability on **RDNA2 architecture**.

## Tech Stack

- **Model:** YOLO11s (Ultralytics)
- **Acceleration:** DirectML (`onnxruntime-directml`)
- **Language:** Python 3.12
- **Hardware:** AMD GPUs with RDNA2


## Results

- **Inference Speed:** ~15FPS at 1080p (RDNA2 accelerated)
- **Confidence:** 90%+ mAP on individual components (even in clustered scenes)

