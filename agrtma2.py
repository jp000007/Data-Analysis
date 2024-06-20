# -*- coding: utf-8 -*-
"""AgrtmA2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MaHuH9EOjZPr_a3rfVNE0X8T9PVtclTD
"""

pip install --upgrade numpy

import numpy as np
import time

def standard_matrix_multiply(A, B):
    return np.dot(A, B)

def strassen_matrix_multiply(A, B):
    n = len(A)

    if n <= 64:  # Base case threshold for standard multiplication
        return np.dot(A, B)

    # Matrix split
    m = n // 2
    A11, A12 = A[:m, :m], A[:m, m:]
    A21, A22 = A[m:, :m], A[m:, m:]
    B11, B12 = B[:m, :m], B[:m, m:]
    B21, B22 = B[m:, :m], B[m:, m:]

    # Strassen's algorithm
    P1 = strassen_matrix_multiply(A11 + A22, B11 + B22)
    P2 = strassen_matrix_multiply(A21 + A22, B11)
    P3 = strassen_matrix_multiply(A11, B12 - B22)
    P4 = strassen_matrix_multiply(A22, B21 - B11)
    P5 = strassen_matrix_multiply(A11 + A12, B22)
    P6 = strassen_matrix_multiply(A21 - A11, B11 + B12)
    P7 = strassen_matrix_multiply(A12 - A22, B21 + B22)

    # Calculate submatrices of the result
    C11 = P1 + P4 - P5 + P7
    C12 = P3 + P5
    C21 = P2 + P4
    C22 = P1 - P2 + P3 + P6

    # Combine submatrices into the result matrix
    C = np.zeros((n, n))
    C[:m, :m], C[:m, m:], C[m:, :m], C[m:, m:] = C11, C12, C21, C22

    return C

def test_algorithm_performance(n, algorithm_function, matrix_generator):
    A = matrix_generator(n, n)
    B = matrix_generator(n, n)

    start_time = time.time()
    result = algorithm_function(A, B)
    end_time = time.time()

    execution_time = end_time - start_time
    return result, execution_time

# Matrix size creation function
def generate_random_matrix(rows, cols):
    return np.random.rand(rows, cols)

# Case 1: n = 50
result_standard, time_standard = test_algorithm_performance(1088, standard_matrix_multiply, generate_random_matrix)
result_strassen, time_strassen = test_algorithm_performance(1088, strassen_matrix_multiply, generate_random_matrix)

# Check if the results are the same for Case 1
print("Case 1: Results are close:", np.allclose(result_standard, result_strassen))

# Print execution times
print("Case 1: Standard Method Time =", time_standard, "seconds, Strassen's Time =", time_strassen, "seconds")

import numpy as np
import time

def standard_matrix_multiply(A, B):
    return np.dot(A, B)

# Matrix size creation function
def generate_random_matrix(rows, cols):
    return np.random.rand(rows, cols)

# Case: n = 500
A = generate_random_matrix(500, 500)
B = generate_random_matrix(500, 500)

start_time = time.time()
result_standard = standard_matrix_multiply(A, B)
end_time = time.time()

execution_time = end_time - start_time

# Print execution time
print("Standard Matrix Multiplication Time for 500x500 matrix:", execution_time, "seconds")

import numpy as np

def strassen_matrix_multiply(A, B):
    n = len(A)

    if n <= 64:  # Base case threshold for standard multiplication
        return np.dot(A, B)

    # Matrix split
    m = n // 2
    A11, A12 = A[:m, :m], A[:m, m:]
    A21, A22 = A[m:, :m], A[m:, m:]
    B11, B12 = B[:m, :m], B[:m, m:]
    B21, B22 = B[m:, :m], B[m:, m:]

    # Strassen's algorithm
    P1 = strassen_matrix_multiply(A11 + A22, B11 + B22)
    P2 = strassen_matrix_multiply(A21 + A22, B11)
    P3 = strassen_matrix_multiply(A11, B12 - B22)
    P4 = strassen_matrix_multiply(A22, B21 - B11)
    P5 = strassen_matrix_multiply(A11 + A12, B22)
    P6 = strassen_matrix_multiply(A21 - A11, B11 + B12)
    P7 = strassen_matrix_multiply(A12 - A22, B21 + B22)

    # Calculate submatrices of the result
    C11 = P1 + P4 - P5 + P7
    C12 = P3 + P5
    C21 = P2 + P4
    C22 = P1 - P2 + P3 + P6

    # Combine submatrices into the result matrix
    C = np.zeros((n, n))
    C[:m, :m], C[:m, m:], C[m:, :m], C[m:, m:] = C11, C12, C21, C22

    return C

