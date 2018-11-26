


[tqdm]("tqdm-jupyter-1.gif" "Logo Title Text 1")

<p align="center">
<img src="../images/Modeling/tqdm-jupyter-1.gif" width="600px" >
</p>




```
from tqdm import tqdm_notebook as tqdm

from time import sleep
from tqdm import tqdm

values = range(3)
with tqdm(total=len(values)) as pbar:
    for i in values:
        pbar.write('processed: %d' %i)
        pbar.update(1)
        sleep(1)

  0%|          | 0/3 [00:00<?, ?it/s]
processed: 1
 67%|██████▋   | 2/3 [00:01<00:00,  1.99it/s]
processed: 2
100%|██████████| 3/3 [00:02<00:00,  1.53it/s]
processed: 3
```
