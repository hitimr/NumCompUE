#!/bin/sh

N=100
PERF_COMMAND="perf stat --no-big-num --repeat=5 -e instructions,cpu-clock"

echo Building files
#make # build c++ files

# delete old contents
echo > inner_product.txt
echo > matrix_vector_mult.txt
echo > matrix_matrix_mult.txt

# measure different N
for N in 10 20
do
    echo Running for n=$N
    # Generate Inputs
    python3 generate_inputs.py $N

    # inner products
    echo "###" n= >> inner_product.txt
    echo $N >> inner_product.txt
    $PERF_COMMAND python3 innerProduct_pythonLoops.py >> inner_product.txt 2>&1
    $PERF_COMMAND python3 innerProduct_numpy.py >> inner_product.txt 2>&1
    $PERF_COMMAND ./innerProduct_eigen >> inner_product.txt 2>&1

    # matrix vector multiplication
    echo "###" n= >> matrix_vector_mult.txt
    echo $N >> matrix_vector_mult.txt
    $PERF_COMMAND python3 matrixVector_pythonLoops.py >> matrix_vector_mult.txt 2>&1
    $PERF_COMMAND python3 matrixVector_numpy.py >> matrix_vector_mult.txt 2>&1
    $PERF_COMMAND ./matrixVector_eigen >> matrix_vector_mult.txt 2>&1

    # matrix matrix multiplication
    echo "###" n=>> matrix_matrix_mult.txt
    echo $N >> matrix_matrix_mult.txt
    $PERF_COMMAND python3 matrixMatrix_pythonLoops.py >> matrix_matrix_mult.txt 2>&1
    $PERF_COMMAND python3 matrixMatrix_numpy.py >> matrix_matrix_mult.txt 2>&1
    $PERF_COMMAND ./matrixMatrix_eigen >> matrix_matrix_mult.txt 2>&1

done