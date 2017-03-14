#!/usr/bin/python
#! coding=utf-8
####################################################################################
# author: iansmith@qq.com
# notice: Use with caution, any situation has nothing to do with the author.
# date: 2017-01-11 12:29:11
####################################################################################
import requests
import platform

PATH = './hosts'
PLATFORM = ''

URL1 = r'https://coding.net/u/scaffrey/p/hosts/git/raw/master/hosts'
URL2 = r'https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts'
#  download hosts file
def download_for_requests():
    global PATH
    r = requests.get(URL1)
    try:
        f = open(PATH, 'w')
    except:
        PATH = './hosts'
        f = open(PATH, 'w')

    f.write(r.text)
    f.close()

#  judge the platform 
def judge_plat_form():
    global PLATFORM
    PLATFORM = platform.system()

#  depend the platform, set the path for the hosts
def set_path():
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
    

# add hostname to /etc/hosts or when use `sudo xxx` will wait for long time
def add_hostname():
    global PATH
    if PATH == r'/etc/hosts':
        hostname_file = open('/etc/hostname', 'r')
        hostname = hostname_file.read()
        hostname_file.close()
        hosts = open(PATH, 'a+')
        hosts.writelines("127.0.0.1\t %s" % hostname)
        hosts.close()
    else:
        pass

def main():
    judge_plat_form()
    set_path()
    download_for_requests()
    add_hostname()
    print ("finish.")

if __name__=='__main__':
    main()
