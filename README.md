# S3


Motivated primarily by the Inverse Eigenvalue Problem, the mathematical community
has invested large amounts of time and energy into the study of the relation
between matrices and their eigenvalues. We contribute to that study by
examining which 3 × 3 sign patterns, matrices with non-numeric 0/+/- entries,
allow certain types of eigenvalues. In particular, we are interested in patterns
that allow refined inertia S3 = {(0, 3, 0, 0),(0, 2, 1, 0),(1, 2, 0, 0)}. In other words,
we seek patterns that have one realization with all negative real-part eigenvalues,
another with all negative real-part except for one zero eigenvalue, and a
third with all negative real-part except for one positive real-part eigenvalue. The
presence of this property is of particular interest, as it signals the presence of a
saddle-node bifurcation in the study of dynamical systems. We classify all 19,683
3×3 sign patterns, and determine which of these patterns allow this specific set of
eigenvalues. We also present a theorem for the extension of our work beyond 3×3
patterns.


## This repository contains the [script](https://github.com/kalapathar/S3/blob/master/categorise_s3.py) to categorise all 3 X 3 sign patterns. 


### Prerequisites
1. Sagemath (Python built)
2. Python Modules: operator,itertools,collections,random,time



## Example: 


[graph]: https://github.com/kalapathar/S3/blob/master/D1.PNG "Logo Title Text 2"

![alt text][graph]

![alt text](https://github.com/kalapathar/S3/blob/master/m_d1.PNG)

Suppose we want to categorise all patterns for this graph which its equivalent matrix under the graph. Code:
```

input_matrix=matrix(SR,[[a,b,0],[0,c,d],[e,0,f]])
D1=S3(input_matrix,6) #6 is the number of nonzeros in the matrix

```
Then D1.categorised will contain a list of lists that has the matrices categorised and D1 will plot the graphs which then can be used to see if the matrix allows S3 or not.

If you have further questions/comments, please email me at shah2 at stolaf.edu