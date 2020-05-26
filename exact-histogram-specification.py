#!/usr/bin/env python3
from argparse import ArgumentParser

from imageio import imread, imwrite
from numpy import ascontiguousarray, uint8

from ehs.ehs import ehs

if __name__ == "__main__":
    parser = ArgumentParser(
        description="""
        Helper script to parse arguments to the ehs function in ehs/ehs.py. If the
        output filename is not given, the script outputs the result to "output.png".
        Also, if the reference is unspecified, the reference is such that we obtain
        histogram equalization. The ehs function implements the algorithm described in
        [1] for histogram specification. Refer to it for more information.
        """,
        epilog="""
        [1] Coltuc, D., P. Bolon, and J.-M. Chassery. 2006. “Exact Histogram
        Specification.” IEEE Transactions on Image Processing 15 (5): 1143–52.
        https://doi.org/10.1109/tip.2005.864170.
        """,
    )

    parser.add_argument("input", help="input image filename")
    parser.add_argument(
        "-o", "--output", default="output.png", help="output image filename"
    )
    parser.add_argument("-r", "--ref", default=None, help="reference image filename")
    parser.add_argument(
        "-k",
        "--k",
        default=6,
        type=int,
        choices=range(1, 7),
        help="number of filters to apply (1 is the identity)",
    )

    args = parser.parse_args()
    print(args)

    A = ascontiguousarray(imread(args.input))

    if args.ref is not None or args.ref == "None":
        ref = ascontiguousarray(imread(args.ref))
    else:
        ref = args.ref  # None

    imwrite(args.output, uint8(ehs(A, ref=ref, K=args.k)))
