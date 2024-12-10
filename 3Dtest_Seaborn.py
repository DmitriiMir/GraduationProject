import pandas as pd
import seaborn as sns
import numpy as np
from scipy.interpolate import griddata
import time
import matplotlib.pyplot as plt


def load_csv(file_path):
    """
    Загрузка данных из CSV-файла.
    """
    try:
        data = pd.read_csv(file_path)
        print(f"Данные успешно загружены из {file_path}")
        print("Колонки в файле:", list(data.columns))
        return data
    except Exception as e:
        print(f"Ошибка при загрузке файла: {e}")
        return None


def measure_time(func):
    """
    Декоратор для измерения времени выполнения функции.
    """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Время рендеринга: {elapsed_time:.4f} секунд")
        return result

    return wrapper


@measure_time
def plot_heatmap(data, x_col, y_col, z_col):
    """
    Построение тепловой карты (аналог 3D-поверхности) с Seaborn.
    """
    try:
        # Получение данных
        x = data[x_col].values
        y = data[y_col].values
        z = data[z_col].values

        # Создание сетки и интерполяция значений
        xi = np.linspace(x.min(), x.max(), 100)
        yi = np.linspace(y.min(), y.max(), 100)
        xi, yi = np.meshgrid(xi, yi)
        zi = griddata((x, y), z, (xi, yi), method='linear')

        # Построение тепловой карты
        plt.figure(figsize=(10, 8))
        sns.heatmap(zi, cmap='viridis', xticklabels=False, yticklabels=False, cbar_kws={'label': z_col})
        plt.title(f"Тепловая карта: {z_col} по {x_col} и {y_col}")
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.show()
    except Exception as e:
        print(f"Ошибка при построении тепловой карты: {e}")


def main():
    """
    Основной цикл приложения.
    """
    print("Приложение для построения тепловой карты (аналог 3D-поверхности) с использованием Seaborn")
    file_path = input("Введите путь к CSV-файлу: ")

    data = load_csv(file_path)
    if data is None:
        return

    while True:
        print("\nДоступные действия:")
        print("1. Построить тепловую карту")
        print("2. Вывести первые строки данных")
        print("3. Завершить работу")

        choice = input("Введите номер действия: ")

        if choice == '1':
            print("\nДоступные колонки:", list(data.columns))
            x_col = input("Введите название колонки для оси X: ")
            y_col = input("Введите название колонки для оси Y: ")
            z_col = input("Введите название колонки для значений Z: ")
            if x_col in data.columns and y_col in data.columns and z_col in data.columns:
                plot_heatmap(data, x_col, y_col, z_col)
            else:
                print("Некорректный выбор колонок.")
        elif choice == '2':
            print("\nПервые строки данных:")
            print(data.head())
        elif choice == '3':
            print("Работа приложения завершена.")
            break
        else:
            print("Некорректный выбор действия. Попробуйте снова.")


if __name__ == "__main__":
    main()
