# coding: utf-8
#-*-coding = utf-8 -*-
from selenium.webdriver import Chrome # import package web browser
# 需要下载Chrome.driver mac见 https://blog.csdn.net/qq_35982344/article/details/79608833
from selenium.webdriver.common.keys import Keys # 点击操作
import time # 自带的不用装 

import xlrd
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
    list=[] # 医院列表
    r=0;
    while r<sheet1.nrows:
    	print r
    	word=sheet1.cell(r,2).value
    	# w=eval("u'%s'"%word)
    	# print(w)
    	list.insert(r,word)
    	r+=1
    print '40',list
if __name__ == '__main__':
    read_excel()



# hospList=['中国人民解放军联勤保障部队第九四四医院','北京市积水潭医院']

# # create browser
# web=Chrome();
# web.get('https://baike.baidu.com')
# # print(web.page_source);

# time.sleep(1)
# # 查找input和回车
# web.find_element_by_xpath('//*[@id="query"]').send_keys(u'北京市积水潭医院',Keys.ENTER);

# if(web.current_url.find('item')>0):
# 	# 如果存在
# 	a=web.find_element_by_class_name("basic-info").find_elements_by_class_name('basicInfo-item')
# 	json=" "
# 	for index,item in enumerate(a):
# 	# 对字符的处理
# 		if index %2==0:
# 			print (item.text+':'+a[index+1].text)
# 			index+=1
# else:
# 	# 如果没有
# 	print('找不到')

# web.quit()

