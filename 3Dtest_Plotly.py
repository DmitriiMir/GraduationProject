import pandas as pd
import plotly.graph_objects as go
import numpy as np
from scipy.interpolate import griddata
import time


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
def plot_3d_surface(data, x_col, y_col, z_col):
    """
    Построение 3D-поверхности с Plotly.
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

        # Построение 3D-поверхности
        fig = go.Figure(data=[go.Surface(z=zi, x=xi[0], y=yi[:, 0], colorscale='Viridis')])
        fig.update_layout(
            title=f'3D-Поверхность: {z_col} по {x_col} и {y_col}',
            scene=dict(
                xaxis_title=x_col,
                yaxis_title=y_col,
                zaxis_title=z_col
            )
        )
        fig.show()
    except Exception as e:
        print(f"Ошибка при построении 3D-поверхности: {e}")


def main():
    """
    Основной цикл приложения.
    """
    print("Приложение для построения 3D-поверхностей с использованием Plotly")
    file_path = input("Введите путь к CSV-файлу: ")

    data = load_csv(file_path)
    if data is None:
        return

    while True:
        print("\nДоступные действия:")
        print("1. Построить 3D-поверхность")
        print("2. Вывести первые строки данных")
        print("3. Завершить работу")

        choice = input("Введите номер действия: ")

        if choice == '1':
            print("\nДоступные колонки:", list(data.columns))
            x_col = input("Введите название колонки для оси X: ")
            y_col = input("Введите название колонки для оси Y: ")
            z_col = input("Введите название колонки для оси Z: ")
            if x_col in data.columns and y_col in data.columns and z_col in data.columns:
                plot_3d_surface(data, x_col, y_col, z_col)
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

