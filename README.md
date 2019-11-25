# 服务器账号
- 组号: 604
- 密码: 258667


# Client端
## Pjproject编译
1. 可以使用源码编译
- `git clone https://github.com/pjsip/pjproject.git`
- `cd pjproject`
- `./configure --enable-shared`
- `make dep && make`
- `sudo make install`

2. 如果只安装交互式界面, 可以使用Homebrew
- `brew install pjproject`


## 编译Python API
1. pjsua(官方已废弃)
- Python版本: 2.7.16
- `cd pjsip-apps/src/python`
- 修改Makefile中的python版本为2
- 或者手动运行`python2 setup.py build`和`python2 setup.py install`

2. pjsua2
- Python版本: 3.6.8
- `cd pjsip-apps/src/swig`
- `make`
- `make install`



# Asterisk
- 环境: 阿里云 ubuntu 16.04

## 安装
- `apt install asterisk`

## 修改配置文件
- `/etc/asterisk/sip.conf`
```
[general]
externip = 120.78.218.59
localnet = 192.168.1.0/255.255.255.0
context = default
bindport = 5060
bindaddr = 0.0.0.0
tcpbindaddr = 0.0.0.0
tcpenable = yes
nat = yes

[1001]
type = friend
callerid = User One
secret = 1001
host = dynamic
canreinvite = no
dtmfmode = rfc2833
mailbox = 1001
disallow = all
allow = ulaw
transport = udp

[1002]
type = friend
callerid = User Two
secret = 1002
host = dynamic
canreinvite = no
dtmfmode = rfc2833
mailbox = 1002
disallow = all
allow = ulaw
transport = udp
```

- /etc/asterisk/extensions.conf
```
[general]
static=yes
writeprotect=no

[default]
exten => 1001,1,Answer()
exten => 1001,n,Dial(SIP/1001,20,tr)
exten => 1001,n,Hangup

exten => 1002,1,Answer()
exten => 1002,n,Dial(SIP/1002,20,tr)
exten => 1002,n,Hangup
```

- **注意**: 由于我的阿里云服务器是公网IP, 因此如要修改一下NAT配置。虽然asterisk使用SIP协议建立连接, 但是语音数据包走的还是RTP协议, 因此需要将阿里云的SIP(默认:5060)端口和RTP(默认:10000~20000)端口都开启, 否则会没油声音。


<!-- # OpenSips
- 版本: http://download.opensips.org/opensips-2.4.5.tar.gz2.4.5

## 依赖
- `apt install bison`
- `apt install flex`
- `apt install libxml2`
- `apt install libxml2-dev`
- `apt install mysql-server`
- `apt install libmysqlclient-dev` 
- `apt-get install libncurses5-dev`

## 安装
- `wget http://download.opensips.org/opensips-2.4.5.tar.gz`
- `tar zxf opensips-3.0.0.tar.gz`
- `cd opensips-3.0.0`
- `make menuconfig`
- 选中`db_mysql`
- Compiler and Install -->