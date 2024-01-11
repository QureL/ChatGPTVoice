# GPT_Talk_Local
[简体中文](https://github.com/QureL/horn/blob/main/README_cn.md)

Base on [whisper](https://openai.com/research/whisper) and PyQT(PySide6), a real-time GPT chat tool is developed, supporting historical conversations. This can help you enjoy the fun of chatting with GPT voice without relying on ChatGPT Plus.

Demo：
[![](https://i.ytimg.com/vi/kg4KivftTps/maxresdefault.jpg)](https://youtu.be/kg4KivftTps?si=LZI5ShF5fhIqFjWj "")



## Requirement

python >= 3.10

### OS

win10+, Linux(Just test in Ubuntu, works), Mac(Based on Linux as reference, theoretically feasible, but not tested.)

### GPU

Running the `whisper base model` requires less than 1GB of available memory, and the results are passable with no noise and an accuracy rate around 90% in accurate spoken language situations. The `whisper large model` requires over 8GB of available memory, yet it provides excellent performance. Even my poor English speaking skills are recognized fairly accurately. Moreover, it handles long speech segments and interruptions quite effectively.

In summary, the base model is more user-friendly, but if conditions allow, it's recommended to use the large model. In cases of recognition errors, modifications can be directly made to the recognized results in the GUI.

## Install

Clone repo

```bash
git clone https://github.com/QureL/GPT_Talk_Local.git
cd GPT_Talk_Local
```

Create and activate a virtual environment.(powershell. In Bash, you may need to run scripts like activate.)

```powershell
mkdir venv
python -m venv .\venv\
.\venv\Scripts\Activate.ps1
```

Install dependencies.

```bash
pip install -r requirements.txt
```

In Linux, you need to run the following command to install the required dependencies.
```bash
apt install portaudio19-dev python3-pyaudio
apt install espeak
```

## Run

Execute directly within the virtual env.

```
python ./main.py
```

## whisper run remotely

I have a Linux host with 12GB of GPU memory and a laptop with a weak 1650 GPU. To run the Whisper large model, you can host Whisper on Linux and use websocket communication between the client and Whisper.

Linux：

```
python scrpit/whisper_server.py --model large-v2
```

client：

```
python .\main.py --whisper_mode remote --whisper_address ws://{You Linux IP}:3001
```

## Proxy for openai

```powershell
python .\main.py --proxy http://127.0.0.1:10809
```

After enabling the proxy, all OpenAI GPT requests and model downloads will pass through the proxy node.

## TODO LIST

- [ ] 国际化支持
- [ ] 聊天ui优化
- [ ] 导入其他TTS
- [ ] 消息编辑
- [ ] 本地langchain向量库

