# Используйте официальный образ Python как родительский образ
FROM python:3.8-slim-buster

# Установите рабочую директорию в контейнере
WORKDIR /app

# Копируйте файл requirements.txt в контейнер
COPY requirements.txt requirements.txt

# Установите все зависимости
RUN pip3 install -r requirements.txt

# Копируйте остальные файлы проекта в контейнер
COPY . .

# Запустите приложение Flask
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]