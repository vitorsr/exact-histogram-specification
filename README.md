```
usage: exact-histogram-specification.py [-h] [-o OUTPUT] [-r REF] [-k {1,2,3,4,5,6}] input

Helper script to parse arguments to the ehs function in ehs/ehs.py. If the output filename is
not given, the script outputs the result to "output.png". Also, if the reference is unspecified,
the reference is such that we obtain histogram equalization. The ehs function implements the
algorithm described in [1] for histogram specification. Refer to it for more information.

positional arguments:
  input                 input image filename

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        output image filename
  -r REF, --ref REF     reference image filename
  -k {1,2,3,4,5,6}, --k {1,2,3,4,5,6}
                        number of filters to apply (1 is the identity)

[1] Coltuc, D., P. Bolon, and J.-M. Chassery. 2006. “Exact Histogram Specification.” IEEE
Transactions on Image Processing 15 (5): 1143–52. https://doi.org/10.1109/tip.2005.864170.
```
