import time
import matplotlib.pyplot as plt
from gauss_mod import gauss_elimination_pivoting
from gauss_notmod import gauss_elimination
from generators import (
    generate_input_data,
    generate_diagonal_input_data,
    generate_singular_input_data,
    generate_diagonally_dominant_matrix
)

def time_gaussian_algorithm(matrix, vector, algorithm):
    start_time = time.time()
    algorithm(matrix.copy(), vector.copy())
    return time.time() - start_time

def run_tests(generator_function):
    sizes = list(range(1, 101))  # тестирование для n от 1 до 100
    times_notmod = []
    times_mod = []

    for size in sizes:
        matrix, vector = generator_function(size)
        
        time_notmod = time_gaussian_algorithm(matrix, vector, gauss_elimination)
        times_notmod.append(time_notmod)

        time_mod = time_gaussian_algorithm(matrix, vector, gauss_elimination_pivoting)
        times_mod.append(time_mod)

    return sizes, times_notmod, times_mod

def plot_results(sizes, times_notmod, times_mod, generator_name, ax):
    ax.plot(sizes, times_notmod, label='Обычный метод')
    ax.plot(sizes, times_mod, label='Модифицированный метод')
    ax.set_xlabel('Размер матрицы (n)')
    ax.set_ylabel('Время выполнения (сек)')
    ax.set_title(f'{generator_name}')
    ax.legend()

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 5))

sizes, times_notmod, times_mod = run_tests(generate_input_data)
plot_results(sizes, times_notmod, times_mod, 'Тест на случайных матрицах', axes[0][0])

sizes, times_notmod, times_mod = run_tests(generate_diagonal_input_data)
plot_results(sizes, times_notmod, times_mod, 'Тест для диагональных матриц', axes[0][1])

sizes, times_notmod, times_mod = run_tests(generate_diagonally_dominant_matrix)
plot_results(sizes, times_notmod, times_mod, 'Тест для диаг. преобл. матриц', axes[1][0])

sizes, times_notmod, times_mod = run_tests(generate_singular_input_data)
plot_results(sizes, times_notmod, times_mod, 'Тест для вырожденных матриц', axes[1][1])

plt.tight_layout()
plt.show()
