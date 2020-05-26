from imageio import imread
from numpy import ascontiguousarray, concatenate, cumsum, linspace, uint64, unique
from numpy.testing import assert_array_equal

from ehs.imhistmatch import imhistmatch


def test_imhistmatch():
    A = linspace(0, 255, num=256, dtype="uint8")

    # Floating-point support.
    assert_array_equal(imhistmatch(A / A.max(), A), A)

    # Scale-invariant.
    for i in range(6):
        assert_array_equal(imhistmatch(uint64(2048 ** i) * uint64(A), A), A)

    A = ascontiguousarray(imread("images/lena.png"))
    B = ascontiguousarray(imread("images/boat.png"))

    C = imhistmatch(A, B)

    _, A_counts = unique(
        concatenate((A.ravel(), linspace(0, 255, num=256, dtype=A.dtype))),
        return_counts=True,
    )
    _, B_counts = unique(
        concatenate((B.ravel(), linspace(0, 255, num=256, dtype=B.dtype))),
        return_counts=True,
    )
    _, C_counts = unique(
        concatenate((C.ravel(), linspace(0, 255, num=256, dtype=C.dtype))),
        return_counts=True,
    )

    A_counts = cumsum((A_counts - 1)) / A.size
    B_counts = cumsum((B_counts - 1)) / B.size
    C_counts = cumsum((C_counts - 1)) / C.size

    # Assert small mean-squared error between CDFs.
    assert ((A_counts - C_counts) ** 2).mean() > ((B_counts - C_counts) ** 2).mean()
    assert ((B_counts - C_counts) ** 2).mean() < 1e-5
