import numpy as np
data = np.load("sample_treated.npz")

def increase(data):
    ff = data['outputs']
    if_doubled = []
    for row in ff:
        if row[0] * 2 < row[-1]:
            if_doubled.append(True)
        else:
            if_doubled.append(False)
    doubled = ff[if_doubled]
    count = len(doubled)
    print(f"There are {count} objects which doubled its size.")
    return(doubled)
