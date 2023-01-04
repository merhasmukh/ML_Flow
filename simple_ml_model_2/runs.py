import numpy as np
import os

alphas=np.linspace(0.1,1.0,5)
l1_ratios_s=np.linspace(0.1,1.0,5)

for alpha in alphas:
    for l1 in l1_ratios_s:
        print(alpha,l1)
        os.system(f"python3 simple_ml_model_2.py -a {alpha} -l1 {l1}")