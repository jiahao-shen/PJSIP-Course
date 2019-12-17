# 服务器账号
- 组号: 604
- 密码: 258667


# Client端
## Pjproject编译
1. 安装视频库和编码器
    ```bash
    brew install sdl2
    brew install ffmpeg
    brew install openh264
    ```

2. 下载源码并编译
- `wget https://www.pjsip.org/release/2.9/pjproject-2.9.zip`
- `unzip pjproject-2.9.zip`
- `cd pjproject-2.9`
- 添加视频支持, 修改文件`pjlib/include/pj/config_site.h`, 添加如下内容:
    ```cpp
    #define PJMEDIA_HAS_VIDEO 1
    #define FF_INPUT_BUFFER_PADDING_SIZE 32
    ```
- `./configure --enable-shared`
- `make dep && make`
- `sudo make install`

3. 如果只安装交互式界面, 可以使用Homebrew
- `brew install pjproject`


## 编译Python API
1. pjsua(官方已废弃)
- Python版本: 2.7.16
- `cd pjsip-apps/src/python`
- 修改Makefile中的python版本为2, 并允许`make && make install`

2. pjsua2
- Python版本: 3.6.8
- `cd pjsip-apps/src/swig`
- 修改`pjsip-apps/src/swig/python/Makefile`文件, 将`USE_THREADS`的注释取消, 否则会导致视频调用产生死锁
- `make && make install`


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

- **注意**: 由于我的阿里云服务器是公网IP, 因此如要修改一下NAT配置。虽然asterisk使用SIP协议建立连接, 但是语音数据包走的还是RTP协议, 因此需要将阿里云的SIP(默认:5060)端口和RTP(默认:10000~20000)端口都开启, 否则会没有声音。


# OpenSips

## 依赖
- `apt install flex`
- `apt install bison`
- `apt install libxml2`
- `apt install rtpproxy`
- `apt install libssl-dev`
- `apt install libxml2-dev`
- `apt install mysql-server`
- `apt install libmysqlclient-dev` 
- `apt install libncurses5-dev`
- `apt install libcurl4-gnutls-dev`
  

## 编译安装
- `git clone https://github.com/OpenSIPS/opensips.git -b 2.4 opensips-2.4`
- `cd opensips-2.4`
- 多核编译`make menuconfig -j`
- 选中附加模块
  - `db_mysql`
  - `presence`
  - `presence_mwi`
  - `presence_xml`
  - `presence_dialoginfo`
  - `xcap`
  - `xcap-client`
  - 
- 选择`Compile And Install OpenSIPS`

## 配置文件
- 编译完成后运行`osipsconfig`并进行配置
- `Generate OpenSIPS Script`->`Residential Script`->`Configure Residential Script`
  - ENABLE_TCP
  - USE_ALIASES
  - USE_AUTH
  - USE_DBACC
  - USE_DBUSRLOC
  - USE_DIALOG
  - USE_NAT
- `Generate Residential Script`并退出
- 将生成后的文件命名为`opensips.cfg`
- 修改`/usr/local/etc/opensips/opensips.cfg`
    ```bash
    listen:udp:${ip}:5060
    listen:tcp:${ip}:5060

    # rtpproxy module
    loadmodule "rtpproxy.so"
    modparam("rtpproxy", "rtpproxy_sock", "udp:${ip}:12221")

    # presence module
    loadmodule "presence.so"
    loadmodule "presence_xml.so"

    modparam("presence","db_url","mysql://opensips:opensipsrw@localhost/opensips")
    modparam("presence","server_address","sip:sa@${ip}:5060")
    modparam("presence_xml","force_active",1)

    # xcap module
    loadmodule "xcap.so"

    modparam("xcap","db_url","mysql://opensips:opensipsrw@localhost/opensips")
    ```

- 修改`/usr/local/etc/opensips/opensipsctlrc`
    ```bash
    ## your SIP domain
    SIP_DOMAIN=${ip}

    ## chrooted directory
    # $CHROOT_DIR="/path/to/chrooted/directory"

    ## database type: MYSQL, PGSQL, ORACLE, DB_BERKELEY, DBTEXT, or SQLITE
    ## by default none is loaded
    # If you want to setup a database with opensipsdbctl, you must at least specify
    # this parameter.
    DBENGINE=MYSQL

    ## database port (PostgreSQL=5432 default; MYSQL=3306 default)
    DBPORT=3306

    ## database host
    DBHOST=localhost

    ## database name (for ORACLE this is TNS name)
    DBNAME=opensips

    # database path used by dbtext, db_berkeley, or sqlite
    DB_PATH="/usr/local/etc/opensips/dbtext"

    ## database read/write user
    DBRWUSER=opensips

    ## password for database read/write user
    DBRWPW="opensipsrw"

    ## engine type for the MySQL/MariaDB tabels (default InnoDB)
    MYSQL_ENGINE="MyISAM"

    ## database super user (for ORACLE this is 'scheme-creator' user)
    DBROOTUSER="root"

    # user name column
    USERCOL="username"
    ```

- 运行`opensipsdbctl create`创建数据库
- 运行`rtpproxy -F -l {ip} -s udp:${ip}:12221`
- 运行`opensipsctl start`



# MiniSipServer
- 操作系统: Windows 10
- 直接下载并安装即可


# Attention
- 受网络影响, 不同的网络有不同的Bug!!!
- 视频窗口目前无法嵌入tkinter中