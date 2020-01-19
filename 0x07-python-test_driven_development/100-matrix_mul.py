#!/usr/bin/python3
"""function that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_a must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_b for num in row]):

        if not all(len(row) == len(m_a[0]) for row in m_a):
            raise TypeError("each row of m_a must should be of the same size")
        if not all(len(row) == len(m_b[0]) for row in m_b):
            raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0] != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = []
    for row in m_a:
        new_row = []
        for col in invert_b:
            prod = 0
            for i in range(len(invert_b[0])):
                prod += row[i] * col[i]
            new_row.append(prod)
        new_matrix.append(new_row)

    new_matrix = []
    for row in m_a:
        new_row = []
        for col in invert_b:
            prod = 0
            for i in range(len(invert_b[0])):
                prod += row[i] * col[i]
            new_row.append(prod)
        new_matrix.append(new_row)

    return new_matrix
