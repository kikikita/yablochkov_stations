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
![Взаимосвязь таблиц (1)](https://user-images.githubusercontent.com/110126453/201216627-54703b09-cac0-4ca9-ac80-bd965a7527e3.jpg)
```
![Взаимосвязь таблиц (2)](https://user-images.githubusercontent.com/110126453/201216642-a4dfdb6b-0763-4b8a-a9d4-ac4ab552aab6.jpg)

## Feature ingeneering
```
В ходе исследования установлены наиболее часто ломающиеся подсистемы:
![image](https://user-images.githubusercontent.com/110126453/201215153-76f59f3b-3a66-4cba-91b6-8291db9703de.png)

Для установления взаимосвязи данных, постуающих с датчков и состояний подсистем, были найдены все основные сообщения, которые передают любые изменения на станции
![image2](https://user-images.githubusercontent.com/110126453/201216458-c8eedbbc-d39a-47ff-a307-3689939d4c85.png)
