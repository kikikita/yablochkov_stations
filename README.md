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
![Взаимосвязь таблиц (1)](https://user-images.githubusercontent.com/110126453/201230045-3055be8d-a81e-43b1-af05-a22e02a34121.jpg)
![Взаимосвязь таблиц (2)](https://user-images.githubusercontent.com/110126453/201230064-2c0bbe90-2f93-4d2f-9efc-89a86143cbd8.jpg)
![Взаимосвязь таблиц (3)](https://user-images.githubusercontent.com/110126453/201230083-c326f22d-7ddd-48ba-af21-58d2f4fdc112.jpg)
![Взаимосвязь таблиц (4)](https://user-images.githubusercontent.com/110126453/201230094-d5fa88b1-dd50-436c-b61c-c282a62c573d.jpg)
![Взаимосвязь таблиц (5)](https://user-images.githubusercontent.com/110126453/201230105-e4229164-2b9c-4759-9694-148d749aa3d7.jpg)

## Метрики

•	Precision (точность) - доля объектов, названных классификатором положительными и при этом действительно являющимися положительными.

$$ Precision = {TP \over (TP + FP)} $$

•	Recall (полнота) - доля объектов положительного класса, найденных классификатором, из всех объектов положительного класса.

$$ Recall = {TP \over (TP + FN)} $$

•	F-мера - гармоническое среднее между точностью и полнотой. Она стремится к нулю, если точность или полнота стремится к нулю.

$$ F = (\beta^{2}+1) * {Precision * Recall \over (\beta^{2}Precision + Recall)} $$

## Гиперпараметры

•	Подбор гиперпараметров: learning_rate & iterations

<img width="975" alt="learningrate" src="https://user-images.githubusercontent.com/110126453/201232085-6279d7c1-9e2b-42ad-aba4-a5e494a6a320.png">

|iterations |	test-Logloss-mean |	test-Logloss-std |	train-Logloss-mean | train-Logloss-std | test-AUC-mean |	test-AUC-std |
| -- | --------- | --------- | --------- | --------- | --------- | --------- |
|0|	0.582369	| 0.001537	| 0.582387	| 0.001344 |	0.850675 | 0.002726 |
|1|	0.497803	| 0.001594	| 0.497844	| 0.001451 |	0.850952 | 0.002529 |
|2|	0.434688	| 0.001516	| 0.434740	| 0.001275 |	0.851116 | 0.002798 |
|3|	0.386346	| 0.001660	| 0.386445	| 0.001177 |	0.851831 | 0.003075 |
|4|	0.349319	| 0.001446	| 0.349450	| 0.001020 |	0.852059 | 0.002840 |

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

## Результаты работы

•	Сравение методов поиска
| method  | speed |
| ------------- | ------------- |
| kNN | 230ms  |
| Approximate NN | 180ms  |

•	Тестовые метрики
| Precission  | Recall | F-мера |
| ------------- | ------------- | ------------- |
| 0.98 | 0.18 | 0.31 |
