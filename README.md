# 计算机网络实验
- 组号: 565
- 密码: 258667

# 安装

## 源码编译
- `git clone https://github.com/pjsip/pjproject.git`
- `cd pjproject`
- `./configure --enable-shared`
- `make dep && make`
- `sudo make install`

## Homebrew
- `brew install pjproject`
- 

# 编译Python Module

# pjsua
- Python版本: 2.7.16
- `cd pjsip-apps/src/python`
- 修改Makefile中的python版本为2
- 或者手动运行`python2 setup.py build`和`python2 setup.py install`

# pjsua2
- Python版本: 3.6.8
- `cd pjsip-apps/src/swig`
- `make`
- `make install`


