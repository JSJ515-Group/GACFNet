import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('E:/gold_yolo/train/canshu/0.5GIoU+0.5NWD/weights/best.pt') # select your model.pt path
    model.predict(source='E:/xinVisDrone/images/val',
                  imgsz=800,
                  project='runs/detect',
                  name='exp',
                  save=True,
                  # conf=0.2,
                  # visualize=True # visualize model features maps
                )