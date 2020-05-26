from numpy import cumsum, empty, intp, unique


def _imhistmatch(I_inverse, I_counts, ref_unique, ref_counts):
    I_unique = empty(len(I_counts), dtype=ref_unique.dtype)
    ir = intp(0)

    for iI in range(len(I_counts)):
        while I_counts[iI] > ref_counts[ir]:
            ir += 1
        I_unique[iI] = ref_unique[ir]

    return I_unique[I_inverse]


def imhistmatch(I, ref):
    """J = imhistmatch(I, ref)"""
    _, I_inverse, I_counts = unique(I, return_inverse=True, return_counts=True)
    I_counts = cumsum(I_counts)
    I_counts = I_counts / I_counts[-1]  # (This is a CDF proper.)

    ref_unique, ref_counts = unique(ref, return_counts=True)
    ref_counts = cumsum(ref_counts)
    ref_counts = ref_counts / ref_counts[-1]

    return _imhistmatch(I_inverse, I_counts, ref_unique, ref_counts).reshape(I.shape)
