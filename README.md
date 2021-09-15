<meta http-equiv="Content-Type" content="text/html; charset=gb2312">

# a-python-proj-crawler
a proj to learn py
## python 代码
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

## js代码
 以下开始，都不是python文件！
### js类的继承```js/a-js.html```
- 包含了类的继承和简单工厂模式

### js 树的生成和遍历 ```js/js-tree.html```
- 本代码是由两个js合并而成，参考地址见[js 递归生成树](https://blog.csdn.net/zJunNa/article/details/109485901),[数据结构-树的遍历可视化](https://blog.csdn.net/Alan_1550587588/article/details/80384945)
- 目标是把对象数组，通过svg生成可视化的形式。

### 设计模式 ```js-pattern/```
- 是整个文件夹,具体看名字
### 阅读器 ```js-reader/```
- ```reader.js```内使用闭包+```$.getJson```的方式获取文件,读取json内容；需要引用jQuery
- ```reader-excel```使用插件```xlsx.core.min```，上传了locale文件夹里的xlsx文件后可被读取。[插件传送门](https://raw.githubusercontent.com/SheetJS/sheetjs/master/dist/xlsx.core.min.js)
)
#### 参考文献
-[五分钟快速了解闭包](https://zhuanlan.zhihu.com/p/22486908)