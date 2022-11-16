# Автомобильные зарядные станции Яблочков

## Задача классификации критических состояний подсистем электростанций
Предсказание вероятного появления критических состояний на подсистемах станций до их фактического появления на основе данных об изменениях работы подсистем.

Для решения данной проблемы был выбран CatBoost — метод машинного обучения, основанный на градиентном бустинге. CatBoost позволяет проводить обучение на нескольких GPU. Библиотека позволяет получить отличные результаты с параметрами по умолчанию, что сокращает время, необходимое для настройки гиперпараметров. Обеспечивает повышенную точность за счет уменьшения переобучения.

## Установка
```Linux Kernel Module
conda create -n env_name --python=3.10

conda activate env_name

pip install -r requirements.txt
```
## Применение
```
python main.py
```
## Поиск фичей
![Взаимосвязь таблиц (1)](https://user-images.githubusercontent.com/110126453/201230045-3055be8d-a81e-43b1-af05-a22e02a34121.jpg)
![Взаимосвязь таблиц (2)](https://user-images.githubusercontent.com/110126453/201230064-2c0bbe90-2f93-4d2f-9efc-89a86143cbd8.jpg)
![Взаимосвязь таблиц (3)](https://user-images.githubusercontent.com/110126453/201230083-c326f22d-7ddd-48ba-af21-58d2f4fdc112.jpg)
![Взаимосвязь таблиц (4)](https://user-images.githubusercontent.com/110126453/201230094-d5fa88b1-dd50-436c-b61c-c282a62c573d.jpg)
![Взаимосвязь таблиц (5)](https://user-images.githubusercontent.com/110126453/201230105-e4229164-2b9c-4759-9694-148d749aa3d7.jpg)

## Метрики

• Accuracy – показатель, который описывает общую точность предсказания модели по всем классам. Рассчитывается как отношение количества правильных прогнозов к их общему количеству.

•	Precision (точность) - доля объектов, названных классификатором положительными и при этом действительно являющимися положительными.

$$ Precision = {TP \over (TP + FP)} $$

•	Recall (полнота) - доля объектов положительного класса, найденных классификатором, из всех объектов положительного класса.

$$ Recall = {TP \over (TP + FN)} $$

•	F-мера - гармоническое среднее между точностью и полнотой. Она стремится к нулю, если точность или полнота стремится к нулю.

$$ F = (\beta^{2}+1) * {Precision * Recall \over (\beta^{2}Precision + Recall)} $$

## Гиперпараметры

•	Подбор гиперпараметров: learning_rate & iterations

<img width="975" alt="learningrate" src="https://user-images.githubusercontent.com/110126453/201232085-6279d7c1-9e2b-42ad-aba4-a5e494a6a320.png">

•	Метрики на кросс-валидации

|iterations |	test-Logloss-mean |	test-Logloss-std |	train-Logloss-mean | train-Logloss-std | test-AUC-mean |	test-AUC-std |
| -- | --------- | --------- | --------- | --------- | --------- | --------- |
|0|	0.582369	| 0.001537	| 0.582387	| 0.001344 |	0.850675 | 0.002726 |
|1|	0.497803	| 0.001594	| 0.497844	| 0.001451 |	0.850952 | 0.002529 |
|2|	0.434688	| 0.001516	| 0.434740	| 0.001275 |	0.851116 | 0.002798 |
|3|	0.386346	| 0.001660	| 0.386445	| 0.001177 |	0.851831 | 0.003075 |
|4|	0.349319	| 0.001446	| 0.349450	| 0.001020 |	0.852059 | 0.002840 |

Best validation Logloss score, not stratified: 0.2198±0.0044 on step 97

•	Итоговые гиперпараметры:

| hyperparameters | value |
| ------------------- | ---------------|
| Iterations | 100 |
| Learning_rate | 0.1 |
| Custom_loss | AUC, Accuracy, F1 |
| Boosting_type | Plain |
| Bootstrap_type | Bernoulli |
| Subsample| 0.5 |
| Rsm | 0.5 |
| Leaf_estimation_iterations | 5 |
| Max_ctr_complexity | 1 |

## Результаты экспериментов

•	График AUC

<img width="974" alt="auc" src="https://user-images.githubusercontent.com/110126453/201235544-ec15fd0a-36c8-4432-8267-94a70c686602.png">

•	График Accuracy

<img width="974" alt="accuracy" src="https://user-images.githubusercontent.com/110126453/201235693-1e6b333f-210b-44fb-b285-e223a27d30a9.png">

•	График F-1

<img width="974" alt="f1" src="https://user-images.githubusercontent.com/110126453/201235760-47206225-4ae2-478d-8b09-37db90ab8099.png">

•	Таблица сравнения качества моделей с разными гиперпараметрами на тестовой выборке

| model name | accuracy | f-1 | precision | recall |
| ------- | -------- | --------- | -------- | --------- |
| model | 0.9428 | 0.9657 | 0.9309 | 0.9339 |
| fast model | 0.9430 | 0.9658 | 0.9395 | 0.9935 |
| best model | 0.9434 | 0.9660 | 0.9413 | 0.9919 |

• Важность фичей

![Взаимосвязь таблиц (6)](https://user-images.githubusercontent.com/110126453/201240730-5d6d8d28-54bf-4ea3-b331-90c95f59ae44.jpg)

## Устройство системы

![Взаимосвязь таблиц (7)](https://user-images.githubusercontent.com/110126453/201247722-5cc842c2-1fe6-4130-9e6e-c21fc7018ae7.jpg)

•	Система может быть масштабирована на множество станций

## Демонстрация работы

<img width="600" alt="Снимок экрана 2022-11-11 054348" src="https://user-images.githubusercontent.com/110126453/201251409-854d812b-5c44-4a93-a7c7-19ef56ccdace.png">

