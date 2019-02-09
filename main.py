# -*-coding:utf8-*-
import os
import re
from multiprocessing import Pool
import time
import requests

import page
import utils

loadPath = 'rosi/'

RootUrl = 'http://www.rosi22.com'

# 需要爬取的页面地址后缀
sufFixUrls = [
    "/x/sp/", "/x/vr/", "/x/app/", "/x/rosi/", "/x/shop/", "/x/sishu/", "/model.html", "/x/yxm/", "/tags.php?/1417/"
]


def CrawlPage(pageUrl) :
    print('开始爬取分页' + pageUrl)
    # 类型下 分页的源码
    pageHtml = page.HtmlSources(pageUrl)
    # 获得所有的图片前缀集合 与文件名集合
    imgUrlAndDirs = page.getImgUrlAndDirPath(pageHtml)
    for imgPath in imgUrlAndDirs:
        PathBase = imgPath[0]
        DirName = loadPath + '/' + imgPath[1] + '/'
        print("图片地址前缀：" + PathBase + "\t\t图片保存文件夹：" + DirName)
        # 判断文件夹是否存在 不存在就创建
        if not os.path.exists(DirName):
            os.makedirs(DirName)
        # # 循环下载未知数量的图片
        utils.batchDownLoad(PathBase,DirName)

if __name__ == '__main__':
    startTime = time.time
    print("开始时间：" + startTime)
    typePageUrls = utils.addListBefore(sufFixUrls, RootUrl)
    for typePageUrl in typePageUrls:
        print('开始爬取地址：' + typePageUrl)
        # 获得类型的源码
        typePageHtml = page.HtmlSources(typePageUrl)
        # 获得分页后缀
        pageUrlSuffix = page.getRootTypePage(typePageHtml)
        # 获得所有的分页
        pageUrls = utils.addListBefore(pageUrlSuffix, typePageUrl)
        with Pool(8) as p:
            p.map(CrawlPage, pageUrls)
    endTime = time.time
    print('结束时间：' + endTime)
    # print('总耗时：' + str(endTime - startTime))