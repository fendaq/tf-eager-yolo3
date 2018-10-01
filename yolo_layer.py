# -*- coding: utf-8 -*-

import tensorflow as tf
import numpy as np


def reshape_y_pred(y_pred):
    y_pred_reshaped = y_pred.reshape(y_pred.shape[0], y_pred.shape[1], y_pred.shape[2], 3, -1)
    return y_pred_reshaped


def cell_grid(max_grid, batch_size=2):

    max_grid_h, max_grid_w = max_grid
    
    cell_x = np.arange(max_grid_w)
    cell_x = np.tile(cell_x, [max_grid_h])
    cell_x = np.reshape(cell_x, (1, max_grid_h, max_grid_w, 1, 1))
    cell_x = cell_x.astype(np.float32)
    cell_y = np.transpose(cell_x, (0,2,1,3,4))
    cell_grid = np.tile(np.concatenate([cell_x,cell_y],-1), [batch_size, 1, 1, 3, 1])
    return cell_grid


class YoloLayerNp(object):
    def __init__(self,
                 anchors=[90, 95, 92, 154, 139, 281],
                 max_grid=[288, 288], 
                 batch_size=2,
                 warmup_batches=0,
                 ignore_thresh=0.5, 
                 grid_scale=1,
                 obj_scale=5,
                 noobj_scale=1,
                 xywh_scale=1,
                 class_scale=1):
        # make the model settings persistent
        self.ignore_thresh  = ignore_thresh
        self.warmup_batches = warmup_batches
        self.anchors        = anchors.reshape([1,1,1,3,2]).astype(np.float32)
        self.grid_scale     = grid_scale
        self.obj_scale      = obj_scale
        self.noobj_scale    = noobj_scale
        self.xywh_scale     = xywh_scale
        self.class_scale    = class_scale        

        # make a persistent mesh grid
        self.cell_grid = cell_grid(max_grid, batch_size)



from yolo_ import YoloLayer
if __name__ == '__main__':
    
    BATCH_SIZE = 1
    MAX_GRID = [3, 3]
    
    cell_grid_tensor = YoloLayer(max_grid=MAX_GRID, batch_size=BATCH_SIZE).cell_grid
    
    with tf.Session() as sess:
        cell_grid_value = sess.run(cell_grid_tensor)
    cell_grid = cell_grid(MAX_GRID, batch_size=BATCH_SIZE)

    print(np.allclose(cell_grid_value, cell_grid))

