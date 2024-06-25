# Библиотека requests

import requests

# Запрос данных из API
response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
data = response.json()

# Вывод данных в консоль
print("Запрос данных из API с помощью requests:")
print(data)
print()

# Библиотека pandas

import pandas as pd

# Загрузка данных из CSV файла
df = pd.read_csv('data.csv')

# Простой анализ данных
print("Анализ данных с помощью pandas:")
print(df.head())
print()
print(df.describe())
print()


# Библиотека numpy

import numpy as np

# Создание массива чисел
array = np.array([1, 2, 3, 4, 5])

# Выполнение математических операций
print("Математические операции с массивом с помощью numpy:")
print("Исходный массив:", array)
print("Квадрат каждого элемента массива:", np.square(array))
print("Среднее значение массива:", np.mean(array))
print()

# Библиотека matplotlib

import matplotlib.pyplot as plt

# Данные для визуализации
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Визуализация данных
plt.plot(x, y, label='sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('График синусоиды')
plt.legend()
plt.show()

# Библиотека pillow

from PIL import Image, ImageFilter

# Загрузка изображения
image = Image.open('example.jpg')

# Применение фильтров
image_resized = image.resize((100, 100))
image_blurred = image.filter(ImageFilter.BLUR)

# Сохранение обработанного изображения
image_resized.save('example_resized.jpg')
image_blurred.save('example_blurred.jpg')

print("Обработка изображения с помощью pillow:")
print("Изображение изменено и сохранено в другие форматы.")
print()

## Пояснения:
# 1. requests: Эта библиотека позволяет легко выполнять HTTP-запросы, получая данные из API.
# Основное преимущество - простота использования и хорошая документация.
# 2. pandas: Позволяет эффективно работать с таблицами данных, проводить анализ и обработку данных.
# Преимущество - мощные функции для манипуляции данными и анализа.
# 3. numpy: Предоставляет удобные инструменты для работы с массивами числовых данных
# и выполнения математических операций.
# Преимущество - высокая производительность для расчетов.
# 4. matplotlib: Предназначена для создания визуализаций данных. Преимущество - широкие возможности
# для построения графиков и настройки их внешнего вида.
# 5. pillow: Позволяет просто работать с изображениями, изменяя их размеры,
# применяя эффекты и сохраняя в различные форматы.
# Преимущество - простота и гибкость в работе с изображениями.
