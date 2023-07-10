from flask import Flask, request, jsonify
import requests
print('HELLO')

app = Flask(__name__)

@app.route('/', methods=['POST'])
def process_image():
    try:
        # Получение данных из POST-запроса
        image = request.files['image']
        data = request.form

        # Создание формы данных для отправки
        formData = {'image': image}

        # Отправка POST-запроса на другой сервер
        response = requests.post('http://178.124.214.161:7777/interrogate', files=formData)

        # Возвращение ответа от другого сервера обратно клиенту
        return response.content, response.status_code, response.headers.items()
    except Exception as e:
        print(e)
        return jsonify({'error': 'Внутренняя ошибка сервера'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3002)
