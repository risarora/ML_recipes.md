# NumPy Cheat Sheet

The NumPy library is the core library for scientific computing in Python. It provides a high-performance multidimensional array object, and tools for working with these arrays.

<code> import numpy as np </code>

### Data Types
* np.int64 *:* *Signed 64-bit integer types  *
* np.float32  *:* *Standard double-precision floating point*  
* np.complex  *:* *Complex numbers represented by 128 floats*  
* np.bool  *:* *Boolean type storing TRUE and FALSE values*  
* np.object  *:* *Python object type*  
* np.string_  *:* *Fixed-length string type*  
* np.unicode_  *:* *Fixed-length unicode type*  


### Creating Arrays
```
 a = np.array([1,2,3])
 b = np.array([(1.5,2,3), (4,5,6)], dtype = float)
 c = np.array([[(1.5,2,3), (4,5,6)], [(3,2,1), (4,5,6)]],
 dtype = float)
```

### Creating placeholder Arrays

* _Create an array of zeros_<code> np.zeros((3,4)) </code>
* _Create an array of ones_<code> np.ones((2,3,4),dtype=np.int16) </code>
* _Create an array of evenly spaced values (step value)_<code> d = np.arange(10,25,5) </code>
* _Create an array of evenly spaced values (number of samples)_<code> np.linspace(0,2,9) </code>
* _Create a constant array_<code> e = np.full((2,2),7) </code>
* _Create a 2X2 identity matrix_<code> f = np.eye(2) </code>
* _Create an array with random values_<code> np.random.random((2,2)) </code>
* _Create an empty array_<code> np.empty((3,2)) </code>
* _Create random arrays_<code> np.random.rand(6,7)*100 </code> floats between 0-100
* _Create random int_<code> np.random.randint(5,size=(2,3)) </code> 2x3 array with random ints between 0-4


#### Inspecting Your Array
*  Array dimensions <code> a.shape</code>
*  Length of array <code> len(a)</code>
*  Number of array dimensions <code> b.ndim</code>
*  Number of array elements <code> e.size</code>
*  Data type of array elements <code> b.dtype</code>
*  Name of data type <code> b.dtype.name</code>
*  Convert an array to a different type <code> b.astype(int)</code>


### Array Mathematics

Code | Operations
---|---
<code> b + a </code>   <br> array([[ 2.5, 4. , 6. ], [ 5. , 7. , 9. ]]) | Addition
<code> np.add(b,a) </code> <br> array([[ 2.5, 4. , 6. ], [ 5. , 7. , 9. ]]) |Addition
<code> a / b </code>    <br>array([[ 0.66666667, 1. , 1. ], [ 0.25 , 0.4 , 0.5 ]]) |Division
<code> np.divide(a,b) </code>    | Division
<code> a * b  </code>    <br>array([[ 1.5, 4. , 9. ],  [ 4. , 10. , 18. ]]) | Multiplication
<code> np.multiply(a,b) </code>    | Multiplication
<code> np.exp(b) </code>    | Exponentiation
<code> np.sqrt(b) </code>    | Square root
<code> np.sin(a) </code>    | Print sines of an Array
<code> np.cos(b) </code>    | Element-wise cosine
<code> np.log(a) </code>    | Element-wise natural logarithm
<code> e.dot(f) </code>    array([[ 7., 7.],  [ 7., 7.]]) | Dot product

#### Aggregate Functions
<code> a.sum() Array-wise sum </code>   
<code> a.min() Array-wise minimum value </code>    
<code> b.max(axis=0) Maximum value of an array row </code>
<code> b.cumsum(axis=1) Cumulative sum of the elements </code>
<code> a.mean() Mean </code>
<code> b.median() Median </code>
<code> a.corrcoef() Correlation coefficient </code>
<code> np.std(b) Standard deviation </code>

### Comparison
##### Element-wise comparison
*  <code> a == b</code>
```
array([[False, True, True],
 [False, False, False]], dtype=bool)
 ```

* <code> a < 2  </code>

  ```
  array([True, False, False], dtype=bool)
  ```

##### Array-wise comparison
* <code> np.array_equal(a, b) </code>

```
array([[False, True, True],
 [False, False, False]], dtype=bool)
```

 #### Copying Arrays
 * Create a view of the array with the same data: <code> h = a.view()</code>
 * Create a copy of the array: <code> np.copy(a)</code>
 * Create a deep copy of the array: <code> h = a.copy()</code>

### Array Manipulation

##### Transposing Array - Permute array dimensions
* <code> i = np.transpose(b)  </code>
* <code> i.T  </code>

