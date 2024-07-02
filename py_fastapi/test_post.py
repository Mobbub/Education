import requests

url = 'http://localhost:8000/post_test'

num_1 = int(input('Введите 1 число: '))
num_2 = int(input('Введите 2 число: '))



data = {'num_1': num_1,
        'num_2': num_2}

response = requests.post(url, json=data)

print(f"\nОтвет: {response.json()}\nОтвет в формате строки: {response.json()['result_str']}\nОтвет в формате целового числа: {response.json()['result_int']}\n")