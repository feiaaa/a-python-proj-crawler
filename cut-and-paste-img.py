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
    

if __name__ == '__main__':
  #简易版本
  # file_path = "number.png"
  # os.mkdir(r"out")
  # image = Image.open(file_path)  
  # #image.show()
  # image = fill_image(image)
  # image_list = cut_image(image)
  # save_images(image_list)

  #从before文件夹循环取图
  file_path = r"before/" #加工前图片地址
  os.mkdir(r"outs") #创建文件夹存放处理结果
  #获取队列
  image_names_before = [name for name in os.listdir(file_path) for item in IMAGES_FORMAT if
        os.path.splitext(name)[1] == item]
  image_names_before.sort();# 排序

  #批量处理
  n=0;
  for img_before in image_names_before:
    # 处理单个图片
    print(file_path,img_before)
    os.mkdir(r"outs/"+img_before);
    image = Image.open(file_path+img_before)  
    # image.show()
    image = fill_image(image)
    image_list = cut_image(image)
    save_images(image_list,img_before);

    # todo stick-img
    n +=1


