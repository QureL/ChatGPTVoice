<h1 align="center">
  ChatGPTVoice
</h1>

<p align="center">
    <a>
        <img src="https://img.shields.io/badge/chatGPT-74aa9c?logo=openai&logoColor=white">
    </a>
    <a>
        <img src="https://img.shields.io/badge/Python-3.10-yellowgreen">
    </a>
    <a style="text-decoration:none">
        <img src="https://img.shields.io/badge/platform-windows%20%7C%20macos%20%7C%20linux-lightgrey" />
    </a>
    <a>
        <img src="https://img.shields.io/badge/pyqt-green.svg">
    </a>
</p>

基于[whisper](https://openai.com/research/whisper)和PyQT(PySide6)的实时GPT聊天工具，支持历史会话。不开通gpt plus，体验gpt语音闲聊 :chicken::chicken: 

![](https://raw.githubusercontent.com/QureL/GPT_Talk_Local/main/img/main.png)

<!-- 效果演示：
[![](https://i.ytimg.com/vi/kg4KivftTps/maxresdefault.jpg)](https://youtu.be/kg4KivftTps?si=LZI5ShF5fhIqFjWj "") -->

<!-- 滑稽的中文效果：
[![](https://i.ytimg.com/vi/9svpySx0J8A/maxresdefault.jpg)](https://youtu.be/9svpySx0J8A "") -->

## 环境需求

python >= 3.10

### 操作系统

### win10

本人环境，可行

### Linux

未测试过Linux desktop环境下的表现，理论可行，tts相关可能需要注意，参照 https://github.com/nateshmbhat/pyttsx3#installation-

### Mac

参照Linux，理论可行。

### 显卡

运行`whisper base model`所需显存在1G以下，效果尚可，无杂音、口语准确的情况下准确率能在90%。whisper的`large model`占用显存在8G以上，但是效果非常好，我这糟糕的英语口语都能基本识别对，而且对长语音、断断续续的也有很棒的处理效果。

总体来说，base model比较亲民，但是有条件尽量上large model。对于识别错误的情况，可以在GUI直接修改识别结果。

## 安装

克隆项目

```bash
git clone https://github.com/QureL/ChatGPTVoice.git
cd ChatGPTVoice
```

创建并激活虚拟环境（powershell）

```powershell
mkdir venv
python -m venv .\venv\
.\venv\Scripts\Activate.ps1
```

安装依赖

```bash
pip install -r requirements.txt
```

linux
```bash
apt install portaudio19-dev python3-pyaudio
apt install espeak
```

## 运行

在虚拟环境中直接执行

```
python ./main.py
```

## whisper远程执行

本人有一台12G显存的Linux主机，一台孱弱的1650笔记本，为了能跑whisper large model，可以考虑whisper放在Linux上，客户端和whisper使用ws通信：

Linux上：

```
python scrpit/whisper_server.py --model large-v2
```

客户端：

```
python .\main.py --whisper_mode remote --whisper_address ws://{你的Linux IP}:3001
```

## 启用代理

```powershell
python .\main.py --proxy http://127.0.0.1:10809
```

启用代理后openai gpt请求、模型下载流量均会经过代理节点

## Thanks

[PyQt-Fluent-Widgets](https://github.com/zhiyiYo/PyQt-Fluent-Widgets) A fluent design widgets library based on PyQt5

## TODO LIST

- [ ] 国际化支持
- [x] 聊天ui优化
- [ ] 导入其他TTS
- [ ] 消息编辑
- [ ] 本地langchain向量库
