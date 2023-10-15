# PeopleTrackModelAPI
## Основа модели
За основу модели была выбрана предобученная модель YOLOv8. В ходе работы она была дообучена на кастомном датасете взятого с Roboflow https://universe.roboflow.com/seeed-studio-knluw/person-ab0mz
## Суть модели
Модель создана для задачи подсчета модели в комнатах офиса. Как результат модели выводится число - количество людей.
## Релизация
1. Модель была дообучена на GPU сервере на кастомном дата сете в 100 эпох. Вот результат обучения:
![Текст с описанием картинки](/images/results.png)
![Текст с описанием картинки](/images/val_batch0_pred.jpg)
2. В ходе предсказания модель модель распазнает только один класс, из-за этого чтобы посчитать людей ножно посчитать количества box в предсказании
3. Преоброзавание в API для того чтобы моделью можно было пользоваться была модель была реализована в микрофреймворке Flask

# Запуск
## Установка
```bash
pip install flask cv2 numpy ultralysics 
```
## Запуск
```bash
python3 run.py 
```