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

| hyperparameters | value |
| ------------------- | ---------------|
| Iterations | 100 |
| learning_rate | 0.1 |
| Custom_loss | AUC, Accuracy, F1 |
| Boosting_type | Plain |
| Bootstrap_type | Bernoulli |
| Subsample| 0.5 |
| rsm | 0.5 |
| leaf_estimation_iterations | 5 |
| max_ctr_complexity | 1 |


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
