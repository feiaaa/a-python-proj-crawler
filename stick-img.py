# coding: utf-8
#-*-coding = utf-8 -*-
'''
将指定文件夹里面的图片拼接成一个大图片
'''
import PIL.Image as Image
import os
 
IMAGES_PATH = r'out1/' # 图片集地址
IMAGES_FORMAT = ['.png', '.PNG'] # 图片格式
IMAGE_ROW = 5 # 图片间隔，也就是合并成一张图后，一共有几行
IMAGE_COLUMN = 2 # 图片间隔，也就是合并成一张图后，一共有几列
IMAGE_SAVE_PATH = r'out1/result/final.png' # 图片转换后的地址,可以自己改，这个路径在存之前建立空文件夹result
 
# 获取图片集地址下的所有图片名称
image_names = [name for name in os.listdir(IMAGES_PATH) for item in IMAGES_FORMAT if
        os.path.splitext(name)[1] == item]
image_names.sort();# 排序
# 简单的对于参数的设定和实际图片集的大小进行数量判断
if len(image_names) != IMAGE_ROW * IMAGE_COLUMN:
  raise ValueError("合成图片的参数和要求的数量不能匹配！")
 
# 定义图像拼接函数
def image_compose(IMAGE_width, IMAGE_height):

  to_image = Image.new('RGBA', (IMAGE_COLUMN * IMAGE_width, IMAGE_ROW * IMAGE_height)) #创建一个新图
  # 循环遍历，把每张图片按顺序粘贴到对应位置上
  for y in range(0, IMAGE_ROW):#10
    for x in range(0, IMAGE_COLUMN):#1
      
      from_image = Image.open(IMAGES_PATH + image_names[ x+IMAGE_COLUMN * y]).resize(
        (IMAGE_width, IMAGE_height),Image.ANTIALIAS)
      print(x,y,image_names)
      to_image.paste(from_image, (x* IMAGE_width, y* IMAGE_height))
  to_image = to_image.convert('RGBA')
  print('done')
  return to_image.save(IMAGE_SAVE_PATH) # 保存新图



if __name__ == '__main__':
  file_path = "number.png" #原始图片尺寸
  image = Image.open(file_path);
  width, height = image.size;
  IMAGE_width=width/IMAGE_COLUMN;
  IMAGE_height=height/IMAGE_ROW;
  image_compose(IMAGE_width, IMAGE_height) #调用函数
