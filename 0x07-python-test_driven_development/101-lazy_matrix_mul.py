#!/usr/bin/python3

"""Code defines a matrix's product function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Returns product of two matrices.

    Args:
        m_a (list of lists of ints/floats): first matrix to multiply.
        m_b (list of lists of ints/floats): second matrix to multiply.
    """

    return (np.matmul(m_a, m_b))
