import pandas as pd
import plotly.express as px
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
def plot_line(data, x_col, y_col):
    """
    Построение линейного графика с Plotly.
    """
    try:
        fig = px.line(data, x=x_col, y=y_col, title=f'Линейный график: {y_col} от {x_col}')
        fig.update_layout(xaxis_title=x_col, yaxis_title=y_col)
        fig.show()
    except Exception as e:
        print(f"Ошибка при построении линейного графика: {e}")


@measure_time
def plot_histogram(data, column, bins=10):
    """
    Построение гистограммы с Plotly.
    """
    try:
        fig = px.histogram(data, x=column, nbins=bins, title=f'Гистограмма распределения: {column}')
        fig.update_layout(xaxis_title=column, yaxis_title='Частота')
        fig.show()
    except Exception as e:
        print(f"Ошибка при построении гистограммы: {e}")


def main():
    """
    Основной цикл приложения.
    """
    print("Приложение для построения графиков и гистограмм с использованием Plotly")
    file_path = input("Введите путь к CSV-файлу: ")

    data = load_csv(file_path)
    if data is None:
        return

    while True:
        print("\nДоступные действия:")
        print("1. Построить линейный график")
        print("2. Построить гистограмму")
        print("3. Вывести первые строки данных")
        print("4. Завершить работу")

        choice = input("Введите номер действия: ")

        if choice == '1':
            print("\nДоступные колонки:", list(data.columns))
            x_col = input("Введите название колонки для оси X: ")
            y_col = input("Введите название колонки для оси Y: ")
            if x_col in data.columns and y_col in data.columns:
                plot_line(data, x_col, y_col)
            else:
                print("Некорректный выбор колонок.")
        elif choice == '2':
            print("\nДоступные колонки:", list(data.columns))
            column = input("Введите название колонки для построения гистограммы: ")
            bins = input("Введите количество интервалов (по умолчанию 10): ")
            bins = int(bins) if bins.isdigit() else 10
            if column in data.columns:
                plot_histogram(data, column, bins)
            else:
                print("Некорректный выбор колонки.")
        elif choice == '3':
            print("\nПервые строки данных:")
            print(data.head())
        elif choice == '4':
            print("Работа приложения завершена.")
            break
        else:
            print("Некорректный выбор действия. Попробуйте снова.")


if __name__ == "__main__":
    main()
