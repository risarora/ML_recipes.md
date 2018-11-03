### Set default Directory

```python
jupyter notebook --generate-config

(C:\ProgramData\Anaconda) C:\Users\user>jupyter notebook --generate-config
Overwrite C:\Users\user\.jupyter\jupyter_notebook_config.py with default config? [y/N]

```
```
c.NotebookApp.notebook_dir = 'C:\Users\users\git'
c.NotebookApp.password_required = True
```


#### jupyter notebook Basic navigation shortcuts
* Basic navigation: <code>enter</code>, <code>shift-enter</code>, <code>up/k</code>, <code>down/j</code>
* Saving the notebook: <code>s</code>
* Cell types: <code>y</code>, <code>m</code>, <code>1-6</code>, <code>t</code>
* Cell creation: <code>a</code>, <code>b</code>
* Cell editing: <code>x</code>, <code>c</code>, <code>v</code>, <code>d</code>, <code>z</code>, <code>shift+=</code>
* Kernel operations: <code>i</code>, <code>.</code>


#### Version Control with  jupyter notebooks

https://github.com/jupyter/nbdime

While git is very useful for comparing line-based scripts, it does not work well with notebook which essentially is a JSON file.

<code>nbdime</code> provides tools for <code>diffing</code> and <code>merging</code> of Jupyter Notebooks.


  The extension is available in both Jupyter Notebook and JupyterLab


### Installation
If you don’t have Jupyter Notebook extension enable, you can follow this.
<code>pip install nbdime</code>

For extension in Jupyter Notebook

* <code>nbdiff</code> compare notebooks in a terminal-friendly way
* <code>nbmerge</code> three-way merge of notebooks with automatic conflict resolution
* <code>nbdiff</code>-web shows you a rich rendered diff of notebooks
* <code>nbmerge</code>-web gives you a web-based three-way merge tool for notebooks
* <code>nbshow</code> present a single notebook in a terminal-friendly way

http://192.168.1.35:1234/
