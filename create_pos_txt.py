
import os
import numpy as np
 
with open('pos.txt', 'w') as f:
    for img in os.listdir('pos'):
        line = 'pos/'+img+' 1 0 0 20 20'+'\n'
        f.write(line)
