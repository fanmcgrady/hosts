### 0x00 项目介绍
这是一个修改本机hosts文件来访问google等网站的小工具,给那些需要上外网查资料的小伙伴。

项目地址[https://github.com/IanSmith123/hosts](https://github.com/IanSmith123/hosts)

下载地址[https://github.com/IanSmith123/hosts/releases](https://github.com/IanSmith123/hosts/releases)

### 0x01 工具介绍
运行该程序时，程序将从[网上](https://coding.net/u/scaffrey/p/hosts/git/raw/master/hosts)获取最新的hosts文件替换本地对应文件，达到科学上网的目的。

由于hosts文件具有时效性，故每隔一段时间需要更新此文件（时间几天到一个月不等），当出现无法访问google的时候，再次运行该程序即可。


### 0x02 环境要求： 
兼容Linux和Windows以及OS/X

非windows用户需要python2/3 以及requests库支持

### 0x03 使用方法：

#### Windows: 
* 方法一： 右击 changehosts.exe ，选择 **以管理员身份运行**即可。

* 方法二： 配置好python和requests， 然后以管理员权限执行changehosts.py

注意：
> 1. 部分安全软件可能会阻止修改本机hosts文件，当出现弹框请求时请点击允许
> 2. 如果不想使用管理员权限运行该程序，请修改`C:\Windows\System32\drivers\etc\hosts`文件权限使当前用户的权限为完全控制

#### Linux && OS/X:
程序会修改`/etc/hosts`文件，如原本有重要内容请注意备份

依次执行：
```bash
$ pip install requests 
$ sudo python changehosts.py
```

###  0x04 注意事项

如果程序对hosts文件没有写权限，程序会将hosts文件保存到当前目录，由用户自行移动到指定位置。

访问网站务必通过 https 方式，方法是在地址栏手动输入https的地址，例如： 
- https://www.google.com/ncr
- https://www.facebook.com
- https://www.twitter.com

关于https的[介绍](https://zh.wikipedia.org/wiki/%E8%B6%85%E6%96%87%E6%9C%AC%E4%BC%A0%E8%BE%93%E5%AE%89%E5%85%A8%E5%8D%8F%E8%AE%AE)
 
如果使用此程序之后仍无法正常访问上述网站，请检查本程序是否已经修改**hosts**文件，若未修改，请确认该程序有修改**hosts**文件的权限。

### 0x05 update
2017-5-30 加入Ipv6 hosts地址, 如有需要请直接修改源码第`21`行的`IPV4`为`IPV6`,作者太懒不想改代码 :)
