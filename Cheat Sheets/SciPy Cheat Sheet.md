SciPy Cheat Sheet
Interacting With NumPy Also see NumPy
The SciPy library is one of the core packages for
scientific computing that provides mathematical
algorithms and convenience functions built on the
NumPy extension of Python.
Index Tricks
* <code>np.mgrid[0:5,0:5] Create a dense meshgrid</code>
* <code>np.ogrid[0:2,0:2] Create an open meshgrid</code>
* <code>np.r_[[3,[0]*5,-1:1:10j] Stack arrays vertically (row-wise)</code>
* <code>np.c_[b,c] Create stacked column-wise arrays</code>
Shape Manipulation
Polynomials
Vectorizing Functions
Type Handling
* <code>np.angle(b,deg=True) Return the angle of the complex argument</code>
* <code>g = np.linspace(0,np.pi,num=5) Create an array of evenly spaced values</code>
> > > g [ 3 : ] + = n p . p i (number of samples)
* <code>np.unwrap(g) Unwrap</code>
* <code>np.logspace(0,10,3) Create an array of evenly spaced values (log scale)</code>
* <code>np.select([c<4],[c*2]) Return values from a list of arrays depending on</code>
conditions
* <code>misc.factorial(a) Factorial</code>
* <code>misc.comb(10,3,exact=True) Combine N things taken at k time</code>
* <code>misc.central_diff_weights(3) Weights for Np-point central derivative</code>
* <code>misc.derivative(myfunc,1.0) Find the n-th derivative of a function at a point</code>
Other Useful Functions
* <code>np.real(c) Return the real part of the array elements</code>
* <code>np.imag(c) Return the imaginary part of the array elements</code>
* <code>np.real_if_close(c,tol=1000) Return a real array if complex parts close to 0</code>
* <code>np.cast['f'](np.pi) Cast object to a data type</code>
* <code>def myfunc(a):</code>
if a < 0:
return a*2
else:
return a/2
* <code>np.vectorize(myfunc) Vectorize functions</code>
* <code>from numpy import poly1d</code>
* <code>p = poly1d([3,4,5]) Create a polynomial object</code>
* <code>np.transpose(b) Permute array dimensions</code>
* <code>b.flatten() Flatten the array</code>
* <code>np.hstack((b,c)) Stack arrays horizontally (column-wise)</code>
* <code>np.vstack((a,b)) Stack arrays vertically (row-wise)</code>
* <code>np.hsplit(c,2) Split the array horizontally at the 2nd index</code>
* <code>np.vpslit(d,2) Split the array vertically at the 2nd index</code>
* <code>import numpy as np</code>
* <code>a = np.array([1,2,3])</code>
* <code>b = np.array([(1+5j,2j,3j), (4j,5j,6j)])</code>
* <code>c = np.array([[(1.5,2,3), (4,5,6)], [(3,2,1), (4,5,6)]])</code>
* <code>help(scipy.linalg.diagsvd)</code>
* <code>np.info(np.matrix)</code>
Linear Algebra
You’ll use the linalg and sparse modules. Note that scipy.linalg contains and expands on numpy.linalg.
* <code>from scipy import linalg, sparse</code>
Creating Matrices
* <code>A = np.matrix(np.random.random((2,2)))</code>
* <code>B = np.asmatrix(b)</code>
* <code>C = np.mat(np.random.random((10,5)))</code>
* <code>D = np.mat([[3,4], [5,6]])</code>
Also see NumPy
Basic Matrix Routines
Inverse
* <code>A.I Inverse</code>
* <code>linalg.inv(A) Inverse</code>
* <code>A.T Tranpose matrix</code>
* <code>A.H Conjugate transposition</code>
* <code>np.trace(A) Trace</code>
Norm
* <code>linalg.norm(A) Frobenius norm</code>
* <code>linalg.norm(A,1) L1 norm (max column sum)</code>
* <code>linalg.norm(A,np.inf) L inf norm (max row sum)</code>
Rank
* <code>np.linalg.matrix_rank(C) Matrix rank</code>
Determinant
* <code>linalg.det(A) Determinant</code>
Solving linear problems
* <code>linalg.solve(A,b) Solver for dense matrices</code>
* <code>E = np.mat(a).T Solver for dense matrices</code>
* <code>linalg.lstsq(D,E) Least-squares solution to linear matrix</code>
equation
Generalized inverse
* <code>linalg.pinv(C) Compute the pseudo-inverse of a matrix</code>
(least-squares solver)
* <code>linalg.pinv2(C) Compute the pseudo-inverse of a matrix</code>
(SVD)
Addition
* <code>np.add(A,D) Addition</code>
Subtraction
* <code>np.subtract(A,D) Subtraction</code>
Division
* <code>np.divide(A,D) Division</code>
Multiplication
* <code>np.multiply(D,A) Multiplication</code>
* <code>np.dot(A,D) Dot product</code>
* <code>np.vdot(A,D) Vector dot product</code>
* <code>np.inner(A,D) Inner product</code>
* <code>np.outer(A,D) Outer product</code>
* <code>np.tensordot(A,D) Tensor dot product</code>
* <code>np.kron(A,D) Kronecker product</code>
Exponential Functions
* <code>linalg.expm(A) Matrix exponential</code>
* <code>linalg.expm2(A) Matrix exponential (Taylor Series)</code>
* <code>linalg.expm3(D) Matrix exponential (eigenvalue</code>
decomposition)
Logarithm Function
* <code>linalg.logm(A) Matrix logarithm</code>
Trigonometric Tunctions
* <code>linalg.sinm(D) Matrix sine</code>
* <code>linalg.cosm(D) Matrix cosine</code>
* <code>linalg.tanm(A) Matrix tangent</code>
Hyperbolic Trigonometric Functions
* <code>linalg.sinhm(D) Hypberbolic matrix sine</code>
* <code>linalg.coshm(D) Hyperbolic matrix cosine</code>
* <code>linalg.tanhm(A) Hyperbolic matrix tangent</code>
Matrix Sign Function
* <code>np.sigm(A) Matrix sign function</code>
Matrix Square Root
* <code>linalg.sqrtm(A) Matrix square root</code>
Arbitrary Functions
* <code>linalg.funm(A, lambda x: x*x) Evaluate matrix function</code>
Matrix Functions
Asking For Help
Decompositions
Eigenvalues and Eigenvectors
* <code>la, v = linalg.eig(A) Solve ordinary or generalized</code>
eigenvalue problem for square matrix
* <code>l1, l2 = la Unpack eigenvalues</code>
* <code>v[:,0] First eigenvector</code>
* <code>v[:,1] Second eigenvector</code>
* <code>linalg.eigvals(A) Unpack eigenvalues</code>
Singular Value Decomposition
* <code>U,s,Vh = linalg.svd(B) Singular Value Decomposition (SVD)</code>
* <code>M,N = B.shape</code>
* <code>Sig = linalg.diagsvd(s,M,N) Construct sigma matrix in SVD</code>
LU Decomposition
* <code>P,L,U = linalg.lu(C) LU Decomposition</code>
* <code>F = np.eye(3, k=1) Create a 2X2 identity matrix</code>
* <code>G = np.mat(np.identity(2)) Create a 2x2 identity matrix</code>
* <code>C[C > 0.5] = 0</code>
* <code>H = sparse.csr_matrix(C) Compressed Sparse Row matrix</code>
* <code>I = sparse.csc_matrix(D) Compressed Sparse Column matrix</code>
* <code>J = sparse.dok_matrix(A) Dictionary Of Keys matrix</code>
* <code>E.todense() Sparse matrix to full matrix</code>
* <code>sparse.isspmatrix_csc(A) Identify sparse matrix</code>
Creating Sparse Matrices
Inverse
* <code>sparse.linalg.inv(I) Inverse</code>
Norm
* <code>sparse.linalg.norm(I) Norm</code>
Solving linear problems
* <code>sparse.linalg.spsolve(H,I) Solver for sparse matrices</code>
Sparse Matrix Routines
Sparse Matrix Functions
* <code>sparse.linalg.expm(I) Sparse matrix exponential</code>
Sparse Matrix Decompositions
* <code>la, v = sparse.linalg.eigs(F,1) Eigenvalues and eigenvectors</code>
* <code>sparse.linalg.svds(H, 2) SVD</code>



### References
[www.datacamp.com](www.datacamp.com)
