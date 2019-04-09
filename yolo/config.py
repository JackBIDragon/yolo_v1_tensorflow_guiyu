import os

#
# path and dataset parameter 数据集路径，和模型检查点文件路径
#配置文件
#

DATA_PATH = 'data' #所有数据所在的根目录

PASCAL_PATH = os.path.join(DATA_PATH, 'pascal_voc')  #VOC2012数据集所在的目录

CACHE_PATH = os.path.join(PASCAL_PATH, 'cache')      #保存生成的数据集标签缓冲文件所在文件夹

OUTPUT_DIR = os.path.join(PASCAL_PATH, 'output')   #存放输出文件的地方，data/pascal_voc/output  #保存生成的网络模型和日志文件所在的文件夹

WEIGHTS_DIR = os.path.join(PASCAL_PATH, 'weights')  #weights_dir, 路径为data/pascal_voc/weights #检查点文件所在的目录

WEIGHTS_FILE = None   #weights file
# WEIGHTS_FILE = os.path.join(DATA_PATH, 'weights', 'YOLO_small.ckpt')

CLASSES = ['aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus',
           'car', 'cat', 'chair', 'cow', 'diningtable', 'dog', 'horse',
           'motorbike', 'person', 'pottedplant', 'sheep', 'sofa',
           'train', 'tvmonitor']    #PASCAL VOC数据集的20个类别

FLIPPED = True   #使用水平镜像，扩大一倍数据集？


#
# model parameter    网络模型参数
#

IMAGE_SIZE = 448     #输入图片的大小

CELL_SIZE = 7     #整张图片分为cell_size * cell_size的大小

BOXES_PER_CELL = 2    #每个cell负责预测两个bounding box

ALPHA = 0.1         #泄露修正线性激活函数 系数

DISP_CONSOLE = False  #控制台输出信息

#损失函数 的权重设置
OBJECT_SCALE = 1.0   #有目标时，置信度权重
NOOBJECT_SCALE = 1.0 #没有目标时，置信度权重
CLASS_SCALE = 2.0    #类别权重
COORD_SCALE = 5.0    #边界框权重


#
# solver parameter 训练参数设置
#

GPU = ''

LEARNING_RATE = 0.0001   #学习率

DECAY_STEPS = 30000      #退化学习率衰减步数

DECAY_RATE = 0.1         #衰减率
 
STAIRCASE = True

BATCH_SIZE = 45   #batch size #批量大小

MAX_ITER = 15000    #迭代次数，可自定义

SUMMARY_ITER = 10   #日志文件保存间隔步

SAVE_ITER = 1000    #模型保存间隔步


#
# test parameter    测试时的相关参数
#

THRESHOLD = 0.2     #格子有目标的置信度阈值

IOU_THRESHOLD = 0.5   #IOU阈值0.5
