import matplotlib.pyplot as plt
import numpy as np
def plot_world(world):
    if type(world) == list:
        A = np.array([world])
    else:
        A = world
    
    plt.figure(figsize=(5,4)) # (30,30) = Taille de la figure
    plt.imshow(A,cmap='cividis')
    plt.tick_params(top=False, bottom=False, right=False, left=False, labelleft=False, labelbottom=False)
    plt.show()
    
def graphique(M):
    for i in range(24):
        plot_world(M[i])

import time
def in_time(d,N):
    
    A = zero_0(d,N)
    print(A, end="\r")
    time.sleep(5)
    plt.clf()
    B = zero_90(d,N)
    print(B)


in_time(10,6)


