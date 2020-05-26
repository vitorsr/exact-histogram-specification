from numpy import array, block, pad, roll, rot90, zeros
from numpy.fft import fft2, ifft2


def imfilter(A, h):
    """B = imfilter(A, h, "replicate")"""
    A = A.copy().astype("float64")
    h = rot90(h, k=2).copy()

    r = array(h.shape) // 2  # Radius.
    A = pad(A, r, mode="edge")

    h = block(
        [
            [h, zeros((h.shape[0], A.shape[1] - h.shape[1]))],
            [zeros((A.shape[0] - h.shape[0], A.shape[1]))],
        ]
    )

    h = roll(h, -r, (0, 1))  # circshift.

    return ifft2(fft2(A) * fft2(h)).real[
        r[0] : A.shape[0] - r[0], r[1] : A.shape[1] - r[1]
    ]
