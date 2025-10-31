# 1. Базовий образ Python
FROM python:3.11-slim

# 2. Робоча директорія всередині контейнера
WORKDIR /app

# 3. Копіюємо всі файли проекту
COPY . /app

# 4. Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# 5. Відкриваємо порт для Flask
EXPOSE 5000

# 6. Команда для запуску Flask
CMD ["python", "app.py"]
