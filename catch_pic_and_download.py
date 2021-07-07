# print('测试')
# 这两个要安装的
import requests
from bs4 import BeautifulSoup
# 发请求
resp= requests.get("https://www.umei.net/weimeitupian/keaitupian")
resp.encoding = 'utf-8'
# 解析
main_page = BeautifulSoup( resp.text, "html.parser")
# 找东西 find 找1个 find_all 所有
alst = main_page.find("div", attrs={"class": "TypeList"}).find_all("a", attrs={"class":"TypeBigPics"})

n=1
# 获取链接的列表
for a in alst:
	print(a.get("href"))
	href=a.get("href")
	if "https://www.umei.net/" not in href:
		href="https://www.umei.net"+a.get("href")
	#拼接
	
	resp1 = requests.get(href)
	resp1.encoding="utf-8"
	child_page = BeautifulSoup(resp1.text, "html.parser")
	#找到图片的真路径
	src = child_page.find("div", attrs={"class":"ImageBody"}).find("img").get("src")
	#发送请求到服务器.把图片保存在本地
	print(src)
	#创建文件
	
	f = open(r"D:\work\python\tu_%s.jpg" % n, mode="wb") # wb表示写入的内容是非文本文件
	# with open(r(src),'wb+')as f :
	f.write(requests.get(src).content)#向外拿出图片的数据—不是文本信息
	f.close()
	print('保存成功，快去查看图片吧！！')
	n += 1 # n自增 1
	