import re

import requests

import utils


# 获得页面源码
def HtmlSources(HTMLURL) :
    request = requests.get(HTMLURL)
    request.encoding = requests.utils.get_encodings_from_content(request.text)[0]
    return request.text

# 获得某一类中的 所有分页页面   某类型的页面
def getRootTypePage (typePageHtml) :
    # 拿到某类
    pattern = "option value=\'(.*?.html)\'"
    sufUrls = utils.myFindAll(pattern,typePageHtml)
    # 拿到某个类别中所有的分页
    return sufUrls 


# 获得文件夹的名称
def getImgUrlAndDirPath (PageHtml):
    # 获得文件夹名称
    pattern = "<img src='(.*?)x.jpg' border='0' width='120' height='120' alt='(.*?)'>"
    ImgUrlAndDirs = utils.myFindAll(pattern,PageHtml) # 所有图片所在页的地址
    return ImgUrlAndDirs
