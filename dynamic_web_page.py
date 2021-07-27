# coding: utf-8
#-*-coding = utf-8 -*-
from selenium.webdriver import Chrome # import package web browser
# 需要下载Chrome.driver mac见 https://blog.csdn.net/qq_35982344/article/details/79608833
from selenium.webdriver.common.keys import Keys # 点击操作
import time # 自带的不用装 

# acsii,unicode转码相关
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# excel 操作相关
import xlrd #读
from xlutils.copy import copy
import xlwt #写

list=[] # 医院列表
def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'hosp.xls')
    # 获取所有sheet
    print workbook.sheet_names() # [u'sheet1', u'sheet2']
    #获取sheet1
    sheet1_name= workbook.sheet_names()[0]
    print ("sheet_name:"+sheet1_name)
    # 根据sheet索引或者名称获取sheet内容
    sheet1 = workbook.sheet_by_name('Sheet1')
    # sheet的名称，行数，列数
    print sheet1.name,sheet1.nrows,sheet1.ncols
    rows = sheet1.row_values(3) # 获取第四行内容
    cols = sheet1.col_values(2) # 获取第三列内容
    print ('row 4:',rows)
    print ('col 2:',cols)
    #获取单元格内容的三种方法
    # print sheet1.cell(1,0).value.encode('utf-8')
    # print sheet1.cell_value(1,0).encode('utf-8')
    # print sheet1.row(1)[0].value.encode('utf-8')
    # 获取单元格内容的数据类型
    # print 'type',sheet1.cell(1,3).ctype

    # 实际操作
    
    r=1;
    while r<sheet1.nrows:
    	word_alias=sheet1.cell(r,3).value
    	word=sheet1.cell(r,2).value
    	# w=eval("u'%s'"%word)
    	list.insert(r,word)
    	r+=1


# 仅展示功能，并没有什么用
def write_excel():
    f = xlwt.Workbook() #创建工作簿

    '''
    创建第一个sheet:
        sheet1
    '''
    sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True) #创建sheet
    row0 = [u'业务',u'状态',u'北京',u'上海',u'广州',u'深圳',u'状态小计',u'合计1']
    column0 = [u'机票',u'船票',u'火车票',u'汽车票',u'其它']
    status = [u'预订',u'出票',u'退票',u'业务小计']

    #生成第一行
    for i in range(0,len(row0)):
        sheet1.write(0,i,row0[i])

    #生成第一列和最后一列(合并4行)
    i, j = 1, 0
    while i < 4*len(column0) and j < len(column0):
        sheet1.write_merge(i,i+3,0,0,column0[j]) #第一列
        sheet1.write_merge(i,i+3,7,7) #最后一列"合计"
        i += 4
        j += 1

    sheet1.write_merge(21,21,0,1,u'合计')

    #生成第二列
    i = 0
    while i < 4*len(column0):
        for j in range(0,len(status)):
            sheet1.write(j+i+1,1,status[j])
        i += 4

    f.save('demo1.xlsx') #保存文件


# 编辑单元格内容
def update_excel(row,col,value):
	rb = xlrd.open_workbook('hosp.xls')    #打开xls文件
	wb = copy(rb)                          #利用xlutils.copy下的copy函数复制
	ws = wb.get_sheet(0)                   #获取表单0
	# ws.write(10,5 , 'changed!')             #改变（10,5）的值
	ws.write(row,col,label = u'%s'%value)           #增加（10,0）的值
	wb.save('hosp_copy.xls')


if __name__ == '__main__':
    read_excel()
    # write_excel()

# 百度百科查找 todo://
# def find_in_baike():


# create browser
web=Chrome();
web.get('https://baike.baidu.com')


for index,i in enumerate(list):
	

	time.sleep(2)
	# 查找input和回车
	web.find_element_by_xpath('//*[@id="query"]').send_keys("%s"%i,Keys.ENTER);
	if(web.current_url.find('item')>0):
		# 如果存在
		a=web.find_element_by_class_name("basic-info").find_elements_by_class_name('basicInfo-item')
		json=" "
		for iindex,item in enumerate(a):
		# 对字符的处理
			if iindex %2==0:
				print (item.text+':'+a[iindex+1].text)
				# python 没有switch 使用 if-else多语句
				if item.text=='医院等级':
					print(index+1,5,)
					update_excel(index+1,5,a[iindex+1].text)
				elif item.text=='地理位置' or item.text=='医院地址':
					update_excel(index+1,4,a[iindex+1].text)
				elif item.text=='医保定点':
					update_excel(index+1,7,'医保定点')
				elif item.text=='经营性质':
					update_excel(index+1,6,a[iindex+1].text)
				iindex+=1
	else:
		# 如果没有
		print (eval("u'%s'"%i)+ ' is not found; ')
	web.find_element_by_xpath('//*[@id="query"]').clear() # 清除输入框
web.quit()

