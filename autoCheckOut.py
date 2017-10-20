# -*- coding: utf-8 -*-
import os
import sys
import time
import hashlib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
import smtplib
import subprocess
import time
import plistlib

# 项目根目录
project_path = '/Users/xieyixin/Documents/Work/Git'
# # 脚本根目录
# tag_num = '557'
# # 是否需要更新
# need_pull = 0
#--------------------- 分界线：上面的变量是需要我们手动填写的 ---------------------

def findAllWorkFolder(workType,tag_num,need_pull):
    pl = plistlib.readPlist("AddTagPlist.plist")
    localFiles = os.listdir(project_path)
    resultFile = set(pl) & set(localFiles)
    for localFile in resultFile:        # 第二个实例
        # print('%s/%s' %(project_path,localFile))
        if localFile.startswith(".")!=1:
            print('woring on %s/%s' %(project_path,localFile))
            if workType == 1:
                addTagToRemote(localFile,tag_num)
            else:
                jumpToTag(localFile,tag_num,need_pull)

def jumpToTag(localFile,tag_name,need_pull):
    # 切换本地的分支
    if need_pull:
        os.system('cd %s/%s ;git pull' % (project_path,localFile))
    os.system('cd %s/%s ;git checkout %s' % (project_path,localFile,tag_name))

def addTagToRemote(localFile,tag_name):
    # 打tag并推送到远程
    os.system('cd %s/%s ;git tag %s' % (project_path,localFile,tag_num))
    os.system('cd %s/%s ;git push origin %s' % (project_path,localFile,tag_num))

def main():
    workType = int(raw_input("请输入需要的操作 1：提交tag 2：切换至tag \n"))
    if workType == 1:
        tag_num = raw_input("请输入想提交的tag名称（如600） \n")
        needPull = 0
    else:
        tag_num = raw_input("请输入想切换的tag或者分支名称（如600或者master） \n")
        needPull = raw_input("是否在切换前拉取master最新代码? Y/N \n").lower().startswith("y")

    print('正在切换 %s' %(tag_num))
    if needPull==1:
        print('需要拉取 %s' %(1))

    findAllWorkFolder(workType,tag_num,needPull)
    
    print('切换完成 %s' %(tag_num))

# 执行
main()