from numpy import array
from numpy.testing import assert_array_almost_equal

from ehs.imfilter import imfilter

A = []
A.append(array([[1, 3], [4, 2]], dtype="uint8"))
A.append(array([[8, 1, 6], [3, 5, 7], [4, 9, 2]], dtype="uint8"))

h = []
h.append(array([[1.0]]))
h.append(array([[0.1, 0.3], [0.2, 0.4]]))
h.append(array([[0.3, 0.2, 0.1], [0.2, 0.15, 0.05]]))

B = []
B.append(array([[1.0, 3.0], [4.0, 2.0]]))
B.append(array([[2.6, 2.4], [2.6, 2.0]]))
B.append(array([[2.3, 2.4], [3.7, 3.0]]))
B.append(array([[8.0, 1.0, 6.0], [3.00, 5.00, 7.0], [4.00, 9.00, 2.0]]))
B.append(array([[3.7, 5.7, 6.6], [6.20, 5.20, 4.0], [7.50, 4.10, 2.0]]))
B.append(array([[5.4, 4.9, 4.5], [3.85, 4.85, 5.8], [4.75, 5.45, 5.5]]))


def test_imfilter():
    for m in range(len(A)):
        for n in range(len(h)):
            # Integer A.
            assert_array_almost_equal(imfilter(A[m], h[n]), B[m * len(h) + n])
            # Floating-point A.
            assert_array_almost_equal(imfilter(1.0 * A[m], h[n]), B[m * len(h) + n])
