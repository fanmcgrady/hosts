### 0x00 项目介绍
[项目地址](https://github.com/IanSmith123/hosts)

[![Build Status](https://travis-ci.org/IanSmith123/hosts.svg?branch=master)](https://travis-ci.org/IanSmith123/hosts)
### 0x01 工具介绍
本程序基于python，程序将从[网上](https://coding.net/u/scaffrey/p/hosts/git/raw/master/hosts)获取最新的hosts文件替换本地对应文件，达到科学上网的目的。

由于hosts文件具有时效性，故每隔一段时间需要更新此文件（时间几天到一个月不等），届时再次运行该程序即可。

### 0x02 环境要求： 
兼容Linux和Windows以及OS/X

非windows用户需要python2/3 以及requests库支持

### 0x03 使用方法：

#### Windows: 
* 直接以管理员权限运行 changehosts.exe 文件即可。

* 如果有python 环境，请安装requests库， 然后以管理员权限执行changehosts.py脚本

* 如果不想使用管理员权限运行该程序，请修改`C:\Windows\System32\drivers\etc\hosts`文件权限使当前用户的权限为完全控制

#### Linux:
依次执行：
```bash
$ pip install requests 
$ sudo python changehosts.py
```

###  0x04 注意事项

如果程序对hosts文件没有写权限，程序会将hosts文件保存到当前目录，由用户自行移动到指定位置。

访问网站务必通过https方式，方法是在地址栏手动输入https的前缀，例如： 
- https://www.google.com/ncr
- https://www.facebook.com
- https://www.twitter.com

如果使用此程序之后仍无法正常访问上述网站，请检查本程序是否已经修改**hosts**文件，若未修改，请确认该程序有修改**hosts**文件的权限。

