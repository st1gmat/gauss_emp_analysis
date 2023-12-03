import time
import numpy as np
from gauss_mod import gauss_elimination_pivoting
from gauss_notmod import gauss_elimination
from generators import generate_input_data
import statistics

def measure_execution_time(algorithm, matrix, vector):
    start_time = time.time()
    solution = algorithm(matrix, vector)
    end_time = time.time()
    return end_time - start_time, solution

def calculate_accuracy(true_solution, computed_solution):
    return np.linalg.norm(true_solution - computed_solution)

def compare_solutions(true_solution, computed_solution, algorithm_name):
    accuracy = calculate_accuracy(true_solution, computed_solution)
    print(f"Погрешность решения для {algorithm_name}: {accuracy:.16f}")
    print("=" * 40)

def empirical_analysis():
    sizes = [10, 20, 40, 80, 160, 320]  # Размеры матрицы
    for size in sizes:
        time_mod_av = []
        time_notmod_av = []
        for i in range(1,21):
            # Измерение времени для модифицированного метода Гаусса
            A, b = generate_input_data(size)
            mod_time, mod_solution = measure_execution_time(gauss_elimination_pivoting, A.tolist(), b.tolist())
            # compare_solutions(np.linalg.solve(A, b), mod_solution, "Модифицированный метод Гаусса")
            time_mod_av.append(mod_time)

            # Измерение времени для обычного метода Гаусса
            A, b = generate_input_data(size)
            notmod_time, notmod_solution = measure_execution_time(gauss_elimination, A.tolist(), b.tolist())
            # compare_solutions(np.linalg.solve(A, b), notmod_solution, "Обычный метод Гаусса")
            time_notmod_av.append(notmod_time)

            # print(f"Размер матрицы: {size}")
            # print(f"Время выполнения для модифицированного метода Гаусса: {mod_time:.10f} секунд")
            # print(f"Время выполнения для обычного метода Гаусса: {notmod_time:.10f} секунд")
            # print("=" * 40)
        print("//"*20)
        print("Размер ", size)
        print(f"Среднее на 20 тестов время мод. метода {statistics.mean(time_mod_av):.20f}" )
        print(f"Среднее на 20 тестов время обычного метода{statistics.mean(time_notmod_av):.20f}"  )


if __name__ == "__main__":
    empirical_analysis()