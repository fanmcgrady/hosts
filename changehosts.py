#!/usr/bin/python
#! coding=utf-8
############################################################
# author: iansmith@qq.com
# notice: 请勿用作非法用途， 出现任何情况与作者无关
# date: 2017-01-11 12:29:11
############################################################
import requests
import platform

PATH = './hosts'
PLATFORM = ''

URL1 = r'https://coding.net/u/scaffrey/p/hosts/git/raw/master/hosts'
URL2 = r'https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts'
# TODO: download hosts file
def downloadForRequests():
    global PATH
    r = requests.get(URL1)
    f = open(PATH, 'w')
    f.write(r.text)
    f.close()

# TODO: judge the platform 
def judgePlatForm():
    global PLATFORM
    PLATFORM = platform.system()

# TODO: depend the platform, set the path for the hosts
def setPath():
    global PLATFORM
    global PATH
    if PLATFORM == 'Linux':
        PATH = '/etc/hosts'
    elif PLATFORM == "Darwin":
        PATH = '/etc/hosts'
    elif PLATFORM == 'Windows':
        PATH = r'C:\Windows\System32\drivers\etc\hosts'
    else:
        pass
    
def addMine():
    if PATH == r'/etc/hosts':
        hosts = open(PATH, 'a+')
        hosts.writelines("127.0.0.1\tLawrence")
        hosts.close()
    else:
        pass

def main():
    judgePlatForm()
    setPath()
    downloadForRequests()
    addMine()
    print ("finish")

if __name__=='__main__':
    main()
