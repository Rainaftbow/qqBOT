# 三叶草bot

## 和群u一起基于nonebot制作了三叶草bot2.0，

### 最新代码&仓库地址：

https://github.com/ClovertaTheTrilobita/SanYeCao-Nonebot

## 介绍

做了一个基于官方api的qq机器人demo，可以进行简单的天气查询、待办编辑、发送图片的功能。

更多功能后续完善中。

### 官方仓库

https://github.com/tencent-connect/botpy

### 亮点

·使用sqlite存储部分字段，实现针对不同用户生成不同的每日运势

·可以为不同用户单独存储待办。

·待办内容以json文件形式存储在本地，机器人下线后仍能妥善保管。

·使用自动化脚本上传图片至图床以供qq官方api使用，具有从本地发送图片的功能。

·图片上传至图床过后会自动访问图床api删除，防止数据冗余。

### 存在的问题

·图片从图床删除时使用selenium库访问url的功能，访问速度较慢且容易发生问题。

·待办添加逻辑不完善，若用户输入的待办和默认一致，则会清空用户待办。

### 声明

·bot脚本使用的部分代码借鉴自网络，非常感谢大佬们能分享自己的思路Orz。

## 如何使用

### 配置conda环境（推荐）

在已安装conda的环境下，在终端输入

```powershell
conda create -n chatbot
```

或者把chatbot换成你喜欢的名字，之后输入

```commandline
conda activate chatbot
```

启动环境。

然后输入：

```powershell
conda install pip
```

安装pip

最后，在项目根目录中找到*requirements.txt*，输入：

```powershell
pip install -r requirements.txt
```

安装所需软件包。

*requirements.txt*内的包可能看起来很多，实际上大部分都是conda环境自带的，我直接把所有的贴上去了，因为懒（）

### 配置API

#### (1) 更改机器人的账号密码

在 ./botpy/examples/config.yaml 中，找到

```yaml
#机器人配置
appid: "Your_Bot_Id"
secret: "Enter_Your_Bot_Secret_Here"

```

将其中的*Your_Bot_Id*和*Enter_Your_Secret_Here*分别更改为你的机器人Apple Id和Apple Secret。需从QQ开放平台获取。

#### （2）更改图床API令牌

\*因为本项目使用的sm.ms图床，所以脚本是基于该图床返回内容格式编写，如果你想用其它图床需根据自己图床返回数据的格式更改代码内容。

首先从https://sm.ms/ 中的*User*下找到*Dashboard*，在*API Token*中复制*Secret Token*。

在 ./botpy/examples/config.yaml 中，找到

```yaml
picturesToken: "Your_Token"
```

将其替换上述的*Your_Token*。

### 启动机器人

非常棒！你已经完成了全部配置过程！

现在，进入 ./botpy/examples/ 路径，找到*client.py*，在终端输入

```powershell
python client.py
```

启动机器人。

