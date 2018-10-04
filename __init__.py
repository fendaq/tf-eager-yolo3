# -*- coding: utf-8 -*-

import os

PKG_ROOT = os.path.dirname(__file__)
PROJECT_ROOT = os.path.dirname(PKG_ROOT)
DARKNET_WEIGHTS = os.path.join(os.path.dirname(PROJECT_ROOT), "dataset", "yolo", "darknet53_conv.weights")    
YOLOV3_WEIGHTS = os.path.join(os.path.dirname(PROJECT_ROOT), "dataset", "yolo", "yolov3.weights")    
YOLOV3_H5 = os.path.join(os.path.dirname(PROJECT_ROOT), "dataset", "yolo", "yolov3.h5")    

