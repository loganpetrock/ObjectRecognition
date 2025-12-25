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

