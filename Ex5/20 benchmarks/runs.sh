#!/bin/sh

N=100
PERF_COMMAND="perf stat -e instructions,cpu-clock python3"


# delete old contents
echo > inner_product.txt
echo > matrix_vector_mult.txt
echo > matrix_matrix_mult.txt

# measure different N
for N in 100 200 300
do
    # Generate Inputs
    python3 generate_inputs.py $N

    # inner products
    echo n=$N >> inner_product.txt
    $PERF_COMMAND innerProduct_pythonLoops.py >> inner_product.txt 2>&1
    $PERF_COMMAND innerProduct_numpy.py >> inner_product.txt 2>&1


    # matrix vector multiplication
    echo n=$N >> matrix_vector_mult.txt
    $PERF_COMMAND matrixVector_pythonLoops.py >> matrix_vector_mult.txt 2>&1
    $PERF_COMMAND matrixVector_numpy.py >> matrix_vector_mult.txt 2>&1

    echo n=$N >> matrix_matrix_mult.txt
    $PERF_COMMAND matrixmatrix_pythonLoops.py >> matrix_matrix_mult.txt 2>&1
    $PERF_COMMAND matrixmatrix_numpy.py >> matrix_matrix_mult.txt 2>&1

done