##### Changing Array Shape
* Flatten the array  <code> b.ravel() </code>
* Reshape, but don’t change data <code> g.reshape(3,-2)  </code>

##### Adding/Removing Elements  
* Return a new array with shape (2,6) -<code> h.resize((2,6)) </code>
* Append items to an array -<code> np.append(h,g) </code>
* Insert items in an array -<code> np.insert(a, 1, 5)</code>
* Delete items from an array -<code> np.delete(a,[1]) </code>

##### Combining Arrays

* Concatenate Arrays

```
np.concatenate((a,d),axis=0)
Concatenate arrays
 array([ 1, 2, 3, 10, 15, 20])
```

* Vertically Stack the arrays

```
np.vstack((a,b))
Stack arrays vertically (row-wise)
 array([[ 1. , 2. , 3. ],
        [ 1.5, 2. , 3. ],
        [ 4. , 5. , 6. ]])
```

* Stack arrays vertically (row-wise)

```
np.r_[e,f]

```

* Stack arrays horizontally (column-wise)

```
np.hstack((e,f))

array([[ 7., 7., 1., 0.],
        [ 7., 7., 0., 1.]])
 ```

* Create stacked column-wise arrays

```
np.column_stack((a,d))
 array([[ 1, 10],
        [ 2, 15],
        [ 3, 20]])
 ```

* Create stacked column-wise arrays

```
np.c_[a,d]
```

##### Splitting Arrays
* Split the array horizontally
```
np.hsplit(a,3)
Split the array horizontally at the 3rd
[array([1]),array([2]),array([3])] index
```
* Split the array vertically
```
np.vsplit(c,2)
Split the array vertically at the 2nd index
  [
  array([[[ 1.5, 2. , 1. ],
          [ 4. , 5. , 6. ]]]),
  array([[[ 3., 2., 3.],
          [ 4., 5., 6.]]])
  ]
```
#### Subsetting, Slicing, Indexing

##### Subsetting
* <code> a[2] </code>  Select the element at the 2nd index 3  
* <code> b[1,2] </code>
Select the element at row 1 column 2 6.0 (equivalent to b[1][2])

#### Slicing
* <code> a[0:2] </code>
 array([1, 2]) #Select items at index 0 and 1   
* <code> b[0:2,1] </code>
 array([ 2., 5.]) #Select items at rows 0 and 1 in column 1
* <code> b[:1] </code>
 array([[1.5, 2., 3.]]) (equivalent to b[0:1, :]) #Select all items at row 0    
* <code> c[1,...] </code>
 array([[[ 3., 2., 1.], [ 4., 5., 6.]]]) #Same as [1,:,:]
* <code> a[ : :-1] </code> Reversed array a array([3, 2, 1])

##### Boolean Indexing
* Select elements from a less than 2  
```
a[a<2]   
array([1])
```


##### Fancy Indexing

* Select elements (1,0),(0,1),(1,2) and (0,0)   
<code> b[[1, 0, 1, 0],[0, 1, 2, 0]]  </code>
array([ 4. , 2. , 6. , 1.5])

* Select a subset of the matrix’s rows   
<code> b[[1, 0, 1, 0]][:,[0,1,2,0]] </code>

```
array([[ 4. ,5. , 6. , 4. ], and columns
 [ 1.5, 2. , 3. , 1.5],
 [ 4. , 5. , 6. , 4. ],
 [ 1.5, 2. , 3. , 1.5]])
```

####  Saving and Loading Text Files

* <code> np.loadtxt("myfile.txt") </code>    
* <code> np.genfromtxt("my_file.csv", delimiter=',') </code>    
* <code> np.savetxt("myarray.txt", a, delimiter=" ") </code>    
```
I/O
1 2 3
1.5 2 3
4 5 6
```

#### Saving & Loading On Disk
* <code> np.save('my_array', a) </code>    
* <code> np.savez('array.npz', a, b) </code>    
* <code> np.load('my_array.npy') </code>    

#### Sorting Arrays
  * Sort an array <code> a.sort() </code>
  * Sort the elements of an array's axis <code> c.sort(axis=0) </code>

<!--
<table align="center">
    <tr>
        <td align="center"><img src="docs/img1.png?raw=true" alt="some text"></td>
        <td align="center">Some other text</td>
        <td align="center">More text</td>
    </tr>
    <tr>
        <td align="center"><img src="docs/img2.png?raw=true" alt="some text"></td>
        <td align="center">Some other text 2</td>
        <td align="center">More text 2</td>
    </tr>
</table>
 -->  
##### Asking For Help
 * <code> np.info(np.ndarray.dtype) </code>
