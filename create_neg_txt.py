
import os
import numpy as np
 
with open('neg.txt', 'w') as f:
    for img in os.listdir('neg'):
        line = 'neg/'+img+'\n'
        f.write(line)
