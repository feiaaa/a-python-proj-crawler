# coding: utf-8
#-*-coding = utf-8 -*-
'''
读入一个图片0.bmp，切成指定数目个小图片(16个)
文件夹名out
'''
from PIL import Image
import sys,os
# 因为考虑到后续拼接编号问题，暂时不考虑横向纵向切>10个的
cut_width_num = 1 # 横向切1个
cut_height_num = 10 # 纵向切10个
# 00,10,20,30,40;01,11,21,31,41

IMAGES_FORMAT = ['.png', '.PNG'] # 图片格式 

# 拼图参数
file_path = r"before/" #加工前图片地址
IMAGES_PATH = r'outs/' # 图片集地址
IMAGES_FORMAT = ['.png', '.PNG'] # 图片格式
IMAGE_ROW = 10 # 图片间隔，也就是合并成一张图后，一共有几行
IMAGE_COLUMN = 1# 图片间隔，也就是合并成一张图后，一共有几列
IMAGE_SAVE_PATH = r'outs/result/' # 图片转换后的地址,可以自己改，这个路径在存之前建立空文件夹result


#生成新图，和原始尺寸一致
def fill_image(image):
  width, height = image.size
  #选取长和宽中较大值作为新图片的
  new_image_length = width if width > height else height
  #生成新图片[白底]
  new_image = Image.new(image.mode, (width, height))
  new_image.paste(image, (0,0))
  return new_image
#切图
def cut_image(image):
  width, height = image.size

  item_width = int(width / cut_width_num)
  item_height=int(height/ cut_height_num)
  box_list = []
  # print(width, height ,item_width,item_height)
  # (left, upper, right, lower)
  for i in range(0,cut_width_num):#两重循环，生成图片基于原图的位置
    for j in range(0,cut_height_num):

      print((i*item_width,j*item_height,(i+1)*item_width,(j+1)*item_height))
      box=(i*item_width,j*item_height,(i+1)*item_width,(j+1)*item_height)
      box_list.append(box)

  image_list = [image.crop(box) for box in box_list]
  return image_list
#保存
def save_images(image_list,folder_name):
  j=0;
  for j in range(0,len(image_list),cut_height_num):
    print (j)
    b=image_list[j:j+cut_height_num];
    i=0;
    for item in b:
        # 逆矩阵编号
        item.save(r'outs/'+folder_name+'/'+str(cut_height_num-1-i)+str(cut_width_num-1-j/cut_height_num) + '.png', 'PNG');
        print (i,j,'done',cut_height_num-1-i,cut_width_num-1-j/cut_height_num);
        i+=1;

# 拼图相关

# 定义图像拼接函数
def image_compose(IMAGE_width, IMAGE_height,names_list,img_before):

  to_image = Image.new('RGBA', (IMAGE_COLUMN * IMAGE_width, IMAGE_ROW * IMAGE_height)) #创建一个新图
  # 循环遍历，把每张图片按顺序粘贴到对应位置上
  for y in range(0, IMAGE_ROW):#10
    for x in range(0, IMAGE_COLUMN):#1

      from_image = Image.open(IMAGES_PATH + names_list[ x+IMAGE_COLUMN * y]).resize(
        (IMAGE_width, IMAGE_height),Image.ANTIALIAS)
      print(x,y,names_list)
      to_image.paste(from_image, (x* IMAGE_width, y* IMAGE_height))
  to_image = to_image.convert('RGBA')
  print('done')
  return to_image.save(IMAGE_SAVE_PATH+img_before) # 保存新图



if __name__ == '__main__':

  #从before文件夹循环取图
  # os.mkdir(r"outs") #创建文件夹存放处理结果
  #获取队列
  print(file_path,'=90',os.listdir)
  image_names_before = [name for name in os.listdir(file_path) for item in IMAGES_FORMAT if
        os.path.splitext(name)[1] == item]
  image_names_before.sort();# 排序

  #批量处理
  n=0;
  for img_before in image_names_before:
    # 处理单个图片 cut
    print(file_path,img_before)
    os.mkdir(IMAGES_PATH+img_before);
    image = Image.open(file_path+img_before);
    width, height = image.size   # 给拼接用的
    # image.show()
    image = fill_image(image)
    image_list = cut_image(image)
    save_images(image_list,img_before);


    #  stick-img
    img_names_after=[name for name in os.listdir(IMAGES_PATH+img_before) for item in IMAGES_FORMAT if
        os.path.splitext(name)[1] == item]
    img_names_after.sort();# 排序

    # 简单的对于参数的设定和实际图片集的大小进行数量判断
    if len(img_names_after) != IMAGE_ROW * IMAGE_COLUMN:
      raise ValueError("合成图片的参数和要求的数量不能匹配！")

    IMAGE_width=width/IMAGE_COLUMN;
    IMAGE_height=height/IMAGE_ROW;
    image_compose(IMAGE_width, IMAGE_height,img_names_after,img_before) #调用函数

    n +=1


