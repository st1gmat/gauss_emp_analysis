import numpy as np

def generate_input_data(size):
    # генерируем случайную матрицу коэффициентов
    matrix = np.random.rand(size, size)
    b = np.random.rand(size)
    return matrix, b

def generate_diagonally_dominant_matrix(size):
    # генерируем случайную матрицу
    matrix = np.random.rand(size, size)
    # делаем каждый элемент на диагонали по модулю больше суммы модулей остальных элементов в строке
    for i in range(size):
        diagonal_element = np.abs(matrix[i, i])
        row_sum = np.sum(np.abs(matrix[i, :])) - diagonal_element
        if row_sum >= diagonal_element:
            matrix[i, i] = row_sum + 1  # добавляем 1, чтобы сделать диагональ преобладающей
    b = np.random.rand(size)
    return matrix, b

def generate_diagonal_input_data(size):
    # генерируем диагональную матрицу коэффициентов
    matrix = np.diag(np.random.rand(size))
    b = np.random.rand(size)
    return matrix, b

def generate_singular_input_data(size):
    # генерируем вырожденную (с нулевым определителем) матрицу коэффициентов
    matrix = np.zeros((size, size))
    b = np.random.rand(size)
    return matrix, b
