# horn
基于[whisper](https://openai.com/research/whisper)和PyQT(PySide6)的实时GPT聊天工具，支持历史会话


效果演示：
[![](https://i.ytimg.com/vi/kg4KivftTps/maxresdefault.jpg)](https://youtu.be/kg4KivftTps?si=LZI5ShF5fhIqFjWj "")

滑稽的中文效果：
[![](https://i.ytimg.com/vi/9svpySx0J8A/maxresdefault.jpg)](https://youtu.be/9svpySx0J8A "")

## 环境需求

python >= 3.10

### 显卡

运行`whisper base model`所需显存在1G以下，效果尚可，无杂音、口语准确的情况下准确率能在90%。whisper的`large model`占用显存在8G以上，但是效果非常好，我这糟糕的英语口语都能基本识别对，而且对长语音、断断续续的也有很棒的处理效果。

总体来说，base model比较亲民，但是有条件尽量上large model。对于识别错误的情况，可以在GUI直接修改识别结果。

## 安装

克隆项目

```bash
git clone https://github.com/QureL/horn.git
cd horn
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

## TODO LIST

- [ ] 国际化支持
- [ ] 聊天ui优化
- [ ] 导入其他TTS
- [ ] 消息编辑
- [ ] 本地langchain向量库

