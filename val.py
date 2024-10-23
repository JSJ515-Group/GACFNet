import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('E:/gold_yolo/train/exp12/weights/best.pt')
    model.val(data='E:/gold_yolo/ultralytics-main/ultralytics/cfg/datasets/DIOR.yaml',
                split='val',
                save_json=True,# if you need to cal coco metrice
                project='runs/val',
                name='exp',
                )