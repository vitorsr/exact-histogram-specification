from numpy import array, clip, iinfo, linspace, uint64

from .imfilter import imfilter
from .imhistmatch import imhistmatch

# Filter bank $\Phi$
h = [
    array([], dtype="float64"),
    array([[1]], dtype="float64"),
    array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], dtype="float64") / 5,
    array([[1, 1, 1], [1, 1, 1], [1, 1, 1]], dtype="float64") / 9,
    array(
        [
            [0, 0, 1, 0, 0],
            [0, 1, 1, 1, 0],
            [1, 1, 1, 1, 1],
            [0, 1, 1, 1, 0],
            [0, 0, 1, 0, 0],
        ],
        dtype="float64",
    )
    / 13,
    array(
        [
            [0, 1, 1, 1, 0],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [0, 1, 1, 1, 0],
        ],
        dtype="float64",
    )
    / 21,
    array(
        [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
        ],
        dtype="float64",
    )
    / 25,
]


def peakval(A):
    if A.dtype.name.startswith("float"):
        if A.max() > 1.0:
            return A.max()
        else:
            return 1.0
    elif A.dtype.name.startswith("uint"):
        return iinfo(A.dtype).max
    else:
        raise TypeError("Supported dtypes: floating-point and unsigned integers.")


def lex(A, K=6):
    """Lexicographic trick (finite sets)"""
    PEAKVAL = peakval(A)
    B = uint64(511 / PEAKVAL * A)  # Make B at most 9 bits wide.
    L = uint64(2048)  # (L - 1) has 11 bits.

    if K > 1:
        for i in range(2, K + 1):
            B = L * B  # Multiplying by L shifts B[r, c] 11 bits to the left.
            B += uint64((L - 1) / PEAKVAL * clip(imfilter(A, h[i]), 0, PEAKVAL))

    return B


def ehs(A, ref=None, K=6):
    if ref is None:
        ref = linspace(0, 255, num=256, dtype="uint8")

    return imhistmatch(lex(A, K=K), ref)
