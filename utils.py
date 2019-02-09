import os
import re

import requests


# 给list所有元素添加前缀
def addListBefore (list,before) :
    sufInd = 0
    while sufInd < len(list):
        list[sufInd] = before + list[sufInd]
        sufInd +=1
    return list



# 调用正则获得想要的内容
def myFindAll(pattern,str) :
    return re.findall(pattern,str,re.S)

# 下载 图片地址  保存路径
def download (url,dir) :
    try:
        if not os.path.exists(dir) :
            r = requests.get(url)
            r.raise_for_status()
            #使用with语句可以不用自己手动关闭已经打开的文件流
            with open(dir,"wb") as f: #开始写文件，wb代表写二进制文件
                f.write(r.content)
            print("爬取完成:" + url + '  to  ' + dir)
        else:
            print("文件已存在")
        return False
    except Exception :
        # print("爬取失败:"+str(e))
        return True


def batchDownLoad (baseUrl,dir) :
    print('开始下载图片：to  ——>   '+dir)
    for i in range(999):
        imgName = (('0' + str(i+1)) if i < 9 else  str(i+1)) + '.jpg'
        if(download(baseUrl + imgName,dir + imgName)) : break
    print('图片下载完成：downLoad  <——    '+baseUrl)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