# Matrix size creation function
def generate_random_matrix(rows, cols):
    return np.random.rand(rows, cols)

# Example: n = 256
n = 256
A = generate_random_matrix(n, n)
B = generate_random_matrix(n, n)

result_strassen = strassen_matrix_multiply(A, B)
print("Strassen's Matrix Multiplication Result for", n, "x", n, "matrix:")
print(result_strassen)

import numpy as np
import time

def strassen_matrix_multiply(A, B):
    n = len(A)

    if n <= 64:  # Base case threshold for standard multiplication
        return np.dot(A, B)

    # Matrix split
    m = n // 2
    A11, A12 = A[:m, :m], A[:m, m:]
    A21, A22 = A[m:, :m], A[m:, m:]
    B11, B12 = B[:m, :m], B[:m, m:]
    B21, B22 = B[m:, :m], B[m:, m:]

    # Strassen's algorithm
    P1 = strassen_matrix_multiply(A11 + A22, B11 + B22)
    P2 = strassen_matrix_multiply(A21 + A22, B11)
    P3 = strassen_matrix_multiply(A11, B12 - B22)
    P4 = strassen_matrix_multiply(A22, B21 - B11)
    P5 = strassen_matrix_multiply(A11 + A12, B22)
    P6 = strassen_matrix_multiply(A21 - A11, B11 + B12)
    P7 = strassen_matrix_multiply(A12 - A22, B21 + B22)

    # Calculate submatrices of the result
    C11 = P1 + P4 - P5 + P7
    C12 = P3 + P5
    C21 = P2 + P4
    C22 = P1 - P2 + P3 + P6

    # Combine submatrices into the result matrix
    C = np.zeros((n, n))
    C[:m, :m], C[:m, m:], C[m:, :m], C[m:, m:] = C11, C12, C21, C22

    return C

# Matrix size creation function
def generate_random_matrix(rows, cols):
    return np.random.rand(rows, cols)

# Example: n = 256
n = 400
A = generate_random_matrix(n, n)
B = generate_random_matrix(n, n)

start_time = time.time()
result_strassen = strassen_matrix_multiply(A, B)
end_time = time.time()

execution_time = end_time - start_time

print("Strassen's Matrix Multiplication Result for", n, "x", n, "matrix:")
print(result_strassen)
print("Execution Time:", execution_time, "seconds")

import numpy as np
import time

def standard_matrix_multiply(A, B):
    return np.dot(A, B)

def strassen_matrix_multiply(A, B):
    n = len(A)

    if n <= 64:  # Base case threshold for standard multiplication
        return np.dot(A, B)

    # Matrix split
    m = n // 2
    A11, A12 = A[:m, :m], A[:m, m:]
    A21, A22 = A[m:, :m], A[m:, m:]
    B11, B12 = B[:m, :m], B[:m, m:]
    B21, B22 = B[m:, :m], B[m:, m:]

    # Strassen's algorithm
    P1 = strassen_matrix_multiply(A11 + A22, B11 + B22)
    P2 = strassen_matrix_multiply(A21 + A22, B11)
    P3 = strassen_matrix_multiply(A11, B12 - B22)
    P4 = strassen_matrix_multiply(A22, B21 - B11)
    P5 = strassen_matrix_multiply(A11 + A12, B22)
    P6 = strassen_matrix_multiply(A21 - A11, B11 + B12)
    P7 = strassen_matrix_multiply(A12 - A22, B21 + B22)

    # Calculate submatrices of the result
    C11 = P1 + P4 - P5 + P7
    C12 = P3 + P5
    C21 = P2 + P4
    C22 = P1 - P2 + P3 + P6

    # Combine submatrices into the result matrix
    C = np.zeros((n, n))
    C[:m, :m], C[:m, m:], C[m:, :m], C[m:, m:] = C11, C12, C21, C22

    return C

def test_algorithm_performance(n, algorithm_function, matrix_generator):
    A = matrix_generator(n, n)
    B = matrix_generator(n, n)

    start_time = time.time()
    result = algorithm_function(A, B)
    end_time = time.time()

    execution_time = end_time - start_time
    return result, execution_time

# Matrix size creation function
def generate_random_matrix(rows, cols):
    return np.random.rand(rows, cols)

# Case 1: n = 50
result_standard, time_standard = test_algorithm_performance(10240, standard_matrix_multiply, generate_random_matrix)
result_strassen, time_strassen = test_algorithm_performance(10240, strassen_matrix_multiply, generate_random_matrix)

# Check if the results are the same for Case 1
print("Case 1: Results are close:", np.allclose(result_standard, result_strassen))

# Print execution times
print("Case 1: Standard Method Time =", time_standard, "seconds, Strassen's Time =", time_strassen, "seconds")