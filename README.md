<meta http-equiv="Content-Type" content="text/html; charset=gb2312">

# a-python-proj-crawler
a proj to learn py

### 抓取图片并存到本地```catch_pic_and_download.py```
- 本代码适用于windows
- import beautifulSoup4
- 抓到图片存到本地文件夹


### 抓取医院的公开信息```dynamic_web_page.py```
- 本代码适用于mac
- import xlrd,xlwt,sys
- 从```hosp.xls```中获得医院的名字，到百度百科里查到基本信息后再填回xls


### 切割图片```cut-img.py```
- 本代码适用于mac
- import pillow
- 可以自定义的定义切的数目（行和列都不能超过10），按矩阵序号排列，也可以设置按需设置正矩阵和逆矩阵
- 普通顺序编号出图，输出效果见文件夹normal-out
- 正矩阵出图，输出效果见文件夹matrix-out
- 逆矩阵出图，输出效果见文件夹inverse-matrix-out

### 拼接图片```stick-img.py```
- 本代码适用于mac
- import pillow
- 把切割好的图片按矩阵序号拼接起来
### 切割图片，倒序排列，拼接图片```cut-and-paste-img-mac.py```
- 本代码适用于mac
- import pillow
- outs和result文件夹是生成的产物。使用这个py前，如果根目录下存在这两个，先删掉再运行。
- 需要处理的图片放在before 文件夹

### 切割图片，倒序排列，拼接图片```cut-and-paste-img.py```
- 本代码适用于windows，是mac的加强版本。增加了对jpg的处理
- import pillow
- outs和result文件夹是生成的产物。使用这个py前，如果根目录下存在这两个，先删掉再运行。
- 需要处理的图片放在before 文件夹

### js类的继承```a-js.html```
- 不是python文件！
- 包含了类的继承和简单工厂模式
