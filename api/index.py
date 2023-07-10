from flask import Flask, request, jsonify
import requests
print('HELLO')

app = Flask(__name__)

@app.route('/', methods=['POST'])
def process_image():
    # Получение данных из POST-запроса
    image = request.files['image']
    data = request.form

    # Создание формы данных для отправки
    formData = {'image': image}

    # Отправка POST-запроса на другой сервер
    response = requests.post('http://178.124.214.161:7777/interrogate', files=formData)

    # Возвращение ответа от другого сервера обратно клиенту
    return response.content, response.status_code, response.headers.items()
