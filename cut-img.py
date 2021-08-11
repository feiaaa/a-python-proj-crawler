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
def save_images(image_list):
  # 普通的保存（这这里顺序编号，不用考虑10的问题）
  # index = 1 
  # for image in image_list:
  #   image.save(r'out/'+str(index) + '.png', 'PNG');
  #   print("done")
  #   index += 1
  j=0;
  for j in range(0,len(image_list),cut_height_num):
    print (j)
    b=image_list[j:j+cut_height_num];
    i=0;
    for item in b:
        # 普通矩阵编号
        #item.save(r'out/'+str(i)+str(j/cut_height_num) + '.png', 'PNG');
        # 逆矩阵编号
        item.save(r'out/'+str(cut_height_num-1-i)+str(cut_width_num-1-j/cut_height_num) + '.png', 'PNG');
        print (i,j,'done',cut_height_num-1-i,cut_width_num-1-j/cut_height_num);
        i+=1;
    

if __name__ == '__main__':
  file_path = "number.png"
  os.mkdir(r"out")
  image = Image.open(file_path)  
  #image.show()
  image = fill_image(image)
  image_list = cut_image(image)
  save_images(image_list)

