# -*- coding: utf-8 -*-
"""

@author: shiro
"""

import os
import json
from os import listdir, getcwd
from os.path import join

classes = ["person","bicycle","car","motorcycle","airplane","bus","train","truck","boat","traffic light","fire hydrant","stop sign","parking meter","bench","bird","cat","dog","horse","sheep","cow","elephant","bear","zebra","giraffe","backpack","umbrella","handbag","tie","suitcase","frisbee","skis","snowboard","sports ball","kite","baseball bat","baseball glove","skateboard","surfboard","tennis racket","bottle","wine glass","cup","fork","knife","spoon","bowl","banana","apple","sandwich","orange","broccoli","carrot","hot dog","pizza","donut","cake","chair","couch","potted plant","bed","dining table","toilet","tv","laptop","mouse","remote","keyboard","cell phone","microwave","oven","toaster","sink","refrigerator","book","clock","vase","scissors","teddy bear","hair drier","toothbrush"]


def convert_annotation(path, mode=None, dir_img='val2014/'):
    with open(path,'r') as f:
        data = json.load(f)
    with open(path.replace('.json', '.txt'),'w') as f:
        for item in data['images']:
            image_id = item['id']
            file_name = item['file_name']
            width = item['width']
            height = item['height']
            value = filter(lambda item1: item1['image_id'] == image_id,data['annotations'])
            #outfile = open(path+'%s.txt'%(file_name[:-4]), 'a+')
            for item2 in value:
                category_id = item2['category_id']
                value1 = list(filter(lambda item3: item3['id'] == category_id,data['categories']))
                name = value1[0]['name']
                box = item2['bbox']

                
                xmin = int(round(float(box[0])))
                ymin = int(round(float(box[1])))
                xmax = int(round(float(box[2]) + float(box[0]) ))
                ymax = int(round( float(box[1]) + float(box[3])))
                #print(file_name, width, height, str(xmin), str(ymin), str(xmax), str(ymax), name)
                if mode is not None:
                    f.write(dir_img+file_name+','+str(width)+','+str(height)+','+str(xmin)+','+str(ymin)+','+str(xmax)+',' + str(ymax) +','+ name +',' + mode + '\n')
                else:
                    f.write(dir_img+file_name+','+str(width)+','+str(height)+','+str(xmin)+','+str(ymin)+','+str(xmax)+',' + str(ymax) +','+ name + '\n')

            
if __name__ == '__main__':
    path = 'COCO/annotations/instances_train2014.json'
    convert_annotation(path, mode='training', dir_img='train2014/')
