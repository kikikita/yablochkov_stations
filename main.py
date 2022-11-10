from catboost import CatBoostClassifier, Pool
from datetime import datetime
from pathlib import Path
import os
import csv

FILE = Path(__file__).resolve()
ROOT_ABS = FILE.parents[0]
ROOT = Path(os.path.relpath(ROOT_ABS, Path.cwd()))

CATBOOST_PATH = f"{ROOT}/models/fast_model.bin"
TEST_METERS_PATH = f"{ROOT}/test/test_meters.csv"
TEST_CD_PATH = f"{ROOT}/test/train.cd"

date_time_now = datetime.now().strftime("%d-%m-%Y %H:%M")
meters_list = []
predictions_list = []

print("Loading model and meters..")
model = CatBoostClassifier().load_model(CATBOOST_PATH)
meters = TEST_METERS_PATH
print("Done")

def start():
    while True:
        Join1 = input('Запустить процесс проверки показателей? [y/n]: ') 
        if Join1.lower() == "y":
            meter_values_loader()
            break
        elif Join1.lower() == "n":
            print("Хорошего дня!")
            exit()
        else:
            print("Подумайте над вопросом еще раз!")

def meter_values_loader():
    pool2 = Pool(
    data=os.path.join(TEST_METERS_PATH), 
    delimiter=',', 
    column_description=os.path.join(TEST_CD_PATH),
    has_header=True
    )
    
    with open(TEST_METERS_PATH, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            meters_list.append(f"\nCABLE_ERROR_STATE: {row['CABLE_ERROR_STATE']}\nY_CPU_TEMPERATURE: {row['Y_CPU_TEMPERATURE']}\nY_MODEM_MOBILE_SIGNAL_TYPE {row['Y_MODEM_MOBILE_SIGNAL_TYPE']}")
        
    for proba in model.predict_proba(pool2):        
        if proba[1] >= 0.76:
            predictions_list.append(f"{date_time_now} - ВНИМАНИЕ! C вероятностью {round(proba[1],2)*100}% возможно критическое состояние станции.")
        else:
            predictions_list.append(f"{date_time_now} - Показатели в норме")
        
    for f, b in zip(meters_list, predictions_list):
        print('\n',b,f)

start()
