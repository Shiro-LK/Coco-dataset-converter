# -*- coding: utf-8 -*-

import os
import json
from os import listdir, getcwd
from os.path import join

classes = ["person","bicycle","car","motorcycle","airplane","bus","train","truck","boat","traffic light","fire hydrant","stop sign","parking meter","bench","bird","cat","dog","horse","sheep","cow","elephant","bear","zebra","giraffe","backpack","umbrella","handbag","tie","suitcase","frisbee","skis","snowboard","sports ball","kite","baseball bat","baseball glove","skateboard","surfboard","tennis racket","bottle","wine glass","cup","fork","knife","spoon","bowl","banana","apple","sandwich","orange","broccoli","carrot","hot dog","pizza","donut","cake","chair","couch","potted plant","bed","dining table","toilet","tv","laptop","mouse","remote","keyboard","cell phone","microwave","oven","toaster","sink","refrigerator","book","clock","vase","scissors","teddy bear","hair drier","toothbrush"]


def convert_annotation(path, mode=None, dir_img='val2014/'):
    '''
        Convert coco .json format to .txt format : filename, xmin, ymin, xmax,ymax, class
    '''
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
                
                # PASCAL VOC format
                if name == 'tv':
                    name = 'tvmonitor'
                elif name == 'motorcycle':
                    name = 'motorbike'
                elif name == 'airplane':
                    name = "aeroplane"
                elif name == "couch":
                    name = "sofa"
                elif name =='dining table':
                    name = 'diningtable'
                elif name == 'potted plant':
                    name = 'pottedplant'
                xmin = int(float(box[0]))
                ymin = int(float(box[1]))
                xmax = int(round(float(box[2]) + float(box[0]) ))
                ymax = int(round(float(box[1]) + float(box[3])))
                if xmin > xmax:
                    print('xmin > xmax')
                elif xmin + 2 > xmax:
                    xmax = xmin + 2
                if ymin > ymax:
                    print('ymin > ymax')
                elif ymin + 2 > ymax:
                    ymax = ymin + 2  
                #print(file_name, width, height, str(xmin), str(ymin), str(xmax), str(ymax), name)
                if mode is not None:
                    f.write(dir_img+file_name+','+str(width)+','+str(height)+','+str(xmin)+','+str(ymin)+','+str(xmax)+',' + str(ymax) +','+ name +',' + mode + '\n')
                else:
                    f.write(dir_img+file_name+','+str(width)+','+str(height)+','+str(xmin)+','+str(ymin)+','+str(xmax)+',' + str(ymax) +','+ name + '\n')
def combine_files(listFile, filename):
    final_data = []
    for file in listFile:
        with open(file, 'r') as f:
            for data in f:
                final_data.append(data)
    with open(filename, 'w') as f:
        for data in final_data:
            f.write(data)
            
if __name__ == '__main__':
#    print('train 2017')
#    path = '../annotations2017/instances_train2017.json'
#    convert_annotation(path, mode='training', dir_img='COCO/train2017/')
#    
#    print('val 2017')
#    path = '../annotations2017/instances_val2017.json'
#    convert_annotation(path, mode='testing', dir_img='COCO/val2017/')
#    
#    print('train 2014')
#    path = '../annotations2014/instances_train2014.json'
#    convert_annotation(path, mode='training', dir_img='COCO/train2014/')
#    
#    print('val 2014')
#    path = '../annotations2014/instances_val2014.json'
#    convert_annotation(path, mode='training', dir_img='COCO/val2014/')
#    
#    print('combine files')
#    combine_files(['../annotations2017/instances_train2017.txt', '../annotations2017/instances_val2017.txt'], 'coco2017.txt')
#    combine_files(['../annotations2014/instances_train2014.txt', '../annotations2014/instances_val2014.txt'], 'coco2014.txt')
#    combine_files(['coco2014.txt', 'coco2017.txt'], 'coco_dataset.txt')
    combine_files(['../../labels/VOCfulltrain.txt', 'coco_dataset.txt'], 'coco_VOC++.txt')
   
    
    #combine_files(['../../labels/VOC2007train.txt', '../../VOCdevkit/labels/VOC2012train.txt'], 'VOCtrain.txt')
    combine_files(['../../labels/VOCtrain.txt', 'coco_dataset.txt'], 'coco_VOCtrain.txt')
