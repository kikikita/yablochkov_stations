# Yablochkov charging stations for electric vehicles

## Setup
```Linux Kernel Module
conda create -n env_name --python=3.10

conda activate env_name

pip install -r requirements.txt
```
## Usage
```
python main.py
```
## Feature ingeneering
```
![Взаимосвязь таблиц (1)](https://user-images.githubusercontent.com/110126453/201212739-92237294-0864-4ac3-9503-a7e15c3fbaa4.jpg)
![Взаимосвязь таблиц (2)](https://user-images.githubusercontent.com/110126453/201212875-25a80976-4da2-45b0-876d-77c971409c98.jpg)

В ходе исследования установлены наиболее часто ломающиеся подсистемы:
![image](https://user-images.githubusercontent.com/110126453/201215153-76f59f3b-3a66-4cba-91b6-8291db9703de.png)

Для установления взаимосвязи данных, постуающих с датчков и состояний подсистем, были найдены все основные сообщения, которые передают любые изменения на станции
![image2](https://user-images.githubusercontent.com/110126453/201216458-c8eedbbc-d39a-47ff-a307-3689939d4c85.png)
