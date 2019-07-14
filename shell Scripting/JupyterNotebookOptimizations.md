# Save Numpy Object
from tempfile import TemporaryFile
outfile = TemporaryFile()

x = np.arange(10)
np.save(outfile, x)

outfile.seek(0) # Only needed here to simulate closing & reopening file
np.load(outfile)


################################################################################################

#  Profiling the memory usage of your code with memory_profiler
https://ipython-books.github.io/

In this recipe, we will look at a simple memory profiler unsurprisingly named memory_profiler. Its usage is very similar to line_profiler, and it can be conveniently used from IPython.

Getting ready
You can install memory_profiler with <mark>conda install memory_profiler.</mark>

## Steps for memory profiling
1.  We load the memory_profiler IPython extension:
```
%load_ext memory_profiler
```
2.  We define a function that allocates big objects:
```
%%writefile memscript.py
def my_func():
    a = [1] * 1000000
    b = [2] * 9000000
    del b
    return a
```
3.  Now, let's run the code under the control of the memory profiler:
```
from memscript import my_func
%mprun -T mprof0 -f my_func my_func()
```
*** Profile printout saved to text file mprof0.
4.  Let's show the results:
```
print(open('mprof0', 'r').read())
Line #  Mem usage    Increment   Line Contents
================================================
   1     93.4 MiB      0.0 MiB   def my_func():
   2    100.9 MiB      7.5 MiB       a = [1] * 1000000
   3    169.7 MiB     68.8 MiB       b = [2] * 9000000
   4    101.1 MiB    -68.6 MiB       del b
   5    101.1 MiB      0.0 MiB       return a
```
We can observe line after line the allocation and deallocation of objects.

How it works...
The memory_profiler package checks the memory usage of the interpreter at every line. The increment column allows us to spot those places in the code where large amounts of memory are allocated. This is especially important when working with arrays. Unnecessary array creations and copies can considerably slow down a program. We will tackle this issue in the next few recipes.

There's more...
The memory_profiler IPython extension also comes with a %memit magic command that lets us benchmark the memory used by a single Python statement. Here is a simple example:
```
%%memit import numpy as np
np.random.randn(1000000)
peak memory: 101.20 MiB, increment: 7.77 MiB
```
The memory_profiler package offers other ways to profile the memory usage of a Python program, including plotting the memory usage as a function of time. For more details, refer to the documentation at https://github.com/pythonprofilers/memory_profiler.

IPython Cookbook, Second Edition

Profiling your code line-by-line with line_profiler
Understanding the internals of NumPy to avoid unnecessary array copying

##############################################
# View Memory usage by various objects
```
import sys

# These are the usual ipython objects, including this one you are creating
ipython_vars = ['In', 'Out', 'exit', 'quit', 'get_ipython', 'ipython_vars']

# Get a sorted list of the objects and their sizes
sorted([(x, sys.getsizeof(globals().get(x))) for x in dir() if not x.startswith('_') and x not in
sys.modules and x not in ipython_vars], key=lambda x: x[1], reverse=True)
```

##############################################
```
import pandas as pd
import numpy as np
import holoviews as hv
from holoviews.operation.datashader import aggregate, shade, datashade, dynspread
import sys

hv.extension('bokeh')

n,k = 1_000_000,4
scales=np.linspace(1,10,k)

df = pd.concat([s * pd.DataFrame({
    'x1' : np.random.randn(n),
    'x2' : np.abs(np.random.randn(n)),
    'x3' : np.random.chisquare(1, n),
    'x4' : np.random.uniform(0,s,n),
    'y' : np.random.randn(n),
    's' : np.full(n, 1)
}) for s in scales])

def extend_range(p, frac):
    a, b = np.min(p), np.max(p)
    m, l = (a + b) / 2, (b - a) / 2
    rv = (m - frac * l, m + frac * l)
    return rv

def pad_scatter(s: hv.Scatter, frac=1.05):
    df = s.dframe()
    r = {d.name: extend_range(df[d.name], frac) for d in (s.kdims + s.vdims)[0:2]}
    return s.redim.range(**r)

print(f'df is around {sys.getsizeof(df) // 1024_000} MB')
```
##############################################

##############################################


##############################################


##############################################


##############################################

conda install -c anaconda dill
To save the Jupyter Notebook session:

import dill
dill.dump_session('notebook_session.db')
To restore the  session:

import dill
dill.load_session('notebook_session.db')

##############################################
https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/
2. Pretty Display of Variables

IPython Magic
* %env: Set Environment Variables
* %run: Execute python code
11. %%time:  will give you information about a single run of the code in your cell.
12. %who: List all variables of global scope.
13. %prun: Show how much time your program spent in each function.Using `%prun
statement_name`
14. %pdb :Debugging with %pdb

24. Jupyter-contrib extensions

Jupyter-contrib extensions is a family of extensions which give Jupyter a lot more functionality,
including e.g. </mark>jupyter spell-checker</mark> and <mark>code-formatter</mark>.


```
!pip install https://github.com/ipython-contrib/jupyter_contrib_nbextensions/tarball/master
!pip install jupyter_nbextensions_configurator
!jupyter contrib nbextension install --user
!jupyter nbextensions_configurator enable --user
```
