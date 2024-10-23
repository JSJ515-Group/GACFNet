# GACFNet:A Global Attention Cross-Level Feature Fusion Network for Aerial Image Object Detection

## Introduction

This project introduces GACFNet, a lightweight target detection network for aerial imagery, which proposes a new feature fusion module that enhances the correlation between non-adjacent layers ignored in the FPN-like feature fusion structure, thus compensating for the lost small target information in the FPN-like feature fusion structure. Considering that low-resolution feature maps retain less small-target information, we improved yolov8's backbone to retain more small-target information in low-resolution feature maps. It achieves 69.9 FPS on VisDrone dataset, DIOR dataset and UAVDT dataset, while the accuracy mAP value is higher than the state-of-the-art methods.

![image-20231222094226001](images/image-20231222094226001.png)

## Paper link address:

## Install

```bash
pip install ultralytics
```

## Train

##### `pyhon train.py`

##### or  one-card training

```
yolo detect train  data=E:/GACFNet/ultralytics-main/ultralytics/cfg/datasets/VisDrone.yaml   model=E:/GACFNet/ultralytics-main/ultralytics/GACFNet.yaml  pretrained=E:/GACFNet/ultralytics-main/ultralyticsyolov8s.pt epochs=150 imgsz=800 batch=4 workers=2`
```

## Val

##### `pyhon val.py`

#### or 

```
yolo detect val model=E:/GACFNet/ultralytics-main/ultralytics/runs/train/NGIoU0.5/weights/best.pt data=E:/GACFNet/ultralytics-main/ultralytics/cfg/datasets/VisDrone.yaml
```

## detect

`pyhon detect.py`

##### or 

```
yolo detect predict  model=E:/GACFNet/ultralytics-main/ultralytics/runs/train/NGIoU0.5\weights\best.pt  source=E:/xinVisDrone/images/val save=True  conf=0.5
```

`