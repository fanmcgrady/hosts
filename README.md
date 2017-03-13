### 好好学习，天天向上。

### 环境要求： python2/3 需要requests库支持

### 兼容Linux和Windows以及OS/X, 使用请同时使用sudo 或者修改windows对应目录下hosts文件当前用户的权限为完全控制
### 使用方法：
**Windows**: 确认安装了python,然后命令行执行 **pip install requests**,然后双击运行即可。  
**Linux**: 依次执行：**pip install requests**, **sudo python changehosts.py**, 运行即可， ~~如果如果电脑名字不是localhost, 那么需要修改源码中的addMine函数，将你的用户名修改插入的条目，避免在使用sudo命令时候的反解出错~~. PS:该问题已经修复，程序自动获取 **/etc/hostname**，添加到文件。

###  2017年2月4日16:42:16
UPDATE：
如果程序对hosts文件没有写权限就会出现下载失败。于是修改了程序，如果没有权限修改系统hosts文件，就将hosts文件保存到当前目录，由用户自行移动到指定位置。  
PS:  
访问网站务必通过https方式，方法是在地址栏手动输入https的前缀，例如： https://www.google.com/ncr   https://www.facebook.com    https://www.twitter.com  
因为http是明文传输数据，用了hosts重定向也是白搭，只有强制用https，才能发挥hosts的作用访问目标网站。  
