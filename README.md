# Petstore API Tests
Проект с примерами автоматизированных API-тестов для сервиса [Swagger Petstore](https://petstore.swagger.io)

## Описание проекта
Цель проекта - продемонстрировать базовую структуру автотестов для REST API, используя:
- **Python 3**
- **Pytest** - для организации и запуска тестов
- **Requests** - для отправки HTTP-запросов

Тесты покрывают типичные CRUD-операции для сущности `Pet`

## ⚙️ Установка и запуск

1️⃣ Клонить проект  
`git clone https://github.com/catherineskoch/petstore-tests.git`  
`cd petstore-tests`

2️⃣ Создать виртуальное окружение (рекомендуется)  
`python -m venv venv`  
`source venv/bin/activate   # для macOS/Linux`  
`venv\Scripts\activate      # для Windows`

3️⃣ Установить зависимости  
`pip install -r requirements.txt`

4️⃣ Запуск всех тестов  
`pytest -v tests/`
