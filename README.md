# Corona-Display

![License](https://img.shields.io/badge/license-MIT-green.svg) [![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

Corona-Display 概览

Corona-Display是一个使用树莓派+屏幕，自动爬取和展示网络上关于新冠感染数据的变动情况的自动程序，它基于BeautifulSoup4对网络上的信息进行爬取，然后将获得的数据保存为Json数据，由Vue+Vuetify构建页面，读取数据并进行相应的展示。Corona-Display目前仅支持获取和展示全球各国家总新冠肺炎数据，以及国内各地区的新冠肺炎数据，Corona-Display支持对所展示的各项数据进行多元排序，方便用户从更多角度理解和分析数据。本程序全部数据均来自于[**丁香园**](https://ncov.dxy.cn/ncovh5/view/pneumonia)。

本仓库包括以下内容：

1. 一份完整的Corona-Display代码和打包后的文件(位于Release页面)。
2. Corona-Display的安装及使用教程。
3. 设置树莓派开机启动Corona-Display的注意事项。

## 内容列表

- [背景](#背景)

- [安装](#安装)
  
  - [BeautifulSoup4](#BeautifulSoup4)
  
- [运行Corona-Display](#运行Corona-Display)
  - [使用PC运行](#使用PC运行)
  - [使用树莓派运行](#使用树莓派运行)
  
- [配置树莓派开机自启动Corona-Display](#配置树莓派开机自启动Corona-Display)

  - [配置crontab](#配置crontab)
  - [配置rc.local](#配置rc.local)
  - [配置autostart](#配置autostart)

- [维护者](#维护者)

- [如何贡献](#如何贡献)

- [使用许可](#使用许可)

## 背景

**Corona-Display** 是为了构建出一个在不占有PC和手机资源的同时，可以使用嵌入式设备在联网环境下获取和展示关于新冠信息的程序，以方便用户对新冠数据的实时追踪。

> 如果您对程序目前所展示的数据抱有异议或建议，请随时在Issue下留下您的想法，不胜感激。

## 安装

该项目使用Python，并依赖BeautifulSoup4。在使用Corona-Display之前，请先保证您的程序所在运行环境内在本地安装了他们。

- [Python官网](https://www.python.org/)

作者使用的Python版本为3.8，在运行过程中并无问题。

### BeautifulSoup4

BeautifulSoup4是一个基于Python的网络数据爬取框架，是本程序爬虫部分的主体框架。

- [BeautifulSoup4 DOC](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

在安装好Python之后，请打开CMD窗口并直接输入:

```sh
pip install beautifulsoup4
```

## 运行Corona-Display

运行Corona-Display十分简单，因为该项目的主体部分已经经过Webpack打包(您可以在本项目的Release页面下得到他们)。总的来说，运行Corona-Display只需要您在项目的主目录一下运行一个服务器，然后通过浏览器访问程序所在的地址即可。

### 使用PC运行

1. 下载Release页面下的压缩文件并解压(一般为 **Corona-Display-X.X.X.zip** )。

   - [Release页面](https://github.com/RockyXRQ/Corona-Display/releases/tag/1.0.0)

2. 在CMD环境下进入到程序主目录下并执行：

   ```sh
   python3 -m http.server --bind 0.0.0.0 8080
   ```

   ![http.server](https://raw.githubusercontent.com/RockyXRQ/Corona-Display/master/public/assets/http.server.png)

3. 使用浏览器进入 http://0.0.0.0:8080，即可看到Corona-Display的数据展示页面。

   ![corona-display-main-page](https://raw.githubusercontent.com/RockyXRQ/Corona-Display/master/public/assets/corona-display-main-page.png)

### 使用树莓派运行

1. 下载Release页面下的压缩文件或使用U盘拷贝至树莓派并解压(一般为 **Corona-Display-X.X.X.zip** )。

   - [Release页面](https://github.com/RockyXRQ/Corona-Display/releases/tag/1.0.0)

   > 注意：在Raspbian环境下挂载U盘可能需要额外安装插件来正常读取U盘的数据。

2. 在终端下进入到程序主目录下并执行：

   ```sh
   python3 -m http.server --bind 0.0.0.0 8080
   ```

3. 使用浏览器进入[ http://0.0.0.0:8080]( http://0.0.0.0:8080)，即可看到Corona-Display的数据展示页面。

   ![corona-display-main-page-raspberry](https://raw.githubusercontent.com/RockyXRQ/Corona-Display/master/public/assets/corona-display-main-page-raspberry.png)

## 配置树莓派开机自启动Corona-Display

### 配置crontab

crontab负责处理linux环境下的定时任务，配置crontab可以通过每3分钟执行一次我们的爬虫程序，使得新冠感染数据更新。

1. 在终端下运行：

   ```sh
   sudo nano /etc/crontab
   ```

2. 在末尾添加以下代码并保存：

   ```sh
   /3 * * * * root python3 /home/pi/Corona-Display/scripts/CoronaCrawler.py
   ```

### 配置rc.local

1. 在终端下运行：

   ```sh
   sudo nano /etc/rc.local
   ```

2. 在exit 0代码前加入以下代码并保存:

   ```sh
   su pi
   cd /home/pi/Corona-Display
   python3 -m http.server --bind 0.0.0.0 8080 &
   service crond start
   ```

   > 注意：当Raspbian在启动过程中执行rc.local是以root身份来执行的，则在rc.local中不使用su pi指令可能会造成某些程序的启动失败。还有请注意在rc.local内书写路径时请务必使用绝对地址。

### 配置autostart

1. 在终端下运行:

   ```sh
   sudo nano /home/pi/.config/autostart/my.desktop
   ```

2. 输入以下代码并保存:

   ```sh
   [Desktop Entry]
   Type=Application
   Exec = chromium-browser --kiosk "http://0.0.0.0:8080/"
   ```

## 维护者

[@Rocky_](https://github.com/RockyXRQ)

## 如何贡献

非常期待您的任何建议，如果您有任何想法，或者发现了程序中的问题，请务必发起 Issue 或者直接与我联系。

## 使用许可

[MIT](LICENSE) © Rocky Xu
