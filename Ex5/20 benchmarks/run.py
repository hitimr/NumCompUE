#!/usr/bin/env python3
import os
from sys import platform
import subprocess

perf_command = "perf stat -B"
n = 10

if platform == "linux" or platform == "linux2":
    os.system("python3 generate_inputs.py "+str(n))

    # inner products
    fileName = "inner_products.txt"
    os.system(perf_command + "python3 innerProduct_pythonLoops.py > out/inner_product.txt")
    os.system(perf_command + "innerProduct_numpy.py >> out/inner_product.txt")

    # matrix vector multiplication
    os.system(perf_command + "matrixVector_pythonLoops.py > out/matrix_vector_mult.txt")
    os.system(perf_command + "matrixVector_numpy.py >> out/matrix_vector_mult.txt